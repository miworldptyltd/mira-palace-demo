# Mira Palace enquiry Worker

The Cloudflare Worker that receives room + spa enquiry submissions from the public site and forwards them by email via Resend.

## Files

- `mira-palace-enquiry.js` — the Worker source (single file, no build step required)
- `wrangler.toml` — Wrangler config for CLI deploys

## Deploy path A — Cloudflare dashboard (no CLI, no auth setup)

1. Open Cloudflare dashboard → **Workers & Pages** → **mira-palace-enquiry**. Create it if it doesn't exist.
2. Click **Edit code**.
3. Delete the default handler. Paste the entire contents of `mira-palace-enquiry.js`. Click **Save and deploy**.
4. Go to **Settings → Variables**. Add these five variables. Tick **Encrypt** on every one so they're stored as secrets:
   - `RESEND_API_KEY` — from resend.com dashboard
   - `TURNSTILE_SECRET` — from Cloudflare Turnstile widget settings (Secret Key, NOT Site Key)
   - `TO_EMAIL` — `info@miworld.tech` for the demo phase
   - `FROM_EMAIL` — `onboarding@resend.dev` until we verify a real domain in Resend
   - `ALLOWED_ORIGINS` — `https://miworldptyltd.github.io` for now. Comma-separated for multiple hosts at launch.
5. Optional but recommended — enable rate limiting with Workers KV:
   - Go to **Workers KV** in the sidebar.
   - Click **Create namespace**. Name it `MIRA_ENQUIRY_RATE`.
   - Back in the Worker, go to **Settings → Bindings → + Add → KV Namespace**.
   - Variable name: `RATE_LIMIT_KV`. Select the namespace you just made. Save.

The Worker now enforces: server-side Turnstile verification, origin allowlist, per-IP rate limit (5 enquiries per hour if KV is bound), payload size cap, input sanitisation, and HTML-safe email formatting for hotel staff.

## Deploy path B — Wrangler CLI (better long-term, first-time setup ~10 min)

Prereqs: Node.js 20+, npm.

```
npm i -g wrangler
wrangler login
cd worker
wrangler deploy
wrangler secret put RESEND_API_KEY
wrangler secret put TURNSTILE_SECRET
wrangler secret put TO_EMAIL
wrangler secret put FROM_EMAIL
wrangler secret put ALLOWED_ORIGINS
```

Optional KV rate limiting:

```
wrangler kv:namespace create MIRA_ENQUIRY_RATE
# Copy the id from the output, paste into wrangler.toml under [[kv_namespaces]]
wrangler deploy
```

## Endpoint contract

**POST** `https://mira-palace-enquiry.<subdomain>.workers.dev`

Request body (from `site.js`):

```
{
  "kind": "room" | "spa",
  "email": {
    "from":    "guest@example.com",
    "to":      "info@mirapalace.com",
    "subject": "Mira Palace enquiry · Family Suite · 2026-08-01–08-05 · Doe",
    "body":    "A new enquiry has arrived...\n\nGuest: Jane Doe\n..."
  },
  "turnstileToken": "…"
}
```

Response:

```
200 { "ok": true,  "id": "resend-message-id" }
400 { "ok": false, "error": "invalid-json" | "invalid-kind" | ... }
403 { "ok": false, "error": "origin-not-allowed" | "turnstile-failed" }
413 { "ok": false, "error": "payload-too-large" }
429 { "ok": false, "error": "rate-limited" }
502 { "ok": false, "error": "send-failed", "detail": "…" }
```

## Testing

The Worker logs to Cloudflare's built-in observability. `wrangler tail` shows live logs. Test manually with:

```
curl -X POST https://mira-palace-enquiry.<subdomain>.workers.dev \
  -H "Origin: https://miworldptyltd.github.io" \
  -H "Content-Type: application/json" \
  -d '{"kind":"room","email":{"from":"test@example.com","to":"info@miworld.tech","subject":"probe","body":"probe body"},"turnstileToken":"XXXX.DUMMY.TOKEN.XXXX"}'
```

You'll get `403 turnstile-failed` back — expected without a real token. Once the site posts with a real Turnstile token, it will succeed.
