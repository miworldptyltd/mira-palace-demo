"""Shared rendering helpers used by every page module."""
from __future__ import annotations
import json, pathlib
from textwrap import dedent

# Resolve the on-disk site/ folder once so the asset scanners can find files.
_SITE_DIR = pathlib.Path(__file__).resolve().parent.parent / "site"

SITE_META = {
    "brand": "Mira Palace",
    "brand_full": "Mira Palace — Side, Antalya",
    "tagline": "A boutique Turkish Riviera escape",
    "phone_display": "+90 534 898 84 05",
    "phone_tel": "+905348988405",
    "email": "info@sidemirapalace.com",  # mocked canonical — owner to confirm
    "address_line1": "Evrenseki Mahallesi, Kömürcüler Küme Evleri No:96",
    "address_line2": "Manavgat / Antalya, Türkiye",
    "google_maps": "https://maps.app.goo.gl/psUsJCW22broH4nQ8",
    "whatsapp": "https://wa.me/905348988405",
    "base_url": "https://mi-world.github.io/mira-palace-demo",  # placeholder; update when repo created
    # Mi World owns the source tree, design, copy and assets of this
    # demonstration site. Mira Palace is the eventual customer — until they
    # accept and acquire the work, the copyright stays with Mi World.
    "copyright_short_en": "© 2026 Mi World Pty Ltd / Mi World Software Technology Limited Company · All rights reserved",
    "copyright_short_tr": "© 2026 Mi World Pty Ltd / Mİ WORLD YAZILIM TEKNOLOJİ LİMİTED ŞİRKETİ · Tüm hakları saklıdır",
    "copyright_long_en": "All content on this demonstration site is © Mi World — held jointly by Mi World Pty Ltd (Australia) and Mi World Software Technology Limited Company (Türkiye) — and is provided for preview purposes only. No part of the source tree, design, copy, or imagery may be copied, re-hosted, or re-used without written permission.",
    "copyright_long_tr": "Bu tanıtım sitesindeki tüm içerikler © Mi World'e aittir — Mi World Pty Ltd (Avustralya) ve Mİ WORLD YAZILIM TEKNOLOJİ LİMİTED ŞİRKETİ (Türkiye) ortak hak sahibidir — ve yalnızca önizleme amacıyla sağlanmıştır. Kaynak kod, tasarım, metin veya görsellerin hiçbir parçası, yazılı izin olmadan kopyalanamaz, yeniden yayınlanamaz veya yeniden kullanılamaz.",
    "permissions_email": "info@miworld.tech",
    "permissions_label_en": "Permissions & queries",
    "permissions_label_tr": "İzin ve sorular",
    "og_image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1600&q=80",
}

# ---- Shared fragments ---------------------------------------------------

HEAD = """<!doctype html>
<html lang="en" class="scroll-smooth">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{description}" />
<meta name="robots" content="noindex,nofollow" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{description}" />
<meta property="og:type" content="website" />
<meta property="og:image" content="{og_image}" />
<meta property="og:url" content="{canonical}" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="icon" type="image/svg+xml" href="{root}assets/img/favicon.svg" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.2.3/css/flag-icons.min.css" />
<script src="https://cdn.tailwindcss.com?plugins=forms,typography"></script>
<script>
tailwind.config = {{
  theme: {{
    extend: {{
      colors: {{
        mira: {{ 50:'#F2F6F7',100:'#E0EBEE',200:'#BDD4DA',300:'#90B5BF',400:'#628F9C',500:'#456E7B',600:'#345661',700:'#274551',800:'#1D3742',900:'#132630' }},
        sand: {{ 50:'#FBF8F1',100:'#F4EDDD',200:'#E8D4A0',300:'#D4B971',400:'#C9A961',500:'#B68F3F',600:'#8E6D2F' }},
        ink:  '#111827',
      }},
      fontFamily: {{
        display: ['\"Cormorant Garamond\"','serif'],
        body:    ['Inter','sans-serif'],
      }},
      boxShadow: {{
        lux: '0 20px 60px -20px rgba(19,38,48,.35)',
      }},
    }}
  }}
}};
</script>
<script>
  // Project root path (e.g. "" for a domain-root site, "../" or "../../"
  // for nested pages). Python's render_page() computes the depth and
  // writes the right value here, so site.js never has to guess. Required
  // because GitHub Pages hosts at /mira-palace-demo/ rather than /.
  window.MIRA_ROOT = "{root}";
</script>
<link rel="stylesheet" href="{root}assets/css/site.css?v=11" />
</head>
<body class="font-body text-ink bg-sand-50 antialiased" data-root="{root}">
<a href="#main" class="sr-only focus:not-sr-only focus:absolute focus:top-3 focus:left-3 bg-mira-800 text-white px-3 py-2 rounded">Skip to content</a>
"""


