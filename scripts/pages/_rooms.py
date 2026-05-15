from common import hero, section, eyebrow, heading, lead, card
from textwrap import dedent

IMG_STD = "https://images.unsplash.com/photo-1590490360182-c33d57733427?auto=format&fit=crop&w=1600&q=80"
IMG_DLX = "https://images.unsplash.com/photo-1611892440504-42a792e24d32?auto=format&fit=crop&w=1600&q=80"
IMG_FAM = "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?auto=format&fit=crop&w=1600&q=80"
IMG_SUITE = "https://images.unsplash.com/photo-1590073242678-70ee3fc28e8e?auto=format&fit=crop&w=1600&q=80"
IMG_BATH = "https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?auto=format&fit=crop&w=1200&q=80"
IMG_BALCONY = "https://images.unsplash.com/photo-1540541338287-41700207dee6?auto=format&fit=crop&w=1200&q=80"

# NB: "count" is the number of suites in the property (internal use only — the
# website never displays it). It feeds the FAQ doc in reference\documents\.
ROOM_TYPES = [
    {"slug": "standard",  "name": "Standard Suite", "count": 19, "size": "22 m²", "view": "Garden view",   "sleeps": "2 adults",            "img": IMG_STD,
     "tag": "From €130 / night*", "short": "A compact, beautifully made double with a French balcony opening onto the citrus orchard."},
    {"slug": "deluxe",    "name": "Deluxe Suite",   "count": 10, "size": "28 m²", "view": "Sea view",       "sleeps": "2 adults + 1 child",  "img": IMG_DLX,
     "tag": "From €180 / night*", "short": "A larger suite with a full balcony, panoramic sea view, and a walk-in rain shower."},
    {"slug": "family",    "name": "Family Suite",   "count":  4, "size": "34 m²", "view": "Garden view",   "sleeps": "2 adults + 2 children","img": IMG_FAM,
     "tag": "From €220 / night*", "short": "Two connecting suites sharing a vestibule and a single en-suite for easy family access."},
    {"slug": "king",      "name": "King Suite",     "count":  1, "size": "42 m²", "view": "Sea view",       "sleeps": "2 adults + 1 child",  "img": IMG_SUITE,
     "tag": "From €290 / night*", "short": "A sitting-room and a separate bedroom, a deep freestanding tub, and a wrap-around balcony."},
]


def rooms_index(root: str) -> str:
    cards_html = "".join(
        dedent(f"""
        <a href="{root}rooms/{r['slug']}.html" class="group grid md:grid-cols-5 gap-0 bg-white rounded-lg overflow-hidden shadow-lux">
          <div class="md:col-span-3 aspect-[16/10] md:aspect-auto bg-cover bg-center" style="background-image:url('{r['img']}')"></div>
          <div class="md:col-span-2 p-8 flex flex-col">
            <div class="text-xs uppercase tracking-widest text-sand-600">{r['tag']}</div>
            <h3 class="font-display text-3xl text-mira-900 mt-2">{r['name']}</h3>
            <div class="mt-3 flex flex-wrap gap-x-5 gap-y-1 text-sm text-mira-700">
              <span>{r['size']}</span><span>•</span><span>{r['view']}</span><span>•</span><span>{r['sleeps']}</span>
            </div>
            <p class="mt-4 text-mira-700 text-sm leading-relaxed">{r['short']}</p>
            <span class="mt-6 inline-flex items-center gap-2 text-sm font-medium text-mira-700 group-hover:text-sand-500">View the suite <span>→</span></span>
          </div>
        </a>
        """) for r in ROOM_TYPES
    )
    h = hero(
        IMG_DLX,
        "Rooms & Suites",
        "Thirty-four suites.<br/>Four ways to sleep.",
        "Every room at Mira Palace is individually styled — no two are identical, but all share the same hand-woven linens, the same Turkish ceramics, and the same Mediterranean light through the shutters.",
        height="68vh",
    )
    body = section(f"""
      {eyebrow('Choose your suite')}
      {heading('Our suite types.')}
      {lead('All rates are illustrative. Final rates depend on season and length of stay; please request a quote for your dates.')}
      <div class="mt-12 grid gap-8">{cards_html}</div>
      <p class="mt-10 text-xs text-mira-600">* Indicative demo rates in EUR, All-Inclusive, double occupancy, shoulder season. Real rates will be supplied by the hotel during content hand-off.</p>
    """, bg="bg-sand-50")
    return h + body


