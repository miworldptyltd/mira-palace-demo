# FUTURE ENHANCEMENTS — Mira Palace

> Ideas that aren't in the current phase. Captured the moment they come up (§7.1). Nothing is deleted — closed items move to the bottom under "Closed / decided" (§7.3).

---

## Open

### Content & language

- **[M] TR / DE / RU translations** — ship English v1 first, freeze source copy, then translate. Reason: retranslating is expensive (§5.2). Raised by: AWA §5. When: Phase 2 after owner content sign-off.
- **[L] Professional photography** — hotel likely needs a proper photoshoot for rooms / pools / dining / spa. Mock uses Unsplash placeholders. Raised by: site-analysis-v1.md §7. When: Phase 2 prerequisite.
- **[S] Real Hotel Policies** in proper English + original Turkish (current site's Turkish policies page has character-encoding corruption). Raised by: site-analysis-v1.md §3. When: Phase 2 when owner clarifies which version is authoritative.

### Booking & commerce

- **[M] Real booking engine integration** — current live site uses a Caglatur-like third-party engine; mock site uses a stubbed enquiry form. Decide: keep Caglatur, switch (e.g. HotelRunner, SiteMinder, Cloudbeds), or run direct-plus-OTA. Raised by: site-analysis-v1.md §5. When: Phase 2.
- **[S] Price display & seasonal calendar** — needs rate card. Blocked on owner rate strategy. Raised by: site-analysis §6. When: Phase 2.
- **[S] Gift voucher / spa voucher e-commerce** — some resort hotels offer. Speculative. Raised by: agent. When: Phase 3.

### Trust & SEO

- **[S] Schema.org Hotel / LocalBusiness / Room structured data** — helps Google rich results. Simple to add. Raised by: site-analysis §5. When: can land during Phase 1 if time permits.
- **[S] Google reviews / TripAdvisor badge** — pulls live rating onto home page. Raised by: site-analysis §6. When: Phase 2 once owner confirms accounts.
- **[M] Turizm İşletme Belgesi + licence numbers in footer** — Turkish regulatory compliance. Raised by: agent. When: Phase 2 with owner-confirmed data.

### Copy / protection

- **[S] Cloudflare Access password gate on preview URL** — belt-and-braces on top of the obscure-URL approach. Useful if owner starts sharing the link more widely. Raised by: agent. When: on demand.
- **[S] Copy-protection light-touch:** disable right-click on images, watermark photos with subtle "Mira Palace" in corner. Security theatre but deters casual copying. Raised by: owner query (2026-04-25). When: Phase 1 if trivially doable.

### Accessibility & quality

- **[M] WCAG 2.2 AA audit** — colour contrast, keyboard nav, alt text, aria-labels. Raised by: agent. When: Phase 2.
- **[S] Lighthouse CI in the deploy workflow** — fail the build if scores drop. Raised by: agent. When: Phase 2.
- **[S] 404 with route suggestions** — nice to have. Raised by: agent. When: Phase 1 basic version, Phase 2 smart.

### Features

- **[L] Member / returning-guest login** — "my booking" area. Speculative. Raised by: agent. When: only if owner asks.
- **[M] Weddings & events page** — some hotels offer. Depends on owner. Raised by: agent. When: if confirmed.
- **[M] Blog / stories** — good for SEO but needs ongoing content. Raised by: agent. When: Phase 3.
- **[S] Newsletter signup** — needs consent flow (§4.2 unbundled consent). Raised by: agent. When: Phase 2.
- **[S] Real enquiry form backend** — currently mailto / stub. Options: Formspree, Netlify Forms, a tiny Cloudflare Worker. Raised by: agent. When: Phase 2.

### Operations

- **[S] Analytics** — Plausible or GA4. Needs cookie consent (§4). Raised by: agent. When: Phase 2.
- **[S] Sitemap.xml + robots.txt** — trivial for SEO. Raised by: agent. When: Phase 1.
- **[S] Favicon set + OG / Twitter cards** — trivial, social-sharing looks. Raised by: agent. When: Phase 1.

---

## Closed / decided

*(Nothing yet.)*
