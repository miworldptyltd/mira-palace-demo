/**
 * mira-palace-enquiry — Cloudflare Worker
 * ---------------------------------------
 * Receives room + spa enquiry POSTs from the public site, verifies the
 * Cloudflare Turnstile token, applies a naive per-IP rate limit, sanitises
 * the fields, and forwards a formatted email to the hotel inbox via Resend.
 *
 * R029: first version — the enquiry form pipeline was a stub before this.
 *
 * Env vars (set in the Cloudflare dashboard, NEVER commit the values):
 *   RESEND_API_KEY     - Resend API key (from resend.com dashboard)
 *   TURNSTILE_SECRET   - Cloudflare Turnstile secret key (widget dashboard)
 *   TO_EMAIL           - Where to deliver enquiries (e.g. info@miworld.tech)
 *   FROM_EMAIL         - Verified Resend sender (e.g. onboarding@resend.dev)
 *   ALLOWED_ORIGINS    - Comma-separated allowlist. During demo:
 *                        "https://miworldptyltd.github.io"
 *                        Production adds:
 *                        "https://sidemirapalace.com,https://www.sidemirapalace.com"
 *
 * Optional bindings:
 *   RATE_LIMIT_KV      - Workers KV namespace for rate limiting. If unbound
 *                        the Worker still works but skips rate limiting.
 */

// -----------------------------------------------------------------------
// Config
// -----------------------------------------------------------------------

// Max enquiries per IP per rolling window (both room + spa combined).
const RATE_LIMIT_MAX     = 5;
const RATE_LIMIT_WINDOW  = 60 * 60; // 1 hour in seconds

// Reject payloads larger than this — real enquiries fit comfortably in 4 KB.
const MAX_BODY_BYTES     = 16 * 1024;

// Turnstile verification endpoint.
const TURNSTILE_VERIFY_URL =
  'https://challenges.cloudflare.com/turnstile/v0/siteverify';

// Resend API endpoint.
const RESEND_URL = 'https://api.resend.com/emails';

// -----------------------------------------------------------------------
// Entry point
// -----------------------------------------------------------------------

export default {
  async fetch(request, env, ctx) {
    // 1. CORS preflight — respond fast, no state changes.
    if (request.method === 'OPTIONS') {
      return handleCorsPreflight(request, env);
    }

    // 2. Only POST is accepted for the main flow.
    if (request.method !== 'POST') {
      return json(
        { ok: false, error: 'method-not-allowed' },
        405,
        corsHeaders(request, env)
      );
    }

    try {
      // 3. Origin allowlist (defence in depth — also enforced by CORS).
      const origin = request.headers.get('Origin') || '';
      if (!isAllowedOrigin(origin, env)) {
        return json(
          { ok: false, error: 'origin-not-allowed' },
          403,
          corsHeaders(request, env)
        );
      }

      // 4. Body size cap.
      const clen = Number(request.headers.get('Content-Length') || '0');
      if (clen && clen > MAX_BODY_BYTES) {
        return json(
          { ok: false, error: 'payload-too-large' },
          413,
          corsHeaders(request, env)
        );
      }

      // 5. Parse JSON.
      let payload;
      try {
        payload = await request.json();
      } catch (_) {
        return json(
          { ok: false, error: 'invalid-json' },
          400,
          corsHeaders(request, env)
        );
      }

      // 6. Shape guard.
      const kind = String(payload?.kind || '').toLowerCase();
      const emailObj = payload?.email;
      const turnstileToken = String(payload?.turnstileToken || '');

      if (kind !== 'room' && kind !== 'spa') {
        return json(
          { ok: false, error: 'invalid-kind' },
          400,
          corsHeaders(request, env)
        );
      }
      if (!emailObj || typeof emailObj !== 'object') {
        return json(
          { ok: false, error: 'invalid-email-object' },
          400,
          corsHeaders(request, env)
        );
      }
      if (!turnstileToken) {
        return json(
          { ok: false, error: 'missing-turnstile-token' },
          400,
          corsHeaders(request, env)
        );
      }

      // 7. Rate limit by client IP.
      const clientIp = request.headers.get('CF-Connecting-IP') || '0.0.0.0';
      const rlOk = await checkRateLimit(clientIp, env);
      if (!rlOk) {
        return json(
          { ok: false, error: 'rate-limited' },
          429,
          corsHeaders(request, env)
        );
      }

      // 8. Server-side Turnstile verification.
      const tsOk = await verifyTurnstile(turnstileToken, clientIp, env);
      if (!tsOk) {
        return json(
          { ok: false, error: 'turnstile-failed' },
          403,
          corsHeaders(request, env)
        );
      }

      // 9. Sanitise email fields (strip control chars, cap length).
      const safe = sanitiseEmailObject(emailObj);

      // 10. Send via Resend.
      const sendResult = await sendViaResend(kind, safe, env);
      if (!sendResult.ok) {
        return json(
          { ok: false, error: 'send-failed', detail: sendResult.detail },
          502,
          corsHeaders(request, env)
        );
      }

      // 11. Success.
      return json(
        { ok: true, id: sendResult.id },
        200,
        corsHeaders(request, env)
      );
    } catch (err) {
      // Belt & braces — never leak stack traces.
      console.error('[enquiry] unhandled', err && err.message);
      return json(
        { ok: false, error: 'internal' },
        500,
        corsHeaders(request, env)
      );
    }
  },
};