def nav(active: str, root: str) -> str:
    # Each item: (key, label, href, sub_items_or_None). sub_items is a list of
    # (label, relative-href) tuples; if present the item renders as a dropdown.
    items = [
        ("home",       "Home",          "index.html",       None),
        ("about",      "About",         "about.html",       None),
        ("rooms",      "Suites",        "rooms/",           [
            ("All suites",         "rooms/"),
            ("Standard Suite",     "rooms/standard.html"),
            ("Deluxe Suite",       "rooms/deluxe.html"),
            ("Family Suite",       "rooms/family.html"),
            ("King Suite",         "rooms/king.html"),
        ]),
        ("concept",    "All-Inclusive", "concept.html",     None),
        ("dining",     "Dining",        "dining/",          [
            ("Dining overview",    "dining/"),
            ("Our dining rooms",   "dining/#dining-rooms"),
            ("Sample menu",        "dining/#sample-menu"),
            ("Main restaurant",    "dining/main-restaurant.html"),
            ("Pool restaurant",    "dining/pool-bar.html"),
            ("Lobby & Orchard bars", "dining/lobby-bar.html"),
        ]),
        ("pools",      "Pools",         "pools-beach.html", None),
        ("spa",        "Spa",           "spa.html",         [
            ("Spa & wellness",     "spa.html"),
            ("Treatments & pricing", "spa-treatments.html"),
        ]),
        ("activities", "Activities",    "activities.html",  None),
        ("location",   "Location",      "location.html",    None),
        ("gallery",    "Gallery",       "gallery.html",     None),
        ("offers",     "Offers",        "offers.html",      None),
        ("contact",    "Contact",       "contact.html",     None),
    ]

    def _link_classes(key: str) -> str:
        is_active = "text-sand-300 after:scale-x-100" if active == key else "text-white/85 hover:text-sand-200"
        return ("relative py-2 text-[13px] font-medium tracking-wide transition whitespace-nowrap "
                "after:absolute after:left-0 after:-bottom-0.5 after:h-0.5 after:w-full after:origin-left "
                "after:scale-x-0 after:bg-sand-300 after:transition-transform hover:after:scale-x-100 ") + is_active

    links = []
    for key, label, href, subs in items:
        if subs:
            sub_html = "".join(
                f'<a href="{root}{sh}" class="block px-4 py-2 text-sm text-mira-800 hover:bg-sand-100 hover:text-mira-900 whitespace-nowrap">{slabel}</a>'
                for slabel, sh in subs
            )
            chevron = '<svg class="w-3 h-3 opacity-70" viewBox="0 0 12 12" fill="currentColor" aria-hidden="true"><path d="M3 5l3 3 3-3z"/></svg>'
            links.append(
                f'<div class="nav-dd relative" data-open="false">'
                f'  <a href="{root}{href}" class="nav-dd-trigger inline-flex items-center gap-1 {_link_classes(key)}">{label} {chevron}</a>'
                f'  <div class="nav-dd-menu absolute top-full left-0 mt-2 min-w-[210px] bg-white rounded-md shadow-lux border border-mira-200 py-2">'
                f'    {sub_html}'
                f'  </div>'
                f'</div>'
            )
        else:
            links.append(f'<a href="{root}{href}" class="{_link_classes(key)}">{label}</a>')

    # Mobile menu — flatten the dropdowns into nested groups for tap navigation.
    mobile_links = []
    for key, label, href, subs in items:
        ac = "bg-mira-900 text-sand-200" if active == key else ""
        if subs:
            sub_mobile = "".join(
                f'<a href="{root}{sh}" class="block pl-8 pr-4 py-2 text-xs text-white/70 hover:bg-mira-800 hover:text-white">{slabel}</a>'
                for slabel, sh in subs
            )
            mobile_links.append(
                f'<a href="{root}{href}" class="block px-4 py-3 text-sm font-medium text-white/90 hover:bg-mira-800 {ac}">{label}</a>'
                f'{sub_mobile}'
            )
        else:
            mobile_links.append(
                f'<a href="{root}{href}" class="block px-4 py-3 text-sm font-medium text-white/90 hover:bg-mira-800 {ac}">{label}</a>'
            )
    return dedent(f"""
    <header id="siteheader" class="fixed top-0 inset-x-0 z-40 transition-all">
      <!-- Thin Mi World copyright strip — language-switched by the EN/TR flag.
           Two spans rendered; one is hidden via the .lang-hidden helper. -->
      <div class="bg-[#0a1820] text-white/70 text-[10px] tracking-widest">
        <div class="max-w-7xl mx-auto px-5 lg:px-8 py-1.5 flex items-center justify-between gap-3 whitespace-nowrap overflow-x-auto">
          <span class="font-medium">
            <span class="lang-text" data-lang="en">{SITE_META['copyright_short_en']}</span>
            <span class="lang-text lang-hidden" data-lang="tr">{SITE_META['copyright_short_tr']}</span>
          </span>
          <span class="hidden sm:inline text-sand-300/70 uppercase">Preview · Demo</span>
        </div>
      </div>
      <div class="bg-mira-900/80 backdrop-blur supports-[backdrop-filter]:bg-mira-900/70 text-white border-b border-white/5">
        <div class="max-w-7xl mx-auto px-5 lg:px-8 flex items-center justify-between gap-4 h-16 xl:h-[72px]">
          <a href="{root}index.html" class="flex items-center gap-2 shrink-0">
            <span class="inline-block w-9 h-9 rounded-full bg-sand-300 text-mira-900 grid place-items-center font-display font-bold text-xl">M</span>
            <span class="font-display text-xl tracking-wide whitespace-nowrap">Mira Palace</span>
          </a>
          <nav class="hidden xl:flex items-center gap-x-5 flex-1 justify-end" aria-label="Primary">
            {''.join(links)}
          </nav>
          <div class="flex items-center gap-3 shrink-0 xl:ml-6">
            <div class="hidden md:flex items-center gap-1.5 mr-1" aria-label="Language">
              <button class="nav-flag rounded overflow-hidden ring-1 ring-white/20 hover:ring-white/60 transition" data-lang="en" aria-label="English" data-active="true"><span class="fi fi-gb block" style="width:24px;height:18px;"></span></button>
              <button class="nav-flag rounded overflow-hidden ring-1 ring-white/20 hover:ring-white/60 transition" data-lang="tr" aria-label="Türkçe"><span class="fi fi-tr block" style="width:24px;height:18px;"></span></button>
              <button class="nav-flag rounded overflow-hidden ring-1 ring-white/20 hover:ring-white/60 transition" data-lang="de" aria-label="Deutsch"><span class="fi fi-de block" style="width:24px;height:18px;"></span></button>
              <button class="nav-flag rounded overflow-hidden ring-1 ring-white/20 hover:ring-white/60 transition" data-lang="ru" aria-label="Русский"><span class="fi fi-ru block" style="width:24px;height:18px;"></span></button>
            </div>
            <a href="{root}book.html" class="hidden sm:inline-flex items-center px-4 py-2 bg-sand-300 text-mira-900 rounded-full font-medium text-sm hover:bg-sand-200 transition whitespace-nowrap">Book</a>
            <button id="mnu-toggle" class="xl:hidden p-2 -mr-2" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">
              <svg viewBox="0 0 24 24" fill="none" class="w-6 h-6"><path stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M4 7h16M4 12h16M4 17h16"/></svg>
            </button>
          </div>
        </div>
        <div id="mobile-menu" class="xl:hidden hidden border-t border-white/5 max-h-[80vh] overflow-y-auto">
          {''.join(mobile_links)}
          <!-- Language flags inside the hamburger menu (phone users) -->
          <div class="px-4 py-3 border-t border-white/10 flex items-center gap-3 bg-mira-900/40">
            <span class="text-[10px] uppercase tracking-widest text-white/60">Language</span>
            <button class="nav-flag rounded overflow-hidden ring-1 ring-white/20 hover:ring-white/60 transition" data-lang="en" aria-label="English" data-active="true"><span class="fi fi-gb block" style="width:28px;height:20px;"></span></button>
            <button class="nav-flag rounded overflow-hidden ring-1 ring-white/20 hover:ring-white/60 transition" data-lang="tr" aria-label="Türkçe"><span class="fi fi-tr block" style="width:28px;height:20px;"></span></button>
            <button class="nav-flag rounded overflow-hidden ring-1 ring-white/20 hover:ring-white/60 transition" data-lang="de" aria-label="Deutsch"><span class="fi fi-de block" style="width:28px;height:20px;"></span></button>
            <button class="nav-flag rounded overflow-hidden ring-1 ring-white/20 hover:ring-white/60 transition" data-lang="ru" aria-label="Русский"><span class="fi fi-ru block" style="width:28px;height:20px;"></span></button>
          </div>
          <a href="{root}book.html" class="block px-4 py-4 text-center bg-sand-300 text-mira-900 font-semibold">Book your stay</a>
        </div>
      </div>
    </header>
    """)