def _room_detail(r: dict, root: str, long_body: str, extra_imgs: list[str]) -> str:
    amenities_left = [
        "King-size or twin bed with hand-woven cotton linens",
        "Black-out curtains and insulated shutters",
        "Individually controlled air-conditioning & heating",
        "55\" 4K Smart TV with international channels & casting",
        "Dedicated writing desk and reading chair",
        "Complimentary Wi-Fi (500 Mbps fibre)",
        "Mini-fridge restocked daily with soft drinks, beer, water",
        "Nespresso machine, tea selection, electric kettle",
    ]
    amenities_right = [
        "Rain shower with Italian ceramic tilework",
        "Marble double vanity with back-lit mirror",
        "Turkish-cotton bathrobes, slippers, amenity set",
        "In-room safe (laptop size)",
        "Bluetooth bedside speaker",
        "Complimentary still & sparkling water",
        "USB-C and UK/EU power sockets bedside",
        "24-hour in-room dining",
    ]
    am_l = "".join(f'<li class="flex gap-3"><span class="text-sand-500">✓</span><span>{a}</span></li>' for a in amenities_left)
    am_r = "".join(f'<li class="flex gap-3"><span class="text-sand-500">✓</span><span>{a}</span></li>' for a in amenities_right)
    gallery = "".join(
        f'<div class="aspect-[4/3] bg-cover bg-center rounded" style="background-image:url(\'{u}\')"></div>'
        for u in extra_imgs
    )
    h = hero(r["img"], "Rooms & Suites", r["name"],
             f'{r["size"]} · {r["view"]} · Sleeps {r["sleeps"]}. {r["short"]}',
             primary_href=f"{root}contact.html#enquiry", primary_label="Enquire for your dates", height="72vh")
    body = section(f"""
      <div class="grid lg:grid-cols-12 gap-12">
        <div class="lg:col-span-7 text-mira-700 leading-relaxed text-lg space-y-5">
          {long_body}
        </div>
        <aside class="lg:col-span-5">
          <div class="bg-white rounded-lg shadow-lux p-7 sticky top-28">
            <div class="text-xs uppercase tracking-widest text-sand-600">{r['tag']}</div>
            <h2 class="font-display text-3xl text-mira-900 mt-2">Your room at a glance</h2>
            <dl class="mt-5 grid grid-cols-2 gap-y-3 text-sm">
              <dt class="text-mira-600">Size</dt><dd class="text-right font-medium">{r['size']}</dd>
              <dt class="text-mira-600">View</dt><dd class="text-right font-medium">{r['view']}</dd>
              <dt class="text-mira-600">Sleeps</dt><dd class="text-right font-medium">{r['sleeps']}</dd>
              <dt class="text-mira-600">Balcony</dt><dd class="text-right font-medium">Yes</dd>
              <dt class="text-mira-600">Smoking</dt><dd class="text-right font-medium">No (terrace OK)</dd>
            </dl>
            <a href="{root}contact.html#enquiry" class="mt-6 w-full inline-flex items-center justify-center px-6 py-3 bg-mira-700 text-white rounded-full font-medium hover:bg-mira-800">Enquire now</a>
            <a href="{root}concept.html" class="mt-3 w-full inline-flex items-center justify-center text-sm text-mira-700 hover:text-sand-600">What's included →</a>
          </div>
        </aside>
      </div>
    """, bg="bg-white")
    amen = section(f"""
      {eyebrow('Amenities')}
      {heading('Every room, fully equipped.', 3)}
      <div class="mt-8 grid md:grid-cols-2 gap-x-10 gap-y-3 text-mira-700 text-sm">
        <ul class="space-y-3">{am_l}</ul>
        <ul class="space-y-3">{am_r}</ul>
      </div>
    """, bg="bg-sand-50")
    imgs = section(f"""
      {eyebrow('Inside the room')}
      {heading('A closer look.', 3)}
      <div class="mt-8 grid grid-cols-2 md:grid-cols-4 gap-3">{gallery}</div>
    """, bg="bg-white")
    other_rooms_cards = "".join(
        f'<a href="{root}rooms/{o["slug"]}.html" class="group block"><div class="aspect-[4/3] bg-cover bg-center rounded" style="background-image:url(\'{o["img"]}\')"></div><h4 class="mt-3 font-display text-lg text-mira-900 group-hover:text-sand-600">{o["name"]}</h4><p class="text-xs text-mira-600">{o["size"]} · {o["view"]}</p></a>'
        for o in ROOM_TYPES if o["slug"] != r["slug"]
    )
    others = section(f"""
      {eyebrow('Other rooms')}
      {heading('You may also like.', 3)}
      <div class="mt-8 grid grid-cols-2 md:grid-cols-3 gap-6">{other_rooms_cards}</div>
    """, bg="bg-sand-50")
    return h + body + amen + imgs + others


