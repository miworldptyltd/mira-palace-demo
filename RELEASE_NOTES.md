# Mira Palace — Build Ledger

*Canonical record of what we have agreed on and built. Updated at each release.*

Different from [`CHANGELOG.md`](CHANGELOG.md) — that file is a running one-line-per-tag log. This file is a curated ledger a new developer or the hotel owner can read in ten minutes to understand where the project stands: what has been decided, what has been built, and what the guiding rules are.

Last significant update: **R028** (2026-07-06). See CHANGELOG.md for the tag-by-tag history.

---

## 1. Guiding principles

These are the hard rules the build is measured against. Any release that violates one is not shipped.

- **World-class foundation.** MVP is enquiry-only but the architecture must scale to payments + admin + multi-currency + traffic without a rewrite. No throwaway demo code.
- **Mobile-first.** Every UI change is designed at 375–428 px first and hand-verified at that width. The hotel owner spot-checks on their phone; their word is the ship-blocker.
- **Fix what's broken before starting new work.** Broken releases, failed deploys, half-shipped features all stop the next-idea train until they're finished. Deferred ≠ broken.
- **Translate in context, never literally.** Every TR/DE/RU/EN translation reads naturally to a native speaker for the specific hotel context; word-for-word is banned.
- **Contact + content honesty.** No fabricated facts on the site (no "private beach", no imaginary pool dimensions, no stock images that misrepresent Mira Palace's spaces).
- **Security in every form.** Turnstile + honeypot + input sanitization + rate-limit + origin check on every form; security headers via meta + Cloudflare proxy at cutover.
- **No dead code, no dead files.** Every release includes a housekeeping pass — orphaned assets, unused functions, and retired scripts are deleted, not left to rot.

---

## 2. Hotel facts (single source of truth)

Anything the site publishes about the hotel must match this list.

| Fact | Value |
|---|---|
| Suites | **34 total** — 19 Standard (A4, A5, B4, B5, C1–C15), 10 Deluxe (A1, A2, A3, A7, B1, B2, B3, B6, B7, B10), 4 Family (A8, A9, B8, B9), 1 King (A6) |
| Pools | **2** — one outdoor (seasonal), one heated indoor |
| Nearest beach | **Evrenseki Halk Plajı** — Blue Flag since 2010, ~700 m walk down the cypress-lined lane. Sandy, family-friendly, public — the hotel does NOT have a private beach |
| Address | Evrenseki Mahallesi, Kömürcüler Küme Evleri No:96, 07600 Manavgat / Antalya, Türkiye |
| Distances | Antalya airport (AYT) 60 km / ~45 min · Side old town 12 km · Manavgat waterfalls 18 km · Aspendos 33 km · Antalya Kaleiçi 65 km |
| Phones | Mobile / WhatsApp: +90 534 898 84 05 · Landline: +90 242 642 09 13 · Spa dedicated line: +90 532 543 15 90 |
| Instagram | Hotel main: [@sidemirapalace](https://www.instagram.com/sidemirapalace/) · Spa: [@sidemirapalacespawellness](https://www.instagram.com/sidemirapalacespawellness/) |
| Google rating | 4.3 / 5 from 118 reviews (as of R024 audit) |
| TripAdvisor | 3.8 / 5 from 13 reviews |
| Airport transfer | VIP minibus (Mercedes V-Class / Vito) — €85 private for up to 4, €25 per person shared |

Any release that publishes different numbers must first update this table AND explain why.

---

## 3. Content and copy decisions

- Every heading, paragraph and CTA carries a `data-i18n` key. Both `_home.py` (source HTML) and `i18n.js` (runtime dictionary) must be updated together — updating one without the other causes the runtime override bug we hit in R023.
- Translations use **warm "siz" for TR**, formal **"Sie" for DE**, formal **"вы" for RU**. All four languages are shipped for every page before it's considered done. Translation order: EN → TR → DE → RU.
- No "Complimentary shuttle to Side twice daily" (fabricated, removed in R023).
- Base currency is **EUR**. All published prices live in the central `PRICES` dictionary at the top of `scripts/common.py`. TRY and USD are computed from a hardcoded FX table (July 2026). Currency selector defaults to EUR (not USD).
- The current one-off Mi World build fee placeholder is **AUD $4,500**. See `Mira_Palace_Hosting_Overview.docx` for the full owner-facing cost breakdown.

---

## 4. Design system

- **Palette:** Midnight teal (`#132630 → #F2F6F7`, 10 stops named `mira-50…900`) + champagne gold (`#8E6D2F → #FBF8F1`, 7 stops named `sand-50…600`). Ink `#111827` for body text.
- **Fonts:** Cormorant Garamond (weights 400 & 600) for display headings; Inter (weights 300, 400, 500, 600, 700) for body. Loaded from Google Fonts with preconnect and `font-display: swap`.
- **Shadow:** custom `shadow-lux` (`0 20px 60px -20px rgb(19 38 48 / 0.35)`) on cards.
- **Icons:** Tabler Icons v3.44 webfont, async-loaded via `rel="preload" onload="this.rel='stylesheet'"` so it doesn't block first paint.
- **Flag icons:** flag-icons v7.5 CDN.

---

## 5. Stack (as of R024)

Every version below is intentional and current as of July 2026. See `CHANGELOG.md` R020 for the last modernisation pass.

| Layer | Choice | Notes |
|---|---|---|
| Site generator | Python 3.14 in CI · 3.10+ locally · stdlib only, no requirements.txt | Custom generator in `scripts/build.py` |
| Styling | **Tailwind CSS v4.3.2** compiled to `~72 KB` minified `site.css` | Standalone CLI, no Node.js dependency for local dev |
| Image optimisation | JPG → **WebP @ Q82** batch conversion via Pillow | Runs in Release.ps1 + GH Actions; ~39% byte saving vs JPG |
| Interactivity | Vanilla JS (`site.js` ~62 KB) + `i18n.js` dictionary (~130 KB with all 4 languages inline; gzipped ~30 KB) | No React, no Vue |
| Hosting | GitHub Pages (`miworldptyltd.github.io/mira-palace-demo`) | Planned prod cutover: sidemirapalace.com via Cloudflare Pages |
| CI/CD | GitHub Actions — `checkout@v6`, `setup-python@v6`, `upload-pages-artifact@v4`, `deploy-pages@v5` | ~30 seconds end-to-end. deploy-pages bumped to v5 in R028 for Node 24 runtime |
| Forms | Cloudflare Turnstile (bot check) + Cloudflare Worker (`mira-palace-enquiry.apps-224.workers.dev`) + Resend (email delivery) | Turnstile currently on test sitekey — parked pending owner-supplied real key |
| Version control | Git + GitHub with R-tagged releases (R001…R024) | `Release.ps1` orchestrates photo import → WebP → Tailwind compile → HTML build → tag → push |

---

## 6. Page inventory (28 HTML pages)

Every URL below is auto-generated by `scripts/build.py` from its Python module.

- `index.html` (home)
- `about.html`
- `book.html` (room enquiry)
- `spa-book.html` (spa package enquiry)
- `spa.html` · `spa-treatments.html`
- `dining/index.html` · `dining/main-restaurant.html` · `dining/pool-bar.html` · `dining/lobby-bar.html`
- `rooms/index.html` · `rooms/standard.html` · `rooms/deluxe.html` · `rooms/family.html` · `rooms/king.html` · `rooms/suite.html`
- `location.html` · `activities.html` · `gallery.html` · `offers.html` · `contact.html` · `concept.html` · `career.html` · `faq.html`
- `legal/privacy.html` · `legal/cookies.html` · `legal/hotel-policies.html`
- `404.html`

Retired pages (removed from build, listed in Release.ps1 `retiredPages` array so they can't leak back):
- `pools-beach.html` (R005 — pool content moved to home + dining/pool-bar)
- `assets/_spa_menu_source.pdf` (R017 — printed spa menu, source-only)

---

## 7. Feature ledger

*What has actually been built and shipped, grouped by area rather than by release.*

**Booking + enquiry pipeline**
- Room enquiry form on `book.html` with 4 suite tabs (Standard / Deluxe / Family / King), currency-aware pricing, add-ons (airport transfer / bus transfer / spa / late check-out / bike hire), Turnstile bot check, honeypot, arrival-time + occasion select fields, demo email preview gated behind `?demo=1`.
- Spa enquiry form on `spa-book.html` with 3 package tabs (Classic / Relax / Aromatherapy), date + time slot picker, party size 1–2, same Turnstile + honeypot infrastructure.
- All prices reference the central `PRICES` dict in `common.py`; one line edit changes all displayed prices site-wide.
- Currency selector in nav (TRY / EUR / USD), default EUR, converted via hardcoded July 2026 FX rates.

**Content pages**
- Full spa page rebuild (R017) modeled on Aman / Six Senses / Rosewood — 8-section blueprint with hero slideshow, philosophy, package cards, every-visit inclusions, facilities showcase, 5-stage ritual journey, etiquette, direct spa contact.
- Full dining hub rebuild (R019) with same 8-section blueprint + 3 venue sub-pages (Main Restaurant, Pool Bar, Lobby Bar).
- 4 room detail pages with real Mira Palace photography from R013.
- Location page with `location.html` distances table and airport transfer options (VIP minibus copy from R023).
- Real Google reviews block on home page (R023 → R025) — 4.3★ from 118 reviews. Three real quotes: Pelinsu Halıcı (family, June 2026), Rianne Van zandvoort (Netherlands, Nov 2025), Abdullah Topçu (couple, 2024). "Read all 118 reviews on Google" CTA.
- **Home hero reviews carousel (R025)** — the corner card in the hero (previously "Our specials") now shows one review at a time with dots + touch-swipe + arrow nav; tap to open a full-text modal with prev/next, dot nav, ESC to close. Auto-rotate every 8s, pauses on hover/focus, honours prefers-reduced-motion. Desktop lg+ only; mobile uses the below-hero 3-card grid.
- **"See our special offers" hero CTA (R025)** — ghost-style secondary button next to "Explore our suites", linking to /offers.html.
- **Offers page hero (R025)** — random-video-per-visit shuffler that picks from the 6 real hotel videos, no repeat within a browser session (sessionStorage-tracked). Previously a tropical palm-beach Unsplash fabrication.
- **Location page nearby-treasures cards (R025)** — Wikimedia Commons imagery for all four sites (Side/Apollo, Aspendos, Manavgat, Kaleiçi) with SME-verified two-sentence copy. Two `[VERIFY]` flags in code for 2026 Aspendos festival dates + Manavgat entrance fee.
- **Instagram 6-tile grid (R023 → R025)** — every tile now deep-links to a specific @sidemirapalace post URL (DaSuvMJN7Bm, DaK_8S2N8nA, DZ-ivNWtJ7p, DZ5HEt0tdfV, DZmqGdANJNU, DZURx0St9S3) captured by browser inspection of the live grid.

**SEO + structured data**
- Hotel `application/ld+json` schema.org data on every page — feeds Google's hotel rich result (star rating, location, photos, contact, amenities).
- Open Graph + Twitter Card meta on every page with locale alternates.
- Sitewide `noindex,nofollow` in the demo phase; flips to indexable at the R026 URL cutover.

**Internationalisation**
- 4 languages: English (source of truth), Turkish, German, Russian. All contextual, not literal.
- Language switcher in header nav (flag pills).
- "Translation in progress" notice for pages not yet fully localised.

**Deployment reliability**
- **R026** — Wikimedia Commons hotlink hostility → pivoted all Nearby Treasures cards to Pexels (Apollo, Aspendos, Manavgat, Kaleiçi).
- **R027** — VIP minibus image on Location page → dead Unsplash 1571043733612 swapped to Pexels 17455633 (black Mercedes V-Class).
- **R028** — GitHub Pages deploy job broke after 3 consecutive successful builds. Root cause: `actions/deploy-pages@v4` ships Node 20 which GitHub sunset 2026-09-16; v5 (2026-03-25) is the Node 24 build. One-line pin bump in `.github/workflows/deploy.yml` restored the pipeline.

**Performance (R024)**
- WebP conversion pipeline saving 39% on the 18 MB image budget.
- Tailwind CSS async-loaded so it doesn't block first paint.
- `content-visibility: auto` on below-fold sections for lazy paint.
- Tabler Icons stylesheet async-loaded.
- Cormorant Garamond trimmed to 2 weights.
- Cache-Control: no-cache meta on HTML so releases propagate instantly.
- Mobile 375–428 px viewport: floats collapsed to WhatsApp only.

---

## 8. Parked / deferred

See [`memory/project_mira_parked.md`](../spaces/…/memory/project_mira_parked.md) for the live parked list. Broad categories currently on the parking lot:

- **Waiting on owner action** — Turnstile Site Key, six Instagram post URLs, real Google reviews (some now captured), hosting migration go/no-go, final build fee.
- **Waiting on joint decision** — hosting migration timing, one-off Mi World build fee.
- **Deferred until later** — i18n.js per-language split (gzips small enough today), full inline-SVG Tabler icons (async load doing the job), PNG → SVG monogram, live FX API, URL migration to sidemirapalace.com (blocked by DNS), backend Phase 1 (Supabase + Workers).

---

## 9. What comes next

Immediately queued: **R025** — Location page cards with SME research + Wikimedia images, home hero reviews carousel replacing the Specials card, "See our offers" CTA in home hero, offers page hero as a randomised video shuffler, Instagram tiles deep-linked to specific posts, dead-code and dead-asset sweep, cache buster bump, ship.

After R025: R026 owner review pass, then production URL cutover to sidemirapalace.com pending DNS access, then backend Phase 1 (Supabase + admin panel + pricing calendar per `project_backend_plan.md`).

---

*This file is manually curated. When something material lands, update the relevant section and the "Last significant update" date at the top. Do not use it as a substitute for `CHANGELOG.md` — that stays a running per-tag log.*