def footer(root: str) -> str:
    m = SITE_META
    return dedent(f"""
    <footer class="bg-mira-900 text-white/80 mt-24">
      <div class="max-w-7xl mx-auto px-5 lg:px-8 py-14 grid grid-cols-1 md:grid-cols-4 gap-10">
        <div class="md:col-span-1">
          <div class="flex items-center gap-2">
            <span class="inline-block w-9 h-9 rounded-full bg-sand-300 text-mira-900 grid place-items-center font-display font-bold text-xl">M</span>
            <span class="font-display text-2xl text-white">Mira Palace</span>
          </div>
          <p class="mt-4 text-sm leading-relaxed">{m['tagline']}. Thirty-four suites, 600 metres from the Mediterranean, on the Turkish Riviera.</p>
        </div>
        <div>
          <h4 class="font-display text-lg text-white">Explore</h4>
          <ul class="mt-4 space-y-2 text-sm">
            <li><a href="{root}rooms/" class="hover:text-sand-300">Rooms &amp; Suites</a></li>
            <li><a href="{root}concept.html" class="hover:text-sand-300">All-Inclusive concept</a></li>
            <li><a href="{root}dining/" class="hover:text-sand-300">Dining</a></li>
            <li><a href="{root}spa.html" class="hover:text-sand-300">Spa &amp; Wellness</a></li>
            <li><a href="{root}offers.html" class="hover:text-sand-300">Offers</a></li>
            <li><a href="{root}gallery.html" class="hover:text-sand-300">Gallery</a></li>
          </ul>
        </div>
        <div>
          <h4 class="font-display text-lg text-white">Contact</h4>
          <address class="mt-4 not-italic text-sm space-y-2">
            <div>{m['address_line1']}<br/>{m['address_line2']}</div>
            <div><a class="hover:text-sand-300" href="tel:{m['phone_tel']}">{m['phone_display']}</a></div>
            <div><a class="hover:text-sand-300" href="mailto:{m['email']}">{m['email']}</a></div>
            <div><a class="hover:text-sand-300" href="{m['whatsapp']}" rel="noopener">WhatsApp</a></div>
          </address>
        </div>
        <div>
          <h4 class="font-display text-lg text-white">Newsletter</h4>
          <p class="mt-4 text-sm">Seasonal offers and stories from the Turkish Riviera. We&apos;ll email you now and then — never more than once a month.</p>
          <form class="mt-4 flex gap-2" onsubmit="event.preventDefault(); this.querySelector('button').innerText='Thanks!';">
            <input type="email" required placeholder="you@example.com" class="flex-1 bg-mira-800 border border-white/10 rounded px-3 py-2 text-sm text-white placeholder:text-white/40 focus:border-sand-300 focus:ring-0" />
            <button class="bg-sand-300 text-mira-900 rounded px-4 py-2 text-sm font-medium hover:bg-sand-200">Sign up</button>
          </form>
          <p class="mt-3 text-[11px] text-white/50">By subscribing you consent to receive marketing emails. Unsubscribe any time. See our <a href="{root}legal/privacy.html" class="underline">Privacy Notice</a>.</p>
        </div>
      </div>
      <div class="border-t border-white/10">
        <div class="max-w-7xl mx-auto px-5 lg:px-8 py-6 flex flex-col md:flex-row items-start md:items-center justify-between gap-4 text-xs text-white/60">
          <div class="max-w-2xl">
            <div class="font-medium text-white/80">
              <span class="lang-text" data-lang="en">{m['copyright_short_en']}</span>
              <span class="lang-text lang-hidden" data-lang="tr">{m['copyright_short_tr']}</span>
            </div>
            <div class="mt-2 text-white/55 text-[11px] leading-snug">
              <span class="lang-text" data-lang="en">{m['copyright_long_en']}</span>
              <span class="lang-text lang-hidden" data-lang="tr">{m['copyright_long_tr']}</span>
            </div>
            <div class="mt-2 text-white/60 text-[11px] leading-snug">
              <span class="lang-text" data-lang="en">{m['permissions_label_en']}:</span>
              <span class="lang-text lang-hidden" data-lang="tr">{m['permissions_label_tr']}:</span>
              <a href="mailto:{m['permissions_email']}" class="hover:text-white underline-offset-2 hover:underline">{m['permissions_email']}</a>
            </div>
          </div>
          <div class="flex gap-5 shrink-0">
            <a href="{root}legal/privacy.html" class="hover:text-white">Privacy</a>
            <a href="{root}legal/cookies.html" class="hover:text-white">Cookies</a>
            <a href="{root}legal/hotel-policies.html" class="hover:text-white">Hotel Policies</a>
            <a href="{root}career.html" class="hover:text-white">Careers</a>
          </div>
        </div>
      </div>
      <div id="demo-banner" class="bg-red-700 text-white text-center text-xs py-2 px-4 font-semibold tracking-wide uppercase">
        <span class="lang-text" data-lang="en">DEMONSTRATION SITE — preview build for review. Content is illustrative until finalised with the hotel.</span>
        <span class="lang-text lang-hidden" data-lang="tr">TANITIM SİTESİ — inceleme amaçlı önizleme sürümü. İçerikler, otelle birlikte nihai hale getirilinceye kadar yalnızca örnek niteliğindedir.</span>
      </div>
    </footer>

    <a href="{m['whatsapp']}" rel="noopener" aria-label="WhatsApp" class="fixed right-5 z-30 bg-[#25D366] text-white w-12 h-12 grid place-items-center rounded-full shadow-lg hover:scale-105 transition whatsapp-bottom-safe">
      <svg viewBox="0 0 24 24" class="w-6 h-6" fill="currentColor" aria-hidden="true"><path d="M20.52 3.48A11.9 11.9 0 0 0 12 0C5.37 0 0 5.37 0 12a11.93 11.93 0 0 0 1.64 6L0 24l6.19-1.62A11.94 11.94 0 0 0 12 24c6.63 0 12-5.37 12-12 0-3.2-1.25-6.2-3.48-8.52Zm-8.52 18a9.9 9.9 0 0 1-5.05-1.38l-.36-.22-3.67.96.98-3.58-.23-.37A9.94 9.94 0 1 1 22 12c0 5.5-4.48 9.98-10 9.98Zm5.47-7.46c-.3-.15-1.77-.87-2.04-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.25-.46-2.39-1.47-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.58c-.2 0-.52.07-.8.37-.27.3-1.05 1.02-1.05 2.48s1.08 2.88 1.23 3.08c.15.2 2.13 3.25 5.15 4.56.72.31 1.28.5 1.72.64.72.23 1.38.2 1.9.12.58-.09 1.77-.72 2.02-1.42.25-.7.25-1.3.17-1.42-.07-.12-.27-.2-.57-.35Z"/></svg>
    </a>

    <!-- Site-wide music cluster: prev / play-pause / next. The "Music on/off"
         text label is hidden on phones (< sm) so the cluster stays compact.
         On phones, the cluster sits ABOVE the WhatsApp bubble; on tablet+
         it sits to its left as before. -->
    <div id="music-cluster" class="fixed right-5 sm:right-20 z-30 inline-flex items-stretch bg-mira-900/90 backdrop-blur text-white text-xs font-medium rounded-full border border-white/15 shadow-lg overflow-hidden music-cluster-pos">
      <button id="music-prev" aria-label="Previous track" class="px-2.5 sm:px-3 py-2 hover:bg-mira-800 transition">&#171;</button>
      <span class="w-px bg-white/15" aria-hidden="true"></span>
      <button id="music-toggle" aria-label="Toggle music" class="inline-flex items-center gap-2 px-2.5 sm:px-3 py-2 hover:bg-mira-800 transition">
        <span aria-hidden="true">♪</span><span id="music-label" class="hidden sm:inline">Music off</span>
      </button>
      <span class="w-px bg-white/15" aria-hidden="true"></span>
      <button id="music-next" aria-label="Next track" class="px-2.5 sm:px-3 py-2 hover:bg-mira-800 transition">&#187;</button>
    </div>
    <audio id="ambient-audio" loop preload="auto"></audio>

    <!-- Hero-video cluster (home page only; site.js hides on others).
         Label text hidden on phones. -->
    <div id="video-cluster" class="fixed left-12 sm:left-16 z-30 inline-flex items-stretch bg-mira-900/90 backdrop-blur text-white text-xs font-medium rounded-full border border-white/15 shadow-lg overflow-hidden floating-bottom-safe">
      <button id="video-prev" aria-label="Previous video" class="px-2.5 sm:px-3 py-2 hover:bg-mira-800 transition">&#171;</button>
      <span class="w-px bg-white/15" aria-hidden="true"></span>
      <button id="video-toggle" aria-label="Cycle hero video" class="inline-flex items-center gap-2 px-2.5 sm:px-3 py-2 hover:bg-mira-800 transition">
        <span aria-hidden="true">▶</span><span id="video-label" class="hidden sm:inline">Video</span>
      </button>
      <span class="w-px bg-white/15" aria-hidden="true"></span>
      <button id="video-next" aria-label="Next video" class="px-2.5 sm:px-3 py-2 hover:bg-mira-800 transition">&#187;</button>
    </div>

    {customiser_panel(root)}
    <script src="{root}assets/js/media-manifest.js?v=17" defer></script>
    <script src="{root}assets/js/site.js?v=17" defer></script>
    </body></html>
    """)


