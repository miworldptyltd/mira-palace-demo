from common import hero, section
from textwrap import dedent

# Gallery — a mix of real Mira Palace photography (suites, spa, garden) and
# stock placeholders for categories we don't yet have photos for (dining,
# bar). Real photos use `assets/img/...` paths; the renderer prefixes
# {root} only on those, leaving full URLs untouched.
GALLERY = [
    # Suites — real Mira Palace photos
    ("Suites",  "assets/img/standard/standard-01.webp",  "Standard Suite"),
    ("Suites",  "assets/img/standard/standard-04.webp",  "Standard Suite — bed"),
    ("Suites",  "assets/img/deluxe/deluxe-01.webp",      "Deluxe Suite"),
    ("Suites",  "assets/img/deluxe/deluxe-04.webp",      "Deluxe Suite — sitting area"),
    ("Suites",  "assets/img/deluxe/deluxe-10.webp",      "Deluxe Suite — view"),
    ("Suites",  "assets/img/family/family-01.webp",      "Family Suite"),
    ("Suites",  "assets/img/king/king-01.webp",          "King Suite"),
    ("Suites",  "assets/img/king/king-04.webp",          "King Suite — bath"),
    ("Suites",  "assets/img/king/king-09.webp",          "King Suite — terrace"),
    # Spa — real Mira Palace photos
    ("Spa",     "assets/img/spa/spa-01.webp",            "Hammam chamber"),
    ("Spa",     "assets/img/spa/spa-03.webp",            "Marble göbek taşı"),
    ("Spa",     "assets/img/spa/spa-06.webp",            "Treatment room"),
    ("Spa",     "assets/img/spa/spa-08.webp",            "Relaxation lounge"),
    ("Spa",     "assets/img/spa/spa-11.webp",            "Spa entrance"),
    # Garden / outdoors — real
    ("Garden",  "assets/img/garden/garden-01.webp",      "The garden walkway"),
    ("Garden",  "assets/img/garden/garden-03.webp",      "Citrus orchard"),
    ("Garden",  "assets/img/garden/garden-05.webp",      "Pool deck"),
    ("Garden",  "assets/img/garden/garden-07.webp",      "Grounds at golden hour"),
    # Dining / Bar — placeholder until we have real photos
    ("Dining",  "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1200&q=80",  "Main restaurant at dinner"),
    ("Dining",  "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=1200&q=80",   "Plated starter"),
    ("Dining",  "https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=1200&q=80", "Breakfast buffet"),
    ("Bar",     "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&w=1200&q=80", "Lobby bar cocktail"),
    ("Bar",     "https://images.unsplash.com/photo-1470337458703-46ad1756a187?auto=format&fit=crop&w=1200&q=80", "Orchard bar at sundown"),
]


def gallery(root: str) -> str:
    cats = ["All"] + sorted({c for c, _, _ in GALLERY})
    _filter_keys = {"All": "gallery.filter.all", "Suites": "gallery.filter.suites", "Spa": "gallery.filter.spa", "Garden": "gallery.filter.garden", "Dining": "gallery.filter.dining", "Bar": "gallery.filter.bar"}
    filters = "".join(
        f'<button data-cat="{c}" class="gal-filter px-4 py-2 rounded-full border border-mira-300 text-sm text-mira-800 hover:bg-mira-900 hover:text-white transition{" bg-mira-900 text-white border-mira-900" if c == "All" else ""}" data-i18n="{_filter_keys.get(c, "gallery.filter." + c.lower())}">{c}</button>'
        for c in cats
    )
    def _u(u): return u if u.startswith("http") else f"{root}{u}"
    tiles = "".join(
        f'<figure class="gal-item break-inside-avoid mb-4 rounded-lg overflow-hidden shadow group" data-cat="{c}">'
        f'<div class="aspect-[4/5] bg-cover bg-center transition duration-500 group-hover:scale-[1.03]" style="background-image:url(\'{_u(url)}\')"></div>'
        f'<figcaption class="px-3 py-2 bg-white text-xs text-mira-600">{alt}</figcaption></figure>'
        for c, url, alt in GALLERY
    )
    h = hero(GALLERY[0][1],
             '<span data-i18n="gallery.hero.kicker">Gallery</span>',
             '<span data-i18n="gallery.hero.h1">A photo album.</span>',
             '<span data-i18n="gallery.hero.sub">Real photography will replace every image on this site before launch. The frames below are representative — Turkish Riviera resort imagery from Unsplash — to give the design its shape.</span>',
             height="55vh")
    body = section(f"""
      <div class="flex flex-wrap items-center gap-2">{filters}</div>
      <div class="mt-8 columns-2 md:columns-3 lg:columns-4 gap-4">{tiles}</div>
      <script>
        (function() {{
          const btns = document.querySelectorAll('.gal-filter');
          const items = document.querySelectorAll('.gal-item');
          btns.forEach(b => b.addEventListener('click', () => {{
            btns.forEach(x => x.classList.remove('bg-mira-900','text-white','border-mira-900'));
            b.classList.add('bg-mira-900','text-white','border-mira-900');
            const cat = b.dataset.cat;
            items.forEach(it => {{
              it.style.display = (cat === 'All' || it.dataset.cat === cat) ? '' : 'none';
            }});
          }}));
        }})();
      </script>
    """, bg="bg-sand-50")
    return h + body


