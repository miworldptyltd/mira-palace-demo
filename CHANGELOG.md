## [R009] - 2026-05-23

R009 feat: floating Book your stay button bottom-center on every page + desktop nav Book pill removed + bottom-padding on main so content does not hide behind the button + mobile + tablet polish

## [R008] - 2026-05-23

R008 feat: nav fit at 100 percent zoom (All-Inclusive removed, font shrunk) + flag green ring ON the flag (no rectangle) + Customise moved to right side + site-wide search icon with client-side index of every page

## [R007] - 2026-05-23

R007 feat: spa booking page (3 packages) + Activities silenced as Coming Soon + Release.ps1 safety guard (detects working-dir + untracked changes)

# Changelog

## [R006] - 2026-05-23

R006 feat: booking page rebuild - 4-suite tabs + 3-info cards + photo grid + expandable smart add-ons (Airport+flight, Otogar+bus line, Late checkout, Spa packages, Wine) + currency selector (TRY/EUR/USD) + multi-currency pricing + mobile responsive

## [R005] - 2026-05-23

R005 feat: white MP logo + tight green flag + midnight default + raised left-aligned hero + Specials card + Pools removed + mobile and tablet fit

## [R004] - 2026-05-21

R004 feat: Midnight theme default + real MP monogram logo + Our Rooms nav + raised hero + green-selected flag border

## [R003] - 2026-05-17

feat: mobile + tablet responsive polish - hide top strip, tighten hero, bigger tap targets, hide customiser on phone

## [R002] - 2026-05-15

feat: Suite rename + real Mira Palace photography + Ken-Burns/slideshow motion + payment-coming-soon notice + mobile polish

All notable changes to the Mira Palace demo website are recorded here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [0.1.0] — 2026-04-25

First publishable build. Sent to the hotel for owner review.

### Site content & structure
- 28 generated pages: home, about, rooms (4 sub-pages — Standard, Deluxe,
  Family, Junior Suite), all-inclusive concept, dining (overview + 3
  sub-pages — Mira main restaurant, Deniz pool restaurant, Lobby & Orchard
  bars), pools & beach, spa (overview + treatments & pricing), activities,
  location & transfers, gallery, offers, careers, contact, book, three
  legal pages, and 404.
- All pages share a fixed top header with bilingual copyright strip,
  navigation, language flags (EN / TR / DE / RU), and a Book CTA.

### Hero & ambient experience
- 8 hero-video loops cycle through the home page, picker bottom-left.
- 8 ambient-music tracks selectable from a customise panel and a
  bottom-right cluster (`«` · ♪ · `»`); music plays on every page.
- Music continues across page navigations and resumes from the saved
  playback position (sessionStorage + HTTP Range support in `dev_server.py`).
- Auto-fallback if a track fails to load: silently advances to the next.
- Cross-page label: shows the friendly track name for 2.5 s on each cycle,
  reverts to "Music on" / "Music off".

### Customise panel
- Slides in on hover (mouse) / tap (touch). Closes with a 220 ms grace
  period when leaving the panel.
- 5 colour themes: Mediterranean (default), Sunset Coast, Olive Grove,
  Midnight Pearl, Onyx (dark mode). Choice persists in localStorage.
- Live-discovered video and music option lists, populated from the build's
  scan of `site/assets/{video,audio}/`.
- Demo-controls only — wired to be hidden in production via a feature flag.

### Bilingual copyright (EN / TR)
- Top strip and footer copyright switch with the EN / TR flag.
- English: "© 2026 Mi World Pty Ltd / Mi World Software Technology Limited
  Company · All rights reserved".
- Turkish: "© 2026 Mi World Pty Ltd / Mİ WORLD YAZILIM TEKNOLOJİ LİMİTED
  ŞİRKETİ · Tüm hakları saklıdır".
- Long fine-print copyright also translated.
- Demonstration banner (red, full-width, bottom of every page) translates
  with the flag.

### Top-navigation dropdowns
- Rooms → All / Standard / Deluxe / Family / Junior Suite.
- Dining → Overview / Our dining rooms / Sample menu / Main restaurant /
  Pool restaurant / Lobby & Orchard bars (with anchor links to the relevant
  sections of the dining page).
- Spa → Spa & wellness / Treatments & pricing.
- Hover-with-grace behaviour (350 ms close timer); first-tap-opens / second-
  tap-navigates on touch devices.

### Build & deploy
- `scripts/build.py` renders every HTML page and writes a JS media manifest
  describing all videos and tracks discovered on disk.
- `scripts/dev_server.py` serves locally with sensible cache headers for
  HTML (no-store) vs media (24 h cache + Accept-Ranges). Implements HTTP
  Range requests so audio seek works the same locally as on GitHub Pages.
- Self-correcting media: any audio file with a wrong extension (e.g. an
  `.mp3` that's actually Ogg Vorbis) gets a corrected sibling written at
  build time, and the manifest references the correctly-named copy.
- `.github/workflows/deploy.yml` rebuilds and publishes on every push to
  `main`.

### PowerShell tooling
- `Run-Dev.ps1`, `Stop-Dev.ps1`, `Restart-Dev.ps1` — local dev loop.
- `Refresh-Media.ps1` — rescan asset folders, regenerate manifest, restart
  preview.
- `Audit-Clean.ps1` — one-shot pre-release housekeeping.
- `Init-Repo.ps1` — first-time GitHub repo + Pages setup.
- `Publish-Site.ps1` — routine: rebuild, commit, push.

### Privacy & security posture
- Every page declares `<meta name="robots" content="noindex,nofollow">`.
- `robots.txt` published as `Disallow: /` so well-behaved crawlers skip
  the site.
- URL is obscure (`<owner>.github.io/mira-palace-demo/`), shared only with
  the hotel directly.
- LICENSE is all-rights-reserved proprietary.

[0.1.0]: https://github.com/-/-/releases/tag/v0.1.0