def customiser_panel(root: str) -> str:
    # Build the video buttons from whatever was discovered on disk.
    vid_btns = []
    for key, label, _path in VIDEO_OPTIONS:
        active = ' data-active="true"' if key == DEFAULT_VIDEO_KEY else ''
        star = ' ★' if key == DEFAULT_VIDEO_KEY else ''
        vid_btns.append(
            f'<button data-video="{key}" class="vid-btn text-left p-2 rounded border border-mira-200 hover:border-mira-700 text-xs font-medium"{active}>{label}{star}</button>'
        )
    mus_btns = []
    for key, label, _path in MUSIC_OPTIONS:
        active = ' data-active="true"' if key == DEFAULT_MUSIC_KEY else ''
        star = ' ★' if key == DEFAULT_MUSIC_KEY else ''
        mus_btns.append(
            f'<button data-music="{key}" class="mus-btn text-left p-2 rounded border border-mira-200 hover:border-mira-700 text-xs font-medium"{active}>{label}{star}</button>'
        )
    vid_html = "\n            ".join(vid_btns)
    mus_html = "\n            ".join(mus_btns)
    n_videos = sum(1 for k, _, _ in VIDEO_OPTIONS if k != "none")
    n_tracks = sum(1 for k, _, _ in MUSIC_OPTIONS if k != "none")
    return dedent(f"""
    <div id="customiser" data-open="false" class="fixed left-0 top-1/2 -translate-y-1/2 z-30 flex items-stretch">
      <button id="cust-toggle" aria-label="Open customiser" aria-expanded="false" class="relative z-10 bg-mira-900 text-sand-300 rounded-r-md py-3 px-2 shadow-lux flex flex-col items-center gap-1 hover:bg-mira-800 transition" style="writing-mode:vertical-rl; transform:rotate(180deg);">
        <span class="text-[11px] tracking-widest uppercase">Customise</span>
      </button>
      <div id="cust-panel" class="bg-white border-r border-y border-mira-200 rounded-r-lg shadow-lux p-5 w-72 max-w-[85vw] -ml-px">
        <div>
          <div class="text-[11px] uppercase tracking-widest text-mira-600 font-semibold">Colour palette</div>
          <p class="mt-1 text-xs text-mira-600">Click a swatch — every page recolours instantly. Your choice is remembered for this browser.</p>
          <div class="mt-3 grid grid-cols-2 gap-2">
            <button data-theme="default" class="theme-swatch text-left p-3 rounded border border-mira-200 hover:border-mira-700 transition" data-active="true">
              <div class="flex gap-1"><span class="w-5 h-5 rounded-full" style="background:#1D3742"></span><span class="w-5 h-5 rounded-full" style="background:#D4B971"></span></div>
              <div class="mt-2 text-xs font-medium text-mira-900">Mediterranean</div>
              <div class="text-[10px] text-mira-600">Turquoise + sand</div>
            </button>
            <button data-theme="sunset" class="theme-swatch text-left p-3 rounded border border-mira-200 hover:border-mira-700 transition">
              <div class="flex gap-1"><span class="w-5 h-5 rounded-full" style="background:#5C2A2A"></span><span class="w-5 h-5 rounded-full" style="background:#E8A862"></span></div>
              <div class="mt-2 text-xs font-medium text-mira-900">Sunset Coast</div>
              <div class="text-[10px] text-mira-600">Rose + ochre</div>
            </button>
            <button data-theme="olive" class="theme-swatch text-left p-3 rounded border border-mira-200 hover:border-mira-700 transition">
              <div class="flex gap-1"><span class="w-5 h-5 rounded-full" style="background:#37432B"></span><span class="w-5 h-5 rounded-full" style="background:#D8C99B"></span></div>
              <div class="mt-2 text-xs font-medium text-mira-900">Olive Grove</div>
              <div class="text-[10px] text-mira-600">Deep olive + cream</div>
            </button>
            <button data-theme="midnight" class="theme-swatch text-left p-3 rounded border border-mira-200 hover:border-mira-700 transition">
              <div class="flex gap-1"><span class="w-5 h-5 rounded-full" style="background:#0F1B33"></span><span class="w-5 h-5 rounded-full" style="background:#C4A875"></span></div>
              <div class="mt-2 text-xs font-medium text-mira-900">Midnight Pearl</div>
              <div class="text-[10px] text-mira-600">Navy + champagne</div>
            </button>
            <button data-theme="onyx" class="theme-swatch text-left p-3 rounded border border-mira-200 hover:border-mira-700 transition col-span-2">
              <div class="flex gap-1"><span class="w-5 h-5 rounded-full" style="background:#000000"></span><span class="w-5 h-5 rounded-full" style="background:#D4B971"></span></div>
              <div class="mt-2 text-xs font-medium text-mira-900">Onyx (dark mode)</div>
              <div class="text-[10px] text-mira-600">Pure black + warm gold</div>
            </button>
          </div>
        </div>
        <div class="mt-5 pt-5 border-t border-mira-200">
          <div class="text-[11px] uppercase tracking-widest text-mira-600 font-semibold">Language</div>
          <p class="mt-1 text-xs text-mira-600">English is live; the others are stubbed for content sign-off.</p>
          <div class="mt-3 grid grid-cols-4 gap-2">
            <button data-lang="en" class="lang-btn text-center p-2 rounded border border-mira-200 hover:border-mira-700 text-xs font-medium" data-active="true">EN</button>
            <button data-lang="tr" class="lang-btn text-center p-2 rounded border border-mira-200 hover:border-mira-700 text-xs font-medium">TR</button>
            <button data-lang="de" class="lang-btn text-center p-2 rounded border border-mira-200 hover:border-mira-700 text-xs font-medium">DE</button>
            <button data-lang="ru" class="lang-btn text-center p-2 rounded border border-mira-200 hover:border-mira-700 text-xs font-medium">RU</button>
          </div>
          <div id="lang-msg" class="mt-3 text-[11px] text-mira-600 italic hidden"></div>
        </div>
        <div class="mt-5 pt-5 border-t border-mira-200">
          <div class="text-[11px] uppercase tracking-widest text-mira-600 font-semibold">Hero video (home page) <span class="text-mira-400 font-normal">{n_videos} loops</span></div>
          <p class="mt-1 text-xs text-mira-600">Pick which loop plays behind the headline. "No video" falls back to the still photo.</p>
          <div class="mt-3 grid grid-cols-2 gap-2">
            {vid_html}
          </div>
        </div>
        <div class="mt-5 pt-5 border-t border-mira-200">
          <div class="text-[11px] uppercase tracking-widest text-mira-600 font-semibold">Ambient music (site-wide) <span class="text-mira-400 font-normal">{n_tracks} tracks</span></div>
          <p class="mt-1 text-xs text-mira-600">Pick a track, then use the ♪ button bottom-right to play / pause. Plays on every page.</p>
          <div class="mt-3 grid grid-cols-2 gap-2">
            {mus_html}
          </div>
          <p class="mt-2 text-[10px] text-mira-500 italic">★ marks the default. The hotel will swap these for licensed tracks before launch.</p>
        </div>
        <p class="mt-5 text-[10px] text-mira-500">DEMO — these controls won't ship in the live site. They're here so the hotel can review options before sign-off.</p>
      </div>
    </div>
    """)