def offers(root: str) -> str:
    # R025: real Mira Palace photos on every card (was 5 Unsplash stock
    # shots including a tropical palm-beach fabrication that misrepresented
    # our Mediterranean coast). Each card now shows an actual hotel view.
    offers_data = [
        ("offers.card1", "Summer 2026 Early Bird", "Up to 25% off",
         "Book by 31 May 2026 for arrivals before 15 July. Minimum three nights, direct bookings only.",
         "assets/img/garden/garden-01.webp"),
        ("offers.card2", "Late-summer escape", "Stay 7, pay 6",
         "Arrivals between 1 and 30 September 2026. Complimentary airport transfer for two. Minimum stay seven nights.",
         "assets/img/garden/garden-04.webp"),
        ("offers.card3", "Honeymoon package", "Included extras",
         "Sparkling wine and flowers on arrival, private hammam session for two, à-la-carte dinner on the beach. Marriage certificate (any date) required.",
         "assets/img/king/king-01.webp"),
        ("offers.card4", "Wellness week", "Spa credit €200 p.p.",
         "Seven nights including full wellness programme, daily yoga, two hammam rituals, two massages, and a personalised nutrition plan.",
         "assets/img/spa/spa-01.webp"),
        ("offers.card5", "Winter warmer", "30% off",
         "A quiet coastline in winter. Direct bookings for November–February arrivals, 4+ nights. Breakfast upgraded, early check-in from 11:00.",
         "assets/img/garden/garden-06.webp"),
    ]
    cards = "".join(
        f'<article class="grid md:grid-cols-5 overflow-hidden rounded-lg bg-white shadow-lux"><div class="md:col-span-2 aspect-[16/10] md:aspect-auto bg-cover bg-center" style="background-image:url(\'{root}{img}\')"></div><div class="md:col-span-3 p-8"><div class="text-xs uppercase tracking-widest text-sand-600" data-i18n="{k}.tag">{tag}</div><h3 class="font-display text-2xl text-mira-900 mt-1" data-i18n="{k}.title">{t}</h3><p class="mt-3 text-mira-700 text-sm leading-relaxed" data-i18n="{k}.body">{d}</p><a href="{root}contact.html#enquiry" class="mt-6 inline-flex items-center gap-2 text-sm font-medium text-mira-700 hover:text-sand-600"><span data-i18n="offers.card.cta">Enquire about this offer</span> <span>→</span></a></div></article>'
        for k, t, tag, d, img in offers_data
    )
    # R025: hero is a random-video-per-visit shuffler picked by site.js from
    # window.MIRA_VIDEOS. No repeat within the same browser session. The
    # poster JPG here is only shown for the ~200ms before the JS swaps in
    # the chosen video source — we use garden-01 as a safe fallback.
    poster = f"{root}assets/img/garden/garden-01.webp"
    h = dedent(f"""
    <section class="relative hero-section overflow-hidden" style="min-height:60vh;">
      <div class="absolute inset-0 bg-cover bg-center" style="background-image:url('{poster}');"></div>
      <video id="offers-hero-video" class="absolute inset-0 w-full h-full object-cover" autoplay loop muted playsinline preload="metadata" poster="{poster}" aria-hidden="true">
        <source src="" type="video/mp4" />
      </video>
      <div class="absolute inset-0 hero-overlay pointer-events-none"></div>
      <div class="relative max-w-7xl mx-auto px-5 lg:px-8 pt-14 pb-16 text-white flex flex-col justify-start" style="min-height:60vh;">
        <div class="max-w-3xl">
          <p class="uppercase tracking-[0.22em] text-sand-300 text-xs sm:text-sm font-semibold mb-4" data-i18n="offers.hero.kicker">Offers</p>
          <h1 class="font-display text-4xl sm:text-5xl md:text-6xl leading-[1.05]" data-i18n="offers.hero.h1">Current offers &amp; packages.</h1>
          <p class="mt-5 max-w-2xl text-base sm:text-lg text-white/90 leading-relaxed" data-i18n="offers.hero.sub">Best rates are always direct. These packages are reserved for direct bookings — if you've come from an agent or OTA, we can still honour them up to 24 hours after booking.</p>
        </div>
      </div>
    </section>
    """)
    body = section(f"""
      <div class="space-y-8">{cards}</div>
      <p class="mt-10 text-xs text-mira-500 italic" data-i18n="offers.foot">All rates, percentages and inclusions are illustrative for this demonstration site. Real offers and terms will be supplied by the hotel on content hand-off.</p>
    """, bg="bg-sand-50")
    return h + body


PAGES = [
    {"path": "gallery.html", "active": "gallery",
     "title": "Gallery · Mira Palace",
     "description": "Photographs of Mira Palace — rooms, pools, beach, dining, spa and hotel.",
     "body": gallery},
    {"path": "offers.html", "active": "offers",
     "title": "Offers · Mira Palace",
     "description": "Current offers and packages at Mira Palace — early-bird, honeymoon, wellness week, winter warmer.",
     "body": offers},
]
