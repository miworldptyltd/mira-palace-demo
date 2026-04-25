# Mira Palace — Existing Site Analysis (v1)

**Source:** https://sidemirapalace.com/en/
**Crawled:** 2026-04-24
**Scope:** English site, 12 URLs visited (home, about, rooms x2, services x4, gallery, contact, career, concept, hotel-policies)

---

## TL;DR

The site has the *scaffolding* of a hotel website (nav, brand, phone number, reservation button, a polished home hero) but **most of the content pages are empty shells**. Every service page below displays only a title and falls back to the same two generic room teasers. The English site also leaks Turkish, leaks a different brand name ("Calimera Side Mira Palace"), and lists three different contact email domains. This is not a "polish it" situation — the content isn't there. A rebuild with a proper information architecture and real written content is the right call.

---

## 1. Structural issues (information architecture)

1. **Dead top-level nav items.** `ACCOMMODATION`, `SERVICES`, and `CONTACT` in the main nav are all `href="#"` — they only function as dropdown triggers. Clicking the parent does nothing. Accessibility and SEO suffer.
2. **Broken URL hygiene.** Standard Room lives at `/en/room/STANDARD%20ROOM` (literal space, uppercase). Deluxe Room at `/en/room/deluxe-room` (clean slug). Inconsistent across sibling pages.
3. **Label glitch.** The contact dropdown contains a duplicated item rendered as "CONTACT>" (with the angle bracket) next to "CAREER".
4. **Language switcher only has EN / RU / DE.** No Turkish public option, yet the English policies page actually renders in Turkish (see §3).
5. **No breadcrumbs, no room comparison, no rate display, no availability calendar.** The "Reservation" button triggers a hidden form with hardcoded static dates (check-in/out set to today+1) — not a real booking widget.
6. **Only two languages' footers are consistent.** No proper hreflang audit done (out of scope for this crawl).
7. **No visible schema.org / structured data for Hotel, Room, LocalBusiness.** Hurts Google rich results.

## 2. Empty / near-empty pages

| Page | URL | What's there | What should be there |
|---|---|---|---|
| Standard Room | `/en/room/STANDARD%20ROOM` | "22 m²" and a button labelled "Hemen İncele" (Turkish for "Review Now") | Beds, occupancy, view, amenities, bathroom, photos |
| Deluxe Room | `/en/room/deluxe-room` | Title only | Size, beds, occupancy, balcony/view, amenities, photos |
| Accommodation | `/en/service/accommodation` | Title + same 2 room teasers | Room-type overview, policy links |
| Beach & Pools | `/en/service/beach-pools` | Title only | Pool count/sizes, beach distance, sunbeds, towel service |
| Restaurant & Bar | `/en/service/restaurant-bar` | Title only | Restaurant concept, cuisine, hours, bars, à la carte |
| Spa & Wellness | `/en/service/spa-wellness` | Title only | Treatment menu, hammam, sauna, fitness |
| Gallery | `/en/gallery` | Header + one line "Photos from our hotels" | An actual gallery |
| Concept & General Information | `/en/document/concept-and-general-information` | Page title only | All-inclusive details, meal plan, timings, inclusions |

## 3. Content quality issues

1. **Hotel Policies is in Turkish on the English site** *and* the Turkish is served with broken character encoding (`ý` for `ı`, `þ` for `ş`, `ð` for `ğ` — classic Latin-1 / Windows-1254 mis-decode). Unreadable in either language.
2. **Hotel Policies has missing placeholders** where the hotel name should be substituted — lines begin with `'te hiçbir odada sigara içilmez` with nothing before the apostrophe.
3. **Career page name-leaks "Calimera Side Mira Palace"** — a different brand name appears nowhere else on the site.
4. **Three different contact email domains appear:**
   - Footer: `info@mirapalace.com`
   - Contact page: `info@sidemirapalace.com`
   - Hotel Policies: `info@aletrishotels.com`