def hero(img_url: str, kicker: str, heading: str, sub: str, primary_href: str = "", primary_label: str = "", height: str = "80vh") -> str:
    cta = ""
    if primary_href:
        cta = (f'<a href="{primary_href}" class="inline-flex items-center justify-center px-7 py-3 bg-sand-300 text-mira-900 '
               f'rounded-full font-medium tracking-wide hover:bg-sand-200 shadow-lux transition">{primary_label}</a>')
    return dedent(f"""
    <section class="relative hero-section" style="min-height:{height};">
      <div class="absolute inset-0 hero-overlay" style="background-image:url('{img_url}'); background-size:cover; background-position:center;"></div>
      <div class="relative max-w-5xl mx-auto px-5 lg:px-8 pt-40 pb-28 text-white flex flex-col justify-end min-h-[inherit]" style="min-height:{height};">
        <div class="max-w-3xl">
          <p class="uppercase tracking-[0.22em] text-sand-300 text-xs sm:text-sm font-semibold mb-4">{kicker}</p>
          <h1 class="font-display text-4xl sm:text-5xl md:text-6xl lg:text-7xl leading-[1.05]">{heading}</h1>
          <p class="mt-5 max-w-2xl text-base sm:text-lg text-white/90 leading-relaxed">{sub}</p>
          <div class="mt-8 flex flex-wrap gap-3">{cta}</div>
        </div>
      </div>
    </section>
    """)