// -----------------------------------------------------------------------
// CORS
// -----------------------------------------------------------------------

function isAllowedOrigin(origin, env) {
  const allow = (env.ALLOWED_ORIGINS || '')
    .split(',')
    .map((s) => s.trim())
    .filter(Boolean);
  return allow.includes(origin);
}

function corsHeaders(request, env) {
  const origin = request.headers.get('Origin') || '';
  const allow = isAllowedOrigin(origin, env) ? origin : '';
  return {
    'Access-Control-Allow-Origin': allow,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
    Vary: 'Origin',
  };
}

function handleCorsPreflight(request, env) {
  return new Response(null, {
    status: 204,
    headers: corsHeaders(request, env),
  });
}

// -----------------------------------------------------------------------
// Rate limit (Workers KV; if unbound, no-op)
// -----------------------------------------------------------------------

async function checkRateLimit(ip, env) {
  if (!env.RATE_LIMIT_KV) return true; // KV not bound → skip

  const key = `rl:${ip}`;
  const raw = await env.RATE_LIMIT_KV.get(key);
  const count = raw ? parseInt(raw, 10) : 0;

  if (count >= RATE_LIMIT_MAX) return false;

  // Increment and set TTL.
  await env.RATE_LIMIT_KV.put(key, String(count + 1), {
    expirationTtl: RATE_LIMIT_WINDOW,
  });
  return true;
}

// -----------------------------------------------------------------------
// Turnstile server-side verify
// -----------------------------------------------------------------------

async function verifyTurnstile(token, ip, env) {
  if (!env.TURNSTILE_SECRET) {
    console.error('[enquiry] TURNSTILE_SECRET not set');
    return false;
  }
  const form = new FormData();
  form.append('secret', env.TURNSTILE_SECRET);
  form.append('response', token);
  form.append('remoteip', ip);

  try {
    const r = await fetch(TURNSTILE_VERIFY_URL, { method: 'POST', body: form });
    const data = await r.json();
    return Boolean(data && data.success);
  } catch (err) {
    console.error('[enquiry] turnstile verify error', err && err.message);
    return false;
  }
}

// -----------------------------------------------------------------------
// Sanitise
// -----------------------------------------------------------------------

function sanitiseEmailObject(email) {
  return {
    from:    sanitiseString(email.from,    120),
    to:      sanitiseString(email.to,      120),
    subject: sanitiseString(email.subject, 200),
    body:    sanitiseString(email.body,    8000),
  };
}

function sanitiseString(v, maxLen) {
  if (v == null) return '';
  let s = String(v);
  // Strip control chars except \n and \t.
  s = s.replace(/[ --]/g, '');
  // Collapse >2 blank lines.
  s = s.replace(/\n{3,}/g, '\n\n');
  if (s.length > maxLen) s = s.slice(0, maxLen);
  return s;
}

