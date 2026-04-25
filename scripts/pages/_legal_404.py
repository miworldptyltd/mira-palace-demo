from common import hero, section, SITE_META


LEGAL_HERO_IMG = "https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&w=1920&q=80"


def _legal_wrap(root: str, title: str, sub: str, body_html: str) -> str:
    h = hero(LEGAL_HERO_IMG, "Legal", title, sub, height="50vh")
    body = section(f'<article class="prose prose-mira max-w-3xl">{body_html}</article>', bg="bg-white")
    return h + body


def privacy(root: str) -> str:
    html = """
      <p class="text-sm text-mira-600">Last updated: 25 April 2026 · Version 1 (demo)</p>
      <h2>1. Who we are</h2>
      <p>Mira Palace is operated by [OPERATING COMPANY NAME, T.C. TAX ID: PLACEHOLDER] at Evrenseki Mahallesi, Kömürcüler Küme Evleri No:96, Manavgat/Antalya, Türkiye. In the terms below "we", "us" and "the hotel" all mean the operating company.</p>
      <h2>2. What data we collect</h2>
      <ul>
        <li><strong>Enquiry &amp; booking data</strong> — name, email, phone, arrival / departure dates, room preferences, any specific requirements you tell us about (accessibility, dietary needs, anniversaries).</li>
        <li><strong>Stay data</strong> — check-in identification (as required by Turkish law), room-charge ledger, spa and restaurant charges.</li>
        <li><strong>Marketing data</strong> — only if you have opted in to our newsletter, separately from your booking consent.</li>
        <li><strong>Career applications</strong> — the details you enter into the careers form, including your CV.</li>
      </ul>
      <h2>3. Why we hold it</h2>
      <p>To answer your enquiry, honour your booking, perform your stay, comply with Turkish hospitality and tax law, and — only with your separate consent — to tell you about future offers. We do not sell your data to anyone, ever.</p>
      <h2>4. How long we keep it</h2>
      <ul>
        <li><strong>Enquiries that don’t turn into stays:</strong> 24 months, then deleted.</li>
        <li><strong>Stays:</strong> 10 years, to comply with Turkish tax and hospitality record-keeping.</li>
        <li><strong>Marketing consent:</strong> until you unsubscribe; confirmed every 24 months.</li>
        <li><strong>Career applications:</strong> 12 months after the last communication, unless you ask us to keep them longer.</li>
      </ul>
      <h2>5. Your rights</h2>
      <p>You can ask us at any time to access, correct, export or delete your personal data, and to withdraw any consent you’ve given. Email <a href="mailto:info@sidemirapalace.com">info@sidemirapalace.com</a> with "data request" in the subject line. We respond within 30 days.</p>
      <h2>6. Lawful basis</h2>
      <p>Enquiries and bookings: contract. Legal records: compliance with Turkish law (KVKK / VUK). Marketing: your separate explicit consent.</p>
      <h2>7. Cookies</h2>
      <p>See the <a href="legal/cookies.html">Cookie Notice</a>.</p>
      <h2>8. Contact</h2>
      <p>Written communications: Mira Palace, Evrenseki Mahallesi, Kömürcüler Küme Evleri No:96, Manavgat/Antalya, Türkiye. Email: <a href="mailto:info@sidemirapalace.com">info@sidemirapalace.com</a>.</p>
      <p class="text-sm text-mira-600 italic">DEMO SITE NOTICE: this policy is a realistic placeholder. The real, legally reviewed version must be provided before public launch, per the project’s legal-gate rule. Do not rely on this wording for real guests.</p>
    """
    return _legal_wrap(root, "Privacy Notice", "How we handle personal data.", html)


def cookies(root: str) -> str:
    html = """
      <p class="text-sm text-mira-600">Last updated: 25 April 2026 · Version 1 (demo)</p>
      <h2>1. What cookies we use on this site</h2>
      <p>This demonstration build uses <strong>no</strong> tracking or analytics cookies. In the production site, we will use strictly the minimum necessary:</p>
      <ul>
        <li><strong>Essential session cookies</strong> — remember your language preference and the state of the enquiry form. Never used for analytics.</li>
        <li><strong>Privacy-friendly analytics</strong> — aggregated, no cross-site tracking, no advertising networks. You will be asked once for consent.</li>
      </ul>
      <h2>2. How to turn them off</h2>
      <p>Any browser lets you refuse cookies — the site will still work. The analytics cookies are off by default until you opt in.</p>
      <h2>3. Third-party embedded content</h2>
      <p>Google Maps embeds on the Location and Contact pages may set their own cookies. If you would like these blocked, use a privacy extension or disable third-party cookies in your browser.</p>
    """
    return _legal_wrap(root, "Cookie Notice", "What we do, and don’t do, with cookies.", html)


