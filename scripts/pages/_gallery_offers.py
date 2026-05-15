from common import hero, section

# Single curated set for gallery
GALLERY = [
    ("Suites",  "https://images.unsplash.com/photo-1590490360182-c33d57733427?auto=format&fit=crop&w=1200&q=80",  "The Standard Suite"),
    ("Suites",  "https://images.unsplash.com/photo-1611892440504-42a792e24d32?auto=format&fit=crop&w=1200&q=80",  "Deluxe Suite with sea view"),
    ("Suites",  "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?auto=format&fit=crop&w=1200&q=80",  "Family Suite (connecting)"),
    ("Suites",  "https://images.unsplash.com/photo-1590073242678-70ee3fc28e8e?auto=format&fit=crop&w=1200&q=80",  "King Suite bedroom"),
    ("Suites",  "https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?auto=format&fit=crop&w=1200&q=80",   "Marble bathroom"),
    ("Pools",   "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1200&q=80",  "Main pool, afternoon"),
    ("Pools",   "https://images.unsplash.com/photo-1540541338287-41700207dee6?auto=format&fit=crop&w=1200&q=80",  "Pool deck"),
    ("Pools",   "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=1200&q=80",  "Infinity pool"),
    ("Beach",   "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80",  "Sunrise at the beach club"),
    ("Beach",   "https://images.unsplash.com/photo-1519046904884-53103b34b206?auto=format&fit=crop&w=1200&q=80",  "Beach umbrellas, June"),
    ("Dining",  "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1200&q=80",  "Main restaurant at dinner"),
    ("Dining",  "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=1200&q=80",   "Plated starter"),
    ("Dining",  "https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=1200&q=80", "Breakfast buffet"),
    ("Dining",  "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=1200&q=80", "Mezze at the pool restaurant"),
    ("Bar",     "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&w=1200&q=80", "Lobby bar cocktail"),
    ("Bar",     "https://images.unsplash.com/photo-1470337458703-46ad1756a187?auto=format&fit=crop&w=1200&q=80", "Orchard bar at sundown"),
    ("Spa",     "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=1200&q=80",  "Treatment room"),
    ("Spa",     "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=1200&q=80", "Hammam entrance"),
    ("Spa",     "https://images.unsplash.com/photo-1519823551278-64ac92734fb1?auto=format&fit=crop&w=1200&q=80", "Massage in progress"),
    ("Hotel",   "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1200&q=80",  "Lobby at dusk"),
    ("Hotel",   "https://images.unsplash.com/photo-1589489873962-88a30d7aa96c?auto=format&fit=crop&w=1200&q=80", "Side, from the coast"),
    ("Hotel",   "https://images.unsplash.com/photo-1504754524776-8f4f37790ca0?auto=format&fit=crop&w=1200&q=80", "Breakfast spread"),
]


def gallery(root: str) -> str:
    cats = ["All"] + sorted({c for c, _, _ in GALLERY})
    filters = "".join(
        f'<button data-cat="{c}" class="gal-filter px-4 py-2 rounded-full border border-mira-300 text-sm text-mira-800 hover:bg-mira-900 hover:text-white transition{" bg-mira-900 text-white border-mira-900" if c == "All" else ""}">{c}</button>'
        for c in cats
    )
    tiles = "".join(
        f'<figure class="gal-item break-inside-avoid mb-4 rounded-lg overflow-hidden shadow group" data-cat="{c}">'
        f'<div class="aspect-[4/5] bg-cover bg-center transition duration-500 group-hover:scale-[1.03]" style="background-image:url(\'{url}\')"></div>'
        f'<figcaption class="px-3 py-2 bg-white text-xs text-mira-600">{alt}</figcaption></figure>'
        for c, url, alt in GALLERY
    )
    h = hero(GALLERY[0][1], "Gallery", "A photo album.",
             "Real photography will replace every image on this site before launch. The frames below are representative — Turkish Riviera resort imagery from Unsplash — to give the design its shape.",
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
    offers_data = [
        ("Summer 2026 Early Bird", "Up to 25% off", "Book by 31 May 2026 for arrivals before 15 July. Minimum three nights, direct bookings only.", "https://images.unsplash.com/photo-1540541338287-41700207dee6?auto=format&fit=crop&w=1600&q=80"),
        ("Late-summer escape", "Stay 7, pay 6", "Arrivals between 1 and 30 September 2026. Complimentary airport transfer for two. Minimum stay seven nights.", "https://images.unsplash.com/photo-1519046904884-53103b34b206?auto=format&fit=crop&w=1600&q=80"),
        ("Honeymoon package", "Included extras", "Sparkling wine and flowers on arrival, private hammam session for two, à-la-carte dinner on the beach. Marriage certificate (any date) required.", "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=1600&q=80"),
        ("Wellness week", "Spa credit €200 p.p.", "Seven nights including full wellness programme, daily yoga, two hammam rituals, two massages, and a personalised nutrition plan.", "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=1600&q=80"),
        ("Winter warmer", "30% off", "A quiet coastline in winter. Direct bookings for November–February arrivals, 4+ nights. Breakfast upgraded, early check-in from 11:00.", "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1600&q=80"),
    ]
    cards = "".join(
        f'<article class="grid md:grid-cols-5 overflow-hidden rounded-lg bg-white shadow-lux"><div class="md:col-span-2 aspect-[16/10] md:aspect-auto bg-cover bg-center" style="background-image:url(\'{img}\')"></div><div class="md:col-span-3 p-8"><div class="text-xs uppercase tracking-widest text-sand-600">{tag}</div><h3 class="font-display text-2xl text-mira-900 mt-1">{t}</h3><p class="mt-3 text-mira-700 text-sm leading-relaxed">{d}</p><a href="{root}contact.html#enquiry" class="mt-6 inline-flex items-center gap-2 text-sm font-medium text-mira-700 hover:text-sand-600">Enquire about this offer <span>→</span></a></div></article>'
        for t, tag, d, img in offers_data
    )
    h = hero("https://images.unsplash.com/photo-1540541338287-41700207dee6?auto=format&fit=crop&w=1920&q=80",
             "Offers", "Current offers &amp; packages.",
             "Best rates are always direct. These packages are reserved for direct bookings — if you’ve come from an agent or OTA, we can still honour them up to 24 hours after booking.", height="55vh")
    body = section(f"""
      <div class="space-y-8">{cards}</div>
      <p class="mt-10 text-xs text-mira-500 italic">All rates, percentages and inclusions are illustrative for this demonstration site. Real offers and terms will be supplied by the hotel on content hand-off.</p>
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