// -----------------------------------------------------------------------
// Resend
// -----------------------------------------------------------------------

async function sendViaResend(kind, safe, env) {
  if (!env.RESEND_API_KEY) {
    return { ok: false, detail: 'RESEND_API_KEY missing' };
  }

  const to      = env.TO_EMAIL   || 'info@miworld.tech';
  const from    = env.FROM_EMAIL || 'onboarding@resend.dev';
  const subject = safe.subject || `Mira Palace ${kind} enquiry`;

  // HTML wrapper — hotel staff want scannable, not markdown.
  const html = renderStaffEmailHtml(kind, safe);

  const body = {
    from:    `Mira Palace enquiries <${from}>`,
    to:      [to],
    reply_to: safe.from || undefined,
    subject,
    text:    safe.body,
    html,
  };

  try {
    const r = await fetch(RESEND_URL, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${env.RESEND_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    });
    if (!r.ok) {
      const txt = await r.text();
      return { ok: false, detail: `resend-${r.status}: ${txt.slice(0, 200)}` };
    }
    const data = await r.json();
    return { ok: true, id: data.id };
  } catch (err) {
    return { ok: false, detail: (err && err.message) || 'network-error' };
  }
}

// -----------------------------------------------------------------------
// Email template — designed for hotel staff at 6am with one eye open.
// -----------------------------------------------------------------------

function renderStaffEmailHtml(kind, safe) {
  const isSpa = kind === 'spa';
  const bandColour = isSpa ? '#8E6D2F' : '#132630';
  const label = isSpa ? 'Spa enquiry' : 'Room enquiry';

  // Escape user-provided strings before dropping into HTML. Amp first (order matters).
  const esc = (s) =>
    String(s || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');

  // The body is already a formatted plaintext block from the client.
  // Preserve line breaks; escape HTML.
  const bodyHtml = esc(safe.body).replace(/\n/g, '<br>');

  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>${esc(safe.subject)}</title>
</head>
<body style="margin:0;padding:0;background:#f4f5f7;font-family:'Segoe UI',-apple-system,BlinkMacSystemFont,sans-serif;color:#111827;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f4f5f7;padding:24px 0;">
    <tr>
      <td align="center">
        <table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;background:#ffffff;border-radius:8px;overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.05);">
          <tr>
            <td style="background:${bandColour};color:#F2F6F7;padding:20px 28px;font-size:14px;letter-spacing:0.16em;text-transform:uppercase;">
              Mira Palace &middot; ${label}
            </td>
          </tr>
          <tr>
            <td style="padding:28px;">
              <p style="margin:0 0 16px 0;font-size:16px;line-height:1.5;color:#111827;">
                A new enquiry has arrived from the website.
              </p>
              <p style="margin:0 0 8px 0;font-size:13px;color:#6b7280;">
                <strong>From:</strong> ${esc(safe.from)}
              </p>
              <p style="margin:0 0 20px 0;font-size:13px;color:#6b7280;">
                <strong>Subject:</strong> ${esc(safe.subject)}
              </p>
              <div style="border-top:1px solid #e5e7eb;padding-top:20px;font-size:14px;line-height:1.6;color:#111827;font-family:'SFMono-Regular',Menlo,Consolas,monospace;">
                ${bodyHtml}
              </div>
              <p style="margin:24px 0 0 0;font-size:12px;color:#9ca3af;">
                Reply directly to this email to respond to the guest.
              </p>
            </td>
          </tr>
          <tr>
            <td style="background:#f9fafb;color:#9ca3af;padding:16px 28px;font-size:11px;text-align:center;">
              Mira Palace &middot; Side, Antalya, T&uuml;rkiye
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>`;
}

// -----------------------------------------------------------------------
// Helpers
// -----------------------------------------------------------------------

function json(obj, status, extraHeaders) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      ...(extraHeaders || {}),
    },
  });
}
