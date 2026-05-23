from common import hero, hero_video, hero_slideshow, section, eyebrow, heading, card, feature_strip, cta_band, quote_block, specials_card

IMG_POOL = "assets/img/garden/garden-01.jpg"
IMG_GARDEN_2 = "assets/img/garden/garden-02.jpg"
IMG_GARDEN_3 = "assets/img/garden/garden-03.jpg"
IMG_GARDEN_4 = "assets/img/garden/garden-04.jpg"
IMG_ROOM = "assets/img/king/king-01.jpg"   # real King Suite signature shot
IMG_DINING = "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1200&q=80"
IMG_SPA = "assets/img/spa/spa-01.jpg"      # real spa hero shot
IMG_BEACH = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1920&q=80"
IMG_LOBBY = "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1920&q=80"
IMG_BREAKFAST = "https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=1200&q=80"

# HERO_POSTER is the still image visible while the home-page hero video
# is buffering. Real Mira Palace garden shot looks more inviting than a
# stock pool photo.
HERO_POSTER = IMG_POOL


def home(root: str) -> str:
    h = hero_video(
        f"{root}{HERO_POSTER}",
        "Side • Antalya • Türkiye",
        "The Turkish Riviera,<br/>reimagined in quiet luxury.",
        "Thirty-four suites, four pools, and a Mediterranean shoreline 600 metres from your door. Mira Palace is a small, boutique all-inclusive where the entire team knows your name by the second morning.",
        primary_href=f"{root}rooms/",
        primary_label="Explore our suites",
        height="88vh",
        root=root,
        extras_html=specials_card(root),
    )
    intro = section(f"""
      <div class="grid lg:grid-cols-12 gap-12 items-start">
        <div class="lg:col-span-5">{eyebrow('A quieter kind of resort')}
          {heading('Big-hotel comfort, small-hotel soul.')}
        </div>
        <div class="lg:col-span-7 text-mira-700 leading-relaxed text-lg space-y-4">
          <p>Open since May 2022, Mira Palace was designed for travellers who want the convenience of an all-inclusive resort — unlimited dining, a full spa, pools for every mood — but in a setting small enough that the staff learn your favourite drink by the second evening.</p>
          <p>Thirty-four suites, individually styled. Four pools, including an adults-only infinity pool overlooking the orchard. A beach club 600 metres from reception. And a kitchen that refuses to serve the same buffet twice in a week.</p>
        </div>
      </div>
      <div class="mt-14">{feature_strip([('Suites','34'),('Pools','4'),('To the beach','600 m'),('To Side old town','12 km'),('Antalya airport','60 km'),('Operates year-round','12/12')])}</div>
    """)
    three = section(f"""
      {eyebrow('Three ways to spend a day')}
      {heading('Stay. Eat. Unwind.')}
      <div class="grid md:grid-cols-3 gap-7 mt-12">
        {card(f"{root}{IMG_ROOM}", "Suites", "Four suite types from 22 to 42 m² — Standard, Deluxe, Family and the King Suite. Garden courtyard or sea-view balcony, all with full en-suite.", f"{root}rooms/", "See our suites")}
        {card(IMG_DINING, "Dining", "Four outlets under one roof — from the open buffet kitchen to à-la-carte evenings by the pool and a lobby bar that stays open late.", f"{root}dining/", "Discover dining")}
        {card(f"{root}{IMG_SPA}", "Spa & wellness", "A full Turkish hammam, two saunas, a steam room, cold plunge, and a treatment menu from a 40-minute back massage to a three-hour hammam ritual.", f"{root}spa.html", "Enter the spa")}
      </div>
    """, bg="bg-white")
    concept_band = cta_band(
        "Everything included. Nothing forgotten.",
        "Unlimited buffet breakfasts, lunches and dinners. All soft drinks, local beers, wines and spirits. Afternoon tea and late-night snacks. Pools, beach, hammam access, fitness classes, evening entertainment. See what's covered.",
        f"{root}concept.html",
        "See the All-Inclusive concept",
        IMG_LOBBY,
    )
    testimonial = section(quote_block(
        "Bu küçük otel, büyük zincirlerin üç katı özenle işliyor. Akşam yemeğinde şefi selamlıyorsun, sabah kapıcıyı, öğleden sonra spa menajerini. 34 oda için tam ihtiyacı olan enerji.",
        "Demo review", "Sample Google review (translation placeholder — swap for real)"
    ), bg="bg-mira-50")
    gallery_teaser = section(f"""
      <div class="flex flex-wrap items-end justify-between gap-6 mb-8">
        <div>{eyebrow('Moments at Mira Palace')}
          {heading('A glimpse of your stay.')}
        </div>
        <a href="{root}gallery.html" class="text-sm font-medium text-mira-700 hover:text-sand-500 inline-flex items-center gap-2">Full gallery <span>→</span></a>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{root}{IMG_POOL}')"></div>
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{root}assets/img/king/king-03.jpg')"></div>
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{IMG_DINING}')"></div>
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{root}assets/img/spa/spa-02.jpg')"></div>
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{root}assets/img/garden/garden-05.jpg')"></div>
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{IMG_BREAKFAST}')"></div>
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{root}assets/img/deluxe/deluxe-02.jpg')"></div>
        <div class="aspect-[4/5] bg-cover bg-center rounded bg-mira-700 grid place-items-center text-sand-200 font-display text-xl"><a href="{root}gallery.html">See all →</a></div>
      </div>
    """, bg="bg-white")
    location_teaser = section(f"""
      <div class="grid lg:grid-cols-2 gap-10 items-center">
        <div>{eyebrow('Where you are')}
          {heading('Evrenseki, between Side and the Taurus Mountains.')}
          <p class="mt-5 text-mira-700 leading-relaxed">Fifteen minutes east of Side's ancient harbour, forty-five minutes from Antalya International Airport, and a short walk along a cypress-lined lane from our private stretch of Mediterranean beach. Pool weather from April to November, spa weather all year.</p>
          <div class="mt-6 grid grid-cols-3 gap-4 text-sm">
            <div><div class="font-display text-2xl text-mira-800">600 m</div><div class="text-mira-600">To the beach</div></div>
            <div><div class="font-display text-2xl text-mira-800">12 km</div><div class="text-mira-600">To Side old town</div></div>
            <div><div class="font-display text-2xl text-mira-800">60 km</div><div class="text-mira-600">To Antalya airport</div></div>
          </div>
          <a href="{root}location.html" class="mt-8 inline-flex items-center gap-2 text-mira-700 font-medium hover:text-sand-500">Directions &amp; transfers <span>→</span></a>
        </div>
        <div class="aspect-[4/3] rounded-lg bg-cover bg-center shadow-lux" style="background-image:url('{IMG_BEACH}')"></div>
      </div>
    """, bg="bg-sand-50")
    return h + intro + three + concept_band + testimonial + gallery_teaser + location_teaser