def hero_slideshow(image_urls, kicker: str, heading: str, sub: str,
                   primary_href: str = "", primary_label: str = "",
                   height: str = "80vh", interval_ms: int = 7000) -> str:
    """Hero with auto-rotating slideshow + Ken-Burns slow zoom on each slide.
    Pass a list of image URLs; if only one is supplied it renders as a single
    Ken-Burns still (no rotation). Respects prefers-reduced-motion."""
    if not image_urls:
        return ""
    if isinstance(image_urls, str):
        image_urls = [image_urls]
    slides = ""
    for i, url in enumerate(image_urls):
        cls = "slide active" if i == 0 else "slide"
        slides += f'<div class="{cls}" style="background-image:url(\'{url}\')"></div>'
    multi = len(image_urls) > 1
    attrs = f'data-slideshow data-interval="{interval_ms}"' if multi else ""
    cta = ""
    if primary_href:
        cta = (f'<a href="{primary_href}" class="inline-flex items-center justify-center px-7 py-3 bg-sand-300 text-mira-900 '
               f'rounded-full font-medium tracking-wide hover:bg-sand-200 shadow-lux transition">{primary_label}</a>')
    return dedent(f"""
    <section class="relative hero-section" style="min-height:{height};">
      <div class="hero-slideshow" {attrs}>
        {slides}
      </div>
      <div class="absolute inset-0 hero-overlay pointer-events-none"></div>
      <div class="relative max-w-5xl mx-auto px-5 lg:px-8 pt-40 pb-28 text-white flex flex-col justify-end min-h-[inherit]" style="min-height:{height};">
        <div class="max-w-3xl">
          <p class="uppercase tracking-[0.22em] text-sand-300 text-xs sm:text-sm font-semibold mb-4">{kicker}</p>
          <h1 class="font-display text-4xl sm:text-5xl md:text-6xl lg:text-7xl leading-[1.05]">{heading}</h1>
          <p class="mt-5 max-w-2xl text-base sm:text-lg text-white/90 leading-relaxed">{sub}</p>
          <div class="mt-8 flex flex-wrap gap-3">{cta}</div>
        </div>
      </div>
    </section>
    """)


# ---- Media discovery -----------------------------------------------------
# Friendly labels for known files. Anything not listed is auto-humanised.

VIDEO_LABEL_OVERRIDES = {
    "pool":         "Resort pool",
    "pool_air":     "Pool from above",
    "coast":        "Mediterranean coast",
    "aerial":       "Drone view",
    "waves":        "Gentle waves",
    "lobby":        "Hotel interior",
    "room":         "Suite walkthrough",
    "spa":          "Spa & wellness",
    "hotel_drone":  "Hotel exterior (drone)",
    "kite_surf":    "Kite surfing",
    "sunset":       "Sunset on the coast",
}
MUSIC_LABEL_OVERRIDES = {
    "ambient":      "Ambient drift",
    "piano":        "Calm piano",
    "santur":       "Turkish santur",
    "ocean":        "Ocean tranquility",
    "spa":          "Spa serenity",
    "lounge":       "Lobby lounge",
    "hotel":        "Hotel ambience",
    "cave_explore": "Cave adventure",
    "zen":          "Zen meditation",
}

# Preferred default keys (used if present; else first available).
_PREFERRED_VIDEO_DEFAULT = "pool"
_PREFERRED_MUSIC_DEFAULT = "ambient"

# Allowed extensions (case-insensitive).
_VIDEO_EXTS = (".mp4", ".webm", ".mov", ".m4v")
_AUDIO_EXTS = (".mp3", ".ogg", ".wav", ".m4a", ".aac")


def _humanise(bare: str) -> str:
    """Turn 'pool_air' or 'Hotel-drone' into 'Pool Air' / 'Hotel Drone'."""
    cleaned = bare.replace("_", " ").replace("-", " ").strip()
    return " ".join(w.capitalize() for w in cleaned.split() if w)


def _detect_audio_ext(path: pathlib.Path) -> str:
    """Sniff the first bytes of a media file. Return the extension that matches
    the actual container — useful when a file has been mis-named (e.g. .mp3
    extension but the bytes say it's Ogg Vorbis)."""
    try:
        with path.open("rb") as fh:
            head = fh.read(12)
    except OSError:
        return path.suffix.lstrip(".").lower()
    if head[:4] == b"OggS":
        return "ogg"
    if head[:3] == b"ID3":
        return "mp3"
    if head[:4] == b"RIFF" and head[8:12] == b"WAVE":
        return "wav"
    if head[:4] == b"fLaC":
        return "flac"
    if len(head) > 1 and head[0] == 0xFF and (head[1] & 0xE0) == 0xE0:
        return "mp3"  # MPEG frame sync
    return path.suffix.lstrip(".").lower()


def _correct_extension_if_needed(path: pathlib.Path) -> pathlib.Path:
    """If a file's extension lies about its content, write a sibling next to it
    with the correct extension and return THAT path. The original stays where
    the user put it (we never rewrite their files); the manifest just points
    at the corrected sibling so browsers pick the right codec from the URL.
    Idempotent — re-running won't grow the folder."""
    cur_ext = path.suffix.lstrip(".").lower()
    real_ext = _detect_audio_ext(path)
    if real_ext == cur_ext:
        return path
    sibling = path.with_suffix(f".{real_ext}")
    if not sibling.exists() or sibling.stat().st_size != path.stat().st_size:
        sibling.write_bytes(path.read_bytes())
    return sibling