def hotel_policies(root: str) -> str:
    html = """
      <p class="text-sm text-mira-600">Last updated: 25 April 2026 · Version 1 (demo)</p>
      <h2>Rates &amp; deposits</h2>
      <p>Rates are quoted in Euro, per room per night, and include 8 per cent VAT. Exchange rates quoted at booking may shift by the time the stay begins; the final bill will reflect the rate on checkout. A valid credit card is required to guarantee the booking.</p>
      <h2>Credit cards &amp; payments</h2>
      <p>Major credit cards (Visa, Mastercard) are accepted. The name on the card must match the name on the booking. Debit cards may be held for a pre-authorisation equal to the room total plus €200 as an incidentals deposit, released on checkout.</p>
      <h2>Check-in &amp; check-out</h2>
      <p>Check-in from 15:00; check-out by 12:00. Early check-in and late check-out are offered subject to availability. A late check-out between 12:00 and 18:00 is charged at half the day rate; after 18:00, a full day rate. Guests must be 18 or over to register, unless accompanied by a parent or guardian.</p>
      <h2>Smoking</h2>
      <p>Rooms and indoor public areas are non-smoking. Smoking is permitted on private balconies and in designated outdoor areas. Cleaning fees apply to violations.</p>
      <h2>Pets</h2>
      <p>Pets are not accepted in guest rooms or restaurants. Service animals are welcome.</p>
      <h2>Cancellation</h2>
      <p>Flexible rate: free cancellation up to 14 days before arrival. Within 14 days, one night is charged. Non-refundable rate: first night charged at booking, rest on arrival, no refund.</p>
      <h2>Children</h2>
      <p>Children 0–5 stay free when sharing with two adults. Children 6–12 pay a reduced rate. Children 13 and over are treated as adults for occupancy.</p>
      <h2>General provisions</h2>
      <p>By completing a booking, the guest accepts the hotel’s standard terms of stay. The hotel reserves the right to update these at any time without prior notice. Turkish law governs these terms.</p>
      <p class="text-sm text-mira-600 italic">DEMO SITE NOTICE: the real version of this document must be reviewed by the hotel’s legal advisor before public launch. This version is a clean English rewrite of the hotel’s existing policy (which was previously published only in Turkish and with broken character encoding).</p>
    """
    return _legal_wrap(root, "Hotel Policies", "The house rules, in plain English.", html)


def notfound(root: str) -> str:
    return hero(
        "https://images.unsplash.com/photo-1519046904884-53103b34b206?auto=format&fit=crop&w=1920&q=80",
        "404",
        "This page has gone swimming.",
        "The link you followed either never existed or has moved. Try the navigation above — or the friendly shortcuts below.",
        primary_href=f"{root}index.html", primary_label="Back to the home page",
        height="85vh",
    ) + section(
        f"""
        <div class="grid md:grid-cols-3 gap-5 text-center">
          <a href="{root}rooms/" class="p-7 bg-white rounded-lg shadow-lux hover:-translate-y-1 transition"><div class="font-display text-2xl text-mira-900">Rooms &amp; Suites</div><div class="mt-1 text-sm text-mira-600">Four room types, 22–42 m²</div></a>
          <a href="{root}dining/" class="p-7 bg-white rounded-lg shadow-lux hover:-translate-y-1 transition"><div class="font-display text-2xl text-mira-900">Dining</div><div class="mt-1 text-sm text-mira-600">Four outlets under one roof</div></a>
          <a href="{root}contact.html#enquiry" class="p-7 bg-white rounded-lg shadow-lux hover:-translate-y-1 transition"><div class="font-display text-2xl text-mira-900">Contact</div><div class="mt-1 text-sm text-mira-600">We’ll reply within the hour</div></a>
        </div>
        """,
        bg="bg-sand-50")


PAGES = [
    {"path": "legal/privacy.html", "active": "",
     "title": "Privacy Notice · Mira Palace",
     "description": "How Mira Palace handles your personal data, and your rights as a guest.",
     "body": privacy},
    {"path": "legal/cookies.html", "active": "",
     "title": "Cookie Notice · Mira Palace",
     "description": "How Mira Palace uses cookies (and why it’s a short list).",
     "body": cookies},
    {"path": "legal/hotel-policies.html", "active": "",
     "title": "Hotel Policies · Mira Palace",
     "description": "The house rules at Mira Palace — check-in, payments, smoking, pets, cancellation.",
     "body": hotel_policies},
    {"path": "404.html", "active": "",
     "title": "Not Found · Mira Palace",
     "description": "The page you were looking for could not be found.",
     "body": notfound},
]