def standard(root: str) -> str:
    r = next(x for x in ROOM_TYPES if x["slug"] == "standard")
    long_body = """
      <p>The Standard Suite is our most popular category — and our workhorse. Twenty-two square metres of quiet, insulated from the corridor by a thick door and from the garden by double-glazing. One king-size bed (or twin, on request), a French balcony with a small bistro table, and an uninterrupted view into the citrus orchard that wraps the east wing.</p>
      <p>The bathroom is a walk-in rain shower with Iznik tiles laid by a family workshop an hour from here, a double vanity, and a mirror the size of a window. The linens are Denizli cotton — the same fabric the hammam uses for peştemals. The desk is oak, from a workshop in Antalya's bazaar district.</p>
      <p>It is a suite designed to be used quietly. Most of the guests who book it spend their days at the pool or the beach and come back in the evening to change. It does that job extremely well — and if you want a little more room, we have three larger categories.</p>
    """
    return _room_detail(r, root, long_body, [IMG_STD, IMG_BATH, IMG_BALCONY, IMG_DLX])


def deluxe(root: str) -> str:
    r = next(x for x in ROOM_TYPES if x["slug"] == "deluxe")
    long_body = """
      <p>Six extra square metres buy you a lot at Mira Palace. The Deluxe Suite is twenty-eight square metres with a full balcony (two lounge chairs, a small table, a footstool) and a direct Mediterranean view across the orchard. The bed is a king-size; a rollaway for one child is possible on request.</p>
      <p>The bathroom adds a long marble bench to the rain shower — a small detail, but the kind that turns a shower into a place you linger. Bathrobes are waffle-textured rather than flat; bedside lighting is individually controlled.</p>
      <p>Our most booked category for couples celebrating something — anniversaries, honeymoons, birthdays with a zero on them. If it's one of those trips, write a note on the booking and we'll arrange a small something on the balcony at turndown.</p>
    """
    return _room_detail(r, root, long_body, [IMG_DLX, IMG_BATH, IMG_BALCONY, IMG_SUITE])


def family(root: str) -> str:
    r = next(x for x in ROOM_TYPES if x["slug"] == "family")
    long_body = """
      <p>The Family Suite is two connecting rooms sharing one vestibule and one bathroom — designed specifically for parents who want to hear their children without sharing their sleep. One side has a king-size bed; the other has two twin beds or (on request) bunks for children up to twelve.</p>
      <p>Both rooms open off a small hall with a door that closes. The shared bathroom is larger than the Standard's, with a deep tub alongside the shower and a second sink. Storage is planned for family trips — a wardrobe long enough for adult hanging, deep enough for children's luggage, and a chest with drawers marked with pictograms so small hands can find their own T-shirts.</p>
      <p>Baby cots, high-chairs at the restaurant, childproof socket covers, and a kids' welcome pack (colouring book, pencils, a Mira Palace teddy) all come as standard.</p>
    """
    return _room_detail(r, root, long_body, [IMG_FAM, IMG_BATH, IMG_STD, IMG_BALCONY])