def _scan_media(folder_name: str, prefix: str, exts: tuple, none_label: str,
                overrides: dict, fix_extensions: bool = False) -> list[tuple[str, str, str]]:
    """Scan site/assets/<folder_name>/ for files; return [(key, label, rel_path), ...].
    First entry is always the 'none' option so the picker can offer 'off'.
    If fix_extensions=True, mis-named files (e.g. Ogg-with-.mp3-extension) get
    a correctly-named sibling and the manifest points at the sibling."""
    options: list[tuple[str, str, str]] = [("none", none_label, "")]
    folder = _SITE_DIR / "assets" / folder_name
    if not folder.exists():
        return options
    seen_keys: set[str] = {"none"}
    seen_paths: set[str] = set()
    files = sorted([p for p in folder.iterdir() if p.is_file()], key=lambda p: p.name.lower())
    # First pass: optionally write corrected-extension siblings.
    if fix_extensions:
        for f in list(files):
            if f.suffix.lower() in exts:
                _correct_extension_if_needed(f)
        # Re-list so we pick up any siblings just written.
        files = sorted([p for p in folder.iterdir() if p.is_file()], key=lambda p: p.name.lower())
    # Second pass: build options. Skip a file if its content-correct sibling
    # also exists in the same folder (avoid duplicating tracks in the picker).
    by_stem: dict[str, list[pathlib.Path]] = {}
    for f in files:
        if f.suffix.lower() not in exts:
            continue
        by_stem.setdefault(f.stem, []).append(f)
    for stem, group in by_stem.items():
        # Prefer the file whose extension matches its content.
        chosen = group[0]
        if fix_extensions and len(group) > 1:
            for cand in group:
                if cand.suffix.lstrip(".").lower() == _detect_audio_ext(cand):
                    chosen = cand
                    break
        files_to_use = [chosen] if (fix_extensions and len(group) > 1) else group
        for f in files_to_use:
            if str(f) in seen_paths:
                continue
            seen_paths.add(str(f))
            bare = f.stem
            if bare.startswith(prefix):
                bare = bare[len(prefix):]
            key = bare.lower().replace("-", "_")
            if key in seen_keys:
                n = 2
                while f"{key}_{n}" in seen_keys:
                    n += 1
                key = f"{key}_{n}"
            seen_keys.add(key)
            label = overrides.get(key) or _humanise(bare)
            rel = f"assets/{folder_name}/{f.name}"
            options.append((key, label, rel))
    # Sort options so the 'none' entry stays first, then alphabetical by label.
    head_opt = options[0]
    body_opts = sorted(options[1:], key=lambda t: t[1].lower())
    return [head_opt] + body_opts


def _pick_default(options: list[tuple[str, str, str]], preferred: str) -> str:
    keys = [k for k, _, _ in options if k != "none"]
    if preferred in keys:
        return preferred
    return keys[0] if keys else "none"


VIDEO_OPTIONS: list[tuple[str, str, str]] = _scan_media(
    "video", "hero-", _VIDEO_EXTS, "No video (photo hero)", VIDEO_LABEL_OVERRIDES
)
# fix_extensions=True so any track-X.mp3 that is actually Ogg Vorbis gets a
# corrected-extension sibling (track-X.ogg) — browsers need the URL/MIME to
# match the codec or they refuse to play.
MUSIC_OPTIONS: list[tuple[str, str, str]] = _scan_media(
    "audio", "track-", _AUDIO_EXTS, "No music", MUSIC_LABEL_OVERRIDES,
    fix_extensions=True,
)
DEFAULT_VIDEO_KEY = _pick_default(VIDEO_OPTIONS, _PREFERRED_VIDEO_DEFAULT)
DEFAULT_MUSIC_KEY = _pick_default(MUSIC_OPTIONS, _PREFERRED_MUSIC_DEFAULT)