5. **Outdated campaign copy.** Home hero still advertises "2024 Early Booking Opportunities" — we're in April 2026.
6. **About page is one short paragraph.** States: opened May 2022, operates 12 months, 34 rooms, 600m from the beach. That's the entire corpus of real prose on the site.
7. **No mention of Antalya airport distance, Side old town distance, nearby attractions, all-inclusive concept, or meal plan** — all table-stakes for a Turkish Riviera hotel site.

## 4. Brand / identity issues

- "Mira Palace" vs "Side Mira Palace" used interchangeably — pick one canonical name.
- Three email domains to reconcile to one.
- "Calimera Side Mira Palace" on career page implies a chain affiliation (Calimera is a Club Med / FTI brand). Needs clarification: is the hotel actually branded as a Calimera property, or is this leftover text from a template?

## 5. Technical observations

- Reservation flow is a third-party POST to what looks like an external reservation system (hidden form fields reveal an `otelId=597`, `kurumId=32`, token `caglatur`). Probably a Turkish reservation engine called *Caglatur*.
- No Lighthouse run yet (defer to after rebuild).
- Page source returned 0 meta description hints visible in extracted text (needs deeper DOM pass if we care about the old site's SEO signals; we don't — we're rebuilding).

## 6. Content gaps the rebuild must fill

A well-structured Turkish Riviera hotel site should have, at minimum:

- **Home** — hero, 3-sentence positioning, 3-tile highlight (rooms / dining / location), social proof, clear CTA
- **Rooms** — a proper index plus a detail page per room type (Standard, Deluxe, and anything else that exists — need to ask the owner)
- **All-Inclusive Concept** — what's included: meals, drinks, snacks, late-night, timings, minibar, à la carte
- **Dining** — main restaurant, snack bar, lobby bar, pool bar — hours, cuisine, dress code
- **Pools & Beach** — pool count and specs, beach access (600 m stated), sunbeds, kids' pool
- **Spa & Wellness** — treatments, Turkish bath, sauna, fitness
- **Entertainment & Activities** — daytime animation, evening shows, live music, kids' club
- **Location & Transfers** — map, drive times (Antalya AYT, Side old town, Manavgat), airport transfer options
- **Gallery** — with categories (rooms, dining, pools, beach, spa) and captions
- **FAQ** — check-in/out, pets, smoking, kids age tiers, payment
- **Offers** — current season promotions (currently advertising 2024!)
- **Contact / Enquiry** — with a proper enquiry form (not a hidden-field POST)
- **Career** — proper job listing, file upload
- **Legal** — Privacy, Cookies, Hotel Policies — in the language of the site and correctly encoded
- **Structured data** — Hotel, LocalBusiness, Room markup for rich results
- **Multi-language** — TR, EN, DE, RU served consistently with `hreflang`

## 7. Owner decisions needed before the rebuild starts

1. **Canonical brand name:** "Mira Palace" or "Side Mira Palace"?
2. **Canonical email:** `info@sidemirapalace.com` (matches domain), `info@mirapalace.com`, or something else?
3. **Calimera affiliation:** real chain partnership, or dead template text to remove?
4. **Actual room types and counts:** site says 34 rooms total and shows Standard + Deluxe only — are those the only types? Any Family, Suite, Connecting?
5. **Concept:** All-Inclusive, Half-Board, Ultra-All, or room-only?
6. **Distances:** confirm 600 m to beach; add AYT airport km; add Side old town km.
7. **Languages to ship first:** EN only for v1? Then TR, then DE+RU?
8. **Reservation:** keep existing Caglatur engine, or swap for a different engine later (we stub for now)?
9. **Assets:** does the owner have a photo library we can use (rooms, pools, dining, spa), or do we need to plan for photography?

---

*This file is v1 — superseding versions move to `Planning/archive/` per §6.1 of the working agreement.*