def king(root: str) -> str:
    r = next(x for x in ROOM_TYPES if x["slug"] == "king")
    long_body = """
      <p>Our King Suite is forty-two square metres organised as two rooms — a sitting room with a sofa, a desk, and a reading chair; and a bedroom with a king-size bed. Between them, a heavy velvet curtain that you can draw when one of you wants to read while the other sleeps.</p>
      <p>The bathroom is the reason many of our returning guests return. A freestanding deep tub, a separate rain shower, a window with a view, and — because this is why you came — a full amenity kit: oils, salts, a bath brush, a bath caddy for a glass of wine.</p>
      <p>The balcony wraps around the corner of the building: twelve square metres with a sun lounger, two chairs, a dining table for two, and planters that change with the season. In summer, jasmine; in winter, rosemary and lavender.</p>
    """
    return _room_detail(r, root, long_body, [IMG_SUITE, IMG_BATH, IMG_BALCONY, IMG_DLX])


def _redirect_to_king(root: str) -> str:
    """Tiny HTML body for the old rooms/suite.html — keeps any external link
    working by sending visitors on to the new King Suite page."""
    return f"""
    <section class="bg-sand-50 py-24"><div class="max-w-2xl mx-auto px-5 text-center">
      <h1 class="font-display text-3xl text-mira-900">This page has moved</h1>
      <p class="mt-4 text-mira-700">The Junior Suite is now called the <a href="{root}rooms/king.html" class="underline text-sand-600">King Suite</a>. You'll be redirected automatically in a moment.</p>
      <noscript><p class="mt-4 text-sm text-mira-600">If your browser doesn't redirect, <a href="{root}rooms/king.html" class="underline">click here</a>.</p></noscript>
      <meta http-equiv="refresh" content="0; url={root}rooms/king.html" />
      <link rel="canonical" href="{root}rooms/king.html" />
      <script>window.location.replace("{root}rooms/king.html");</script>
    </div></section>
    """


PAGES = [
    {"path": "rooms/index.html", "active": "rooms",
     "title": "Suites · Mira Palace",
     "description": "Four suite types at Mira Palace, from 22 m² Standard Suite to 42 m² King Suite. Garden and sea views, all with full en-suite and balcony.",
     "body": rooms_index},
    {"path": "rooms/standard.html", "active": "rooms",
     "title": "Standard Suite · Mira Palace",
     "description": "The 22 m² Standard Suite at Mira Palace — garden view, French balcony, walk-in rain shower, king-size bed.",
     "body": standard},
    {"path": "rooms/deluxe.html", "active": "rooms",
     "title": "Deluxe Suite · Mira Palace",
     "description": "The 28 m² Deluxe Suite at Mira Palace — sea-view balcony, marble rain shower, king-size bed.",
     "body": deluxe},
    {"path": "rooms/family.html", "active": "rooms",
     "title": "Family Suite · Mira Palace",
     "description": "34 m² of connecting suites for families — one king-size bed, two twins, shared en-suite, garden view.",
     "body": family},
    {"path": "rooms/king.html", "active": "rooms",
     "title": "King Suite · Mira Palace",
     "description": "The 42 m² King Suite at Mira Palace — separate sitting room, wrap-around balcony, freestanding bath, sea view.",
     "body": king},
    # Legacy URL — quietly forwards visitors of the old Junior Suite link.
    {"path": "rooms/suite.html", "active": "rooms",
     "title": "King Suite · Mira Palace",
     "description": "The King Suite at Mira Palace (formerly Junior Suite).",
     "body": _redirect_to_king},
]