def about(root: str) -> str:
    # 4-slide garden hero — sweeping, evocative, real Mira Palace photography
    hero_urls = [f"{root}{u}" for u in (IMG_POOL, IMG_GARDEN_2, IMG_GARDEN_3, IMG_GARDEN_4)]
    h = hero_slideshow(
        hero_urls,
        "Our story",
        "Small hotel. Big intent.",
        "Opened in May 2022 by a family who believed the Turkish Riviera deserved a boutique option between the sprawling resorts and the guesthouses — where service feels personal and the design tells a story.",
        height="70vh",
    )
    story = section(f"""
      <div class="grid lg:grid-cols-12 gap-12">
        <div class="lg:col-span-4">{eyebrow('Since 2022')}
          {heading('How Mira Palace began.')}
        </div>
        <div class="lg:col-span-8 text-mira-700 leading-relaxed space-y-5 text-lg">
          <p>The property opened its doors in May 2022 after three years of design and construction. Thirty-four suites were built instead of a hundred — because we wanted a kitchen that could cook to order, a pool team that could remember how your family likes its towels, and a front desk that never feels overwhelmed.</p>
          <p>The building sits in Evrenseki, a quiet village east of Side, surrounded by citrus orchards and pomegranate trees. Many of those were there before the hotel was; some have been planted since. The restaurant's winter menu leans heavily on what the orchard gives us — pomegranate molasses, bitter orange marmalade, quince paste, lemon curd.</p>
          <p>We are open twelve months of the year. Summer is pools and beach; winter is the lobby fireplace, the hammam, and the quiet. Both seasons have the same number of smiles at reception.</p>
        </div>
      </div>
    """, bg="bg-white")
    values = section(f"""
      {eyebrow('What we care about', 'text-sand-600')}
      {heading('Three promises, kept quietly.')}
      <div class="grid md:grid-cols-3 gap-7 mt-12">
        <div class="p-8 bg-white rounded-lg shadow-lux"><div class="font-display text-3xl text-sand-500">01</div><h3 class="mt-4 font-display text-2xl text-mira-900">Small enough to notice</h3><p class="mt-3 text-mira-700 text-sm leading-relaxed">Thirty-four suites means the bar knows your drink, the kitchen remembers your allergy, the spa recognises your voice. Not because of a system — because there are only thirty-four of you.</p></div>
        <div class="p-8 bg-white rounded-lg shadow-lux"><div class="font-display text-3xl text-sand-500">02</div><h3 class="mt-4 font-display text-2xl text-mira-900">Honest all-inclusive</h3><p class="mt-3 text-mira-700 text-sm leading-relaxed">No wristbands, no fine print, no up-sell. The food you see on the menu is the food included. The wine poured at dinner is the same wine poured at lunch. Extras are clearly marked; almost nothing is an extra.</p></div>
        <div class="p-8 bg-white rounded-lg shadow-lux"><div class="font-display text-3xl text-sand-500">03</div><h3 class="mt-4 font-display text-2xl text-mira-900">Of the place</h3><p class="mt-3 text-mira-700 text-sm leading-relaxed">Furniture from Antalya workshops. Linens from Denizli cotton. Olive oil from a single grove eight kilometres away. Tiles from a ceramicist in Iznik. If we can source it locally, we do.</p></div>
      </div>
    """, bg="bg-mira-50")
    cta = cta_band(
        "Come and meet us.",
        "Every review we read starts with the same sentence: it felt like a home. Book direct and get a bottle of local wine on arrival, a late check-out when it's possible, and a welcome from the owner's family.",
        f"{root}contact.html#enquiry",
        "Plan your stay",
        f"{root}{IMG_POOL}",
    )
    return h + story + values + cta


PAGES = [
    {"path": "index.html", "active": "home",
     "title": "Mira Palace · Boutique all-inclusive on the Turkish Riviera",
     "description": "A 34-suite boutique all-inclusive hotel in Side, Antalya. Four pools, full Turkish hammam, private beach 600 metres from reception.",
     "body": home},
    {"path": "about.html", "active": "about",
     "title": "About · Mira Palace",
     "description": "The story of Mira Palace — a small Turkish-Riviera hotel opened in 2022 with thirty-four suites and one simple idea.",
     "body": about},
]