def write_media_manifest(out_path: pathlib.Path) -> None:
    """Emit assets/js/media-manifest.js — defines window.MIRA_VIDEOS / MIRA_TRACKS
    so the browser knows about every file the build saw on disk. site.js reads this."""
    videos = {k: p for k, _, p in VIDEO_OPTIONS}
    tracks = {k: p for k, _, p in MUSIC_OPTIONS}
    video_labels = {k: lbl for k, lbl, _ in VIDEO_OPTIONS}
    track_labels = {k: lbl for k, lbl, _ in MUSIC_OPTIONS}
    js = (
        "// Auto-generated by scripts/build.py — do not edit by hand.\n"
        "// Lists every video and audio file discovered under site/assets/.\n"
        f"window.MIRA_VIDEOS = {json.dumps(videos, indent=2)};\n"
        f"window.MIRA_VIDEO_LABELS = {json.dumps(video_labels, indent=2)};\n"
        f"window.MIRA_TRACKS = {json.dumps(tracks, indent=2)};\n"
        f"window.MIRA_TRACK_LABELS = {json.dumps(track_labels, indent=2)};\n"
        f"window.MIRA_DEFAULT_VIDEO = {json.dumps(DEFAULT_VIDEO_KEY)};\n"
        f"window.MIRA_DEFAULT_TRACK = {json.dumps(DEFAULT_MUSIC_KEY)};\n"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(js, encoding="utf-8")


def hero_video(poster_url: str, kicker: str, heading: str, sub: str,
               primary_href: str = "", primary_label: str = "", height: str = "88vh", root: str = "") -> str:
    """Video-backed hero. Video autoplays muted (browser rule); music is opt-in via a toggle.
       Both video source and music source are swappable from the Customise panel — see site.js."""
    cta = ""
    if primary_href:
        cta = (f'<a href="{primary_href}" class="inline-flex items-center justify-center px-7 py-3 bg-sand-300 text-mira-900 '
               f'rounded-full font-medium tracking-wide hover:bg-sand-200 shadow-lux transition">{primary_label}</a>')
    # Default video path (for the <source> tag). The JS swaps this on load
    # from the user's stored choice if any.
    default_video_rel = next((p for k, _, p in VIDEO_OPTIONS if k == DEFAULT_VIDEO_KEY), "")
    default_video = f"{root}{default_video_rel}" if default_video_rel else ""
    return dedent(f"""
    <section class="relative hero-section overflow-hidden" style="min-height:{height};">
      <div class="absolute inset-0 bg-cover bg-center" style="background-image:url('{poster_url}');"></div>
      <video id="hero-video" class="absolute inset-0 w-full h-full object-cover" autoplay loop muted playsinline preload="auto" poster="{poster_url}" data-root="{root}">
        <source id="hero-video-source" src="{default_video}" type="video/mp4" />
      </video>
      <div class="absolute inset-0 hero-overlay pointer-events-none"></div>
      <div class="relative max-w-5xl mx-auto px-5 lg:px-8 pt-40 pb-28 text-white flex flex-col justify-end min-h-[inherit]" style="min-height:{height};">
        <div class="max-w-3xl">
          <p class="uppercase tracking-[0.22em] text-sand-300 text-xs sm:text-sm font-semibold mb-4">{kicker}</p>
          <h1 class="font-display text-4xl sm:text-5xl md:text-6xl lg:text-7xl leading-[1.05]">{heading}</h1>
          <p class="mt-5 max-w-2xl text-base sm:text-lg text-white/90 leading-relaxed">{sub}</p>
          <div class="mt-8 flex flex-wrap gap-3">{cta}</div>
        </div>
      </div>
    </section>
    """)


def render_page(page: dict) -> str:
    depth = page["path"].count("/")
    root = "../" * depth
    canonical = SITE_META["base_url"].rstrip("/") + "/" + page["path"]
    head = HEAD.format(
        title=page["title"],
        description=page["description"],
        og_image=SITE_META["og_image"],
        canonical=canonical,
        root=root,
    )
    body = page["body"](root) if callable(page["body"]) else page["body"]
    # Total fixed-header height = thin copyright strip (~26px) + main nav row.
    main_open = f'<main id="main" class="pt-[88px] xl:pt-[96px]">'
    return head + nav(page.get("active", ""), root) + main_open + body + "</main>" + footer(root)


# ---- Re-usable UI atoms -------------------------------------------------

def section(inner: str, bg: str = "bg-sand-50", pad: str = "py-20 lg:py-28", id: str = "") -> str:
    id_attr = f' id="{id}"' if id else ""
    # scroll-mt-24 leaves room for the fixed header when an in-page anchor jumps here.
    return f'<section{id_attr} class="{bg} {pad} scroll-mt-24"><div class="max-w-7xl mx-auto px-5 lg:px-8">{inner}</div></section>'


def eyebrow(text: str, color: str = "text-mira-600") -> str:
    return f'<p class="uppercase tracking-[0.22em] {color} text-xs font-semibold">{text}</p>'


def heading(text: str, level: int = 2, extra: str = "") -> str:
    size = {2: "text-3xl sm:text-4xl md:text-5xl", 3: "text-2xl sm:text-3xl", 4: "text-xl sm:text-2xl"}.get(level, "text-3xl")
    return f'<h{level} class="font-display {size} text-mira-900 leading-tight {extra}">{text}</h{level}>'


def lead(text: str) -> str:
    return f'<p class="mt-5 max-w-2xl text-lg text-mira-700 leading-relaxed">{text}</p>'


def card(img: str, title: str, body: str, href: str, cta: str = "Discover") -> str:
    return dedent(f"""
    <a href="{href}" class="group block bg-white rounded-lg overflow-hidden shadow-lux hover:-translate-y-1 transition will-change-transform">
      <div class="aspect-[4/3] bg-cover bg-center transition group-hover:scale-[1.04]" style="background-image:url('{img}')"></div>
      <div class="p-7">
        <h3 class="font-display text-2xl text-mira-900">{title}</h3>
        <p class="mt-3 text-sm text-mira-700 leading-relaxed">{body}</p>
        <span class="mt-5 inline-flex items-center gap-2 text-sm font-medium text-mira-700 group-hover:text-sand-500">
          {cta} <span class="transition group-hover:translate-x-1">→</span>
        </span>
      </div>
    </a>
    """)


def feature_strip(items: list[tuple[str, str]]) -> str:
    cells = "".join(
        f'<div class="flex-1 py-6 px-4 text-center border-r border-mira-200 last:border-r-0"><div class="font-display text-2xl md:text-3xl text-mira-800">{v}</div><div class="mt-1 text-[11px] uppercase tracking-widest text-mira-600">{k}</div></div>'
        for k, v in items
    )
    return f'<div class="bg-white rounded-md shadow-lux flex flex-wrap overflow-hidden">{cells}</div>'


def cta_band(heading_text: str, sub: str, href: str, label: str, img: str) -> str:
    return dedent(f"""
    <section class="relative">
      <div class="absolute inset-0 bg-cover bg-center" style="background-image:linear-gradient(180deg,rgba(19,38,48,.55),rgba(19,38,48,.75)),url('{img}')"></div>
      <div class="relative max-w-5xl mx-auto px-5 lg:px-8 py-24 text-center text-white">
        <h2 class="font-display text-3xl sm:text-4xl md:text-5xl">{heading_text}</h2>
        <p class="mt-5 max-w-2xl mx-auto text-white/90">{sub}</p>
        <a href="{href}" class="mt-8 inline-flex items-center px-7 py-3 bg-sand-300 text-mira-900 rounded-full font-medium hover:bg-sand-200 transition">{label}</a>
      </div>
    </section>
    """)


def quote_block(quote: str, name: str, role: str) -> str:
    return dedent(f"""
    <figure class="max-w-3xl mx-auto text-center">
      <svg class="w-10 h-10 mx-auto text-sand-400" fill="currentColor" viewBox="0 0 24 24"><path d="M7 7h4v4H7v4a4 4 0 0 0 4 4v2a6 6 0 0 1-6-6V7Zm10 0h4v4h-4v4a4 4 0 0 0 4 4v2a6 6 0 0 1-6-6V7Z"/></svg>
      <blockquote class="mt-5 font-display text-2xl md:text-3xl text-mira-900 leading-snug">{quote}</blockquote>
      <figcaption class="mt-5 text-sm text-mira-700"><span class="font-semibold">{name}</span> — {role}</figcaption>
    </figure>
    """)
