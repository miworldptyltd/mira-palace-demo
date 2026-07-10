from common import hero, hero_video, hero_slideshow, section, eyebrow, heading, card, feature_strip, cta_band, quote_block, reviews_hero_card

IMG_POOL = "assets/img/garden/garden-01.webp"
IMG_GARDEN_2 = "assets/img/garden/garden-02.webp"
IMG_GARDEN_3 = "assets/img/garden/garden-03.webp"
IMG_GARDEN_4 = "assets/img/garden/garden-04.webp"
IMG_ROOM = "assets/img/king/king-01.webp"    # real King Suite signature shot
IMG_SPA  = "assets/img/spa/spa-01.webp"      # real spa hero

# R021 image audit: the four constants below used to be generic Unsplash
# shots that showed *specific* venues (a restaurant, a hotel lobby, a
# breakfast spread, a tropical beach) — presenting them as Mira Palace
# spaces when they weren't. Fixed: dining now uses the live sidemirapalace.com
# bar photo (same as the dining hub hero); the other three swap to real
# Mira Palace photography already on disk.
IMG_DINING    = "https://sidemirapalace.com/img/restaurant/20240713110135_88159.png"  # real bar from live site
IMG_LOBBY     = "assets/img/garden/garden-06.webp"      # real garden (used on "everything included" band)
IMG_BREAKFAST = "assets/img/standard/standard-01.webp"  # real Standard Suite — rounds gallery out to all 4 room types
IMG_BEACH     = "assets/img/garden/garden-07.webp"      # real garden/exterior — TODO: swap for a real beach photo when the hotel supplies one

# HERO_POSTER is the still image visible while the home-page hero video
# is buffering. Real Mira Palace garden shot looks more inviting than a
# stock pool photo.
HERO_POSTER = IMG_POOL


def home(root: str) -> str:
    h = hero_video(
        f"{root}{HERO_POSTER}",
        '<span data-i18n="home.hero.kicker">Side • Antalya • Türkiye</span>',
        '<span data-i18n="home.hero.h1">The Turkish Riviera, reimagined in quiet luxury.</span>',
        '<span data-i18n="home.hero.sub">Thirty-four suites, two pools (one outdoor, one indoor) and Evrenseki\'s Blue-Flag public beach a seven-minute walk down a cypress lane. A small, boutique all-inclusive where the entire team knows your name by the second morning.</span>',
        primary_href=f"{root}rooms/",
        primary_label='<span data-i18n="home.hero.cta_suites">Explore our suites</span>',
        secondary_href=f"{root}offers.html",
        secondary_label='<span data-i18n="home.hero.cta_offers">See our special offers</span>',
        height="88vh",
        root=root,
        # R025: Specials card replaced by a real guest-reviews carousel per
        # owner request. Both are corner-slot components — same lg+ visibility
        # rule; on mobile the full reviews block below the hero handles social
        # proof. See reviews_hero_card() in common.py for the widget shape.
        extras_html=reviews_hero_card(root),
    )
    intro = section(f"""
      <div class="grid lg:grid-cols-12 gap-12 items-start">
        <div class="lg:col-span-5">{eyebrow('A quieter kind of resort')}
          {heading('Big-hotel comfort, small-hotel soul.')}
        </div>
        <div class="lg:col-span-7 text-mira-700 leading-relaxed text-lg space-y-4">
          <p data-i18n="home.intro.p1">Open since May 2022, Mira Palace was designed for travellers who want the convenience of an all-inclusive resort — unlimited dining, a full spa, pools for every mood — but in a setting small enough that the staff learn your favourite drink by the second evening.</p>
          <p data-i18n="home.intro.p2">Thirty-four suites, individually styled. Two pools — a generous outdoor pool for the season, and a heated indoor pool for winter mornings. Evrenseki\'s Blue-Flag public beach seven minutes down the lane. And a kitchen that refuses to serve the same buffet twice in a week.</p>
        </div>
      </div>
      <div class="mt-14">{feature_strip([('Suites','34'),('Pools','2'),('To Evrenseki beach','700 m'),('To Side old town','12 km'),('Antalya airport','60 km'),('Operates year-round','12/12')])}</div>
    """)
    three = section(f"""
      {eyebrow('Three ways to spend a day')}
      {heading('Stay. Eat. Unwind.')}
      <div class="grid md:grid-cols-3 gap-7 mt-12">
        {card(f"{root}{IMG_ROOM}", "Suites", "Four suite types from 22 to 42 m² — Standard, Deluxe, Family and the King Suite. Garden view or sea view, all with full en-suite.", f"{root}rooms/", "See our suites")}
        {card(IMG_DINING, "Dining", "Four outlets under one roof — from the open buffet kitchen to à-la-carte evenings by the pool and a lobby bar that stays open late.", f"{root}dining/", "Discover dining")}
        {card(f"{root}{IMG_SPA}", "Spa & wellness", "A full Turkish hammam, two saunas, a steam room, cold plunge, and a treatment menu from a 40-minute back massage to a three-hour hammam ritual.", f"{root}spa.html", "Enter the spa")}
      </div>
    """, bg="bg-white")
    concept_band = cta_band(
        '<span data-i18n="home.cta_band.h2">Everything included. Nothing forgotten.</span>',
        '<span data-i18n="home.cta_band.body">Unlimited buffet breakfasts, lunches and dinners. All soft drinks, local beers, wines and spirits. Afternoon tea and late-night snacks. Pools, beach, hammam access, fitness classes, evening entertainment. See what&#8217;s covered.</span>',
        f"{root}concept.html",
        '<span data-i18n="home.cta_band.btn">See the All-Inclusive concept</span>',
        f"{root}{IMG_LOBBY}",
    )
    # R025: swapped to real Google reviews (verified via Google Hotels
    # panel — 4.3★ from 118 reviews at the time of audit). Pelinsu (most
    # recent, family, TR original), Rianne (NL, praises spa), Abdullah
    # (couple angle) — same three reviewers used in the hero corner card
    # so the mobile experience mirrors desktop.
    reviews = [
        {
            "quote": "A quiet, peaceful place where families can stay with peace of mind — very clean rooms. Special thanks to Mustafa Bey, the owner, and Eren Bey for their hospitality.",
            "name": "Pelinsu Halıcı",
            "meta": "Family · Google · June 2026",
            "stars": 5,
        },
        {
            "quote": "We are very happy to be here — the staff and service was really nice and they helped us a lot with everything. You can feel like home, they have a big spa.",
            "name": "Rianne Van zandvoort",
            "meta": "Netherlands · Google · November 2025",
            "stars": 5,
        },
        {
            "quote": "Perfect for a quiet and beautiful holiday. The staff was friendly and took care of all our problems. A great place for a family or couple holiday.",
            "name": "Abdullah Topçu",
            "meta": "Couple · Google · 2024",
            "stars": 5,
        },
    ]
    def _stars(n):
        return "★" * n + "☆" * (5 - n)
    review_cards = "".join(
        f"""
        <article class="p-8 bg-white rounded-2xl shadow-lux flex flex-col h-full">
          <div class="text-sand-500 tracking-widest text-sm mb-4">{_stars(r['stars'])}</div>
          <blockquote class="font-display text-xl text-mira-900 leading-snug flex-1">&ldquo;{r['quote']}&rdquo;</blockquote>
          <div class="mt-6 pt-5 border-t border-mira-100">
            <div class="font-medium text-mira-900">{r['name']}</div>
            <div class="text-xs text-mira-600 mt-0.5">{r['meta']}</div>
          </div>
        </article>
        """
        for r in reviews
    )
    testimonial = section(f"""
      <div class="text-center max-w-2xl mx-auto mb-12">
        <p class="uppercase tracking-[0.22em] text-sand-600 text-xs font-semibold" data-i18n="home.reviews.eyebrow">In our guests' words</p>
        <h2 class="font-display text-3xl sm:text-4xl md:text-5xl text-mira-900 leading-tight mt-3" data-i18n="home.reviews.h2">Read by the people who stayed.</h2>
      </div>
      <div class="grid md:grid-cols-3 gap-6">
        {review_cards}
      </div>
      <p class="mt-10 text-center text-sm text-mira-600">
        <a class="underline decoration-sand-400 underline-offset-4 hover:text-sand-600" href="https://www.google.com/search?q=Side+Mira+Palace+Hotel+Evrenseki+reviews" target="_blank" rel="noopener" data-i18n="home.reviews.see_all">Read all 118 Mira Palace reviews on Google →</a>
      </p>
    """, bg="bg-mira-50")
    gallery_teaser = section(f"""
      <div class="flex flex-wrap items-end justify-between gap-6 mb-8">
        <div>{eyebrow('Moments at Mira Palace')}
          {heading('A glimpse of your stay.')}
        </div>
        <a href="{root}gallery.html" class="text-sm font-medium text-mira-700 hover:text-sand-500 inline-flex items-center gap-2"><span data-i18n="home.gallery.full_link">Full gallery</span> <span>→</span></a>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{root}{IMG_POOL}')"></div>
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{root}assets/img/king/king-03.webp')"></div>
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{IMG_DINING}')"></div>
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{root}assets/img/spa/spa-02.webp')"></div>
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{root}assets/img/garden/garden-05.webp')"></div>
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{root}{IMG_BREAKFAST}')"></div>
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{root}assets/img/deluxe/deluxe-02.webp')"></div>
        <div class="aspect-[4/5] bg-cover bg-center rounded bg-mira-700 grid place-items-center text-sand-200 font-display text-xl"><a href="{root}gallery.html" data-i18n="home.gallery.see_all">See all →</a></div>
      </div>
    """, bg="bg-white")
    location_teaser = section(f"""
      <div class="grid lg:grid-cols-2 gap-10 items-center">
        <div>{eyebrow('Where you are')}
          {heading('Evrenseki, between Side and the Taurus Mountains.')}
          <p class="mt-5 text-mira-700 leading-relaxed" data-i18n="home.location.p">Fifteen minutes east of Side's ancient harbour, forty-five minutes from Antalya International Airport, and a seven-minute walk down a cypress-lined lane to <strong>Evrenseki Halk Plajı</strong> — the Blue-Flag public beach on our doorstep. Pool weather from April to November, spa weather all year.</p>
          <div class="mt-6 grid grid-cols-3 gap-4 text-sm">
            <div><div class="font-display text-2xl text-mira-800">700 m</div><div class="text-mira-600" data-i18n="home.location.stat_beach">To Evrenseki beach</div></div>
            <div><div class="font-display text-2xl text-mira-800">12 km</div><div class="text-mira-600" data-i18n="home.location.stat_side">To Side old town</div></div>
            <div><div class="font-display text-2xl text-mira-800">60 km</div><div class="text-mira-600" data-i18n="home.location.stat_airport">To Antalya airport</div></div>
          </div>
          <a href="{root}location.html" class="mt-8 inline-flex items-center gap-2 text-mira-700 font-medium hover:text-sand-500"><span data-i18n="home.location.link">Directions &amp; transfers</span> <span>→</span></a>
        </div>
        <div class="aspect-[4/3] rounded-lg bg-cover bg-center shadow-lux" style="background-image:url('{root}{IMG_BEACH}')"></div>
      </div>
    """, bg="bg-sand-50")
    # R025: Instagram tile grid — six hand-picked posts from @sidemirapalace,
    # each deep-linking to the specific post URL (not the profile).
    # Post shortcodes captured 2026-07-05 from the live Instagram grid.
    # If any specific post gets deleted upstream, the tile still works —
    # Instagram redirects unknown shortcodes back to the profile.
    ig_url = "https://www.instagram.com/sidemirapalace/"
    ig_tiles = [
        # (thumbnail image on disk, alt/caption, IG post shortcode)
        ("assets/img/spa/spa-01.webp",       "Turkish hammam · marble göbek taşı",  "DaSuvMJN7Bm"),
        ("assets/img/king/king-01.webp",     "Signature bedroom · clean lines",     "DaK_8S2N8nA"),
        ("assets/img/king/king-11.webp",     "King Suite room 206 · arrival ritual", "DZ-ivNWtJ7p"),
        ("assets/img/garden/garden-04.webp", "Fresh orange juice · pool detail",     "DZ5HEt0tdfV"),
        ("assets/img/garden/garden-01.webp", "Sun loungers under orange trees",      "DZmqGdANJNU"),
        ("assets/img/garden/garden-02.webp", "Pomegranate tree · Turkish orchard",   "DZURx0St9S3"),
    ]
    ig_grid = "".join(
        f'<a href="https://www.instagram.com/p/{shortcode}/" target="_blank" rel="noopener" '
        f'class="group relative aspect-square block bg-cover bg-center overflow-hidden rounded" '
        f'style="background-image:url(\'{root}{src}\')" aria-label="{alt} — see this post on Instagram">'
        f'<div class="absolute inset-0 bg-mira-900/0 group-hover:bg-mira-900/40 transition flex items-center justify-center">'
        f'<span class="opacity-0 group-hover:opacity-100 text-white text-xs tracking-widest uppercase transition">View post</span>'
        f'</div></a>'
        for src, alt, shortcode in ig_tiles
    )
    instagram = section(f"""
      <div class="flex flex-wrap items-end justify-between gap-6 mb-8">
        <div>
          <p class="uppercase tracking-[0.22em] text-sand-600 text-xs font-semibold" data-i18n="home.instagram.eyebrow">Follow us</p>
          <h2 class="mt-2 font-display text-3xl sm:text-4xl text-mira-900 leading-tight">
            <a href="{ig_url}" target="_blank" rel="noopener" class="hover:text-sand-600 transition">@sidemirapalace</a>
          </h2>
        </div>
        <a href="{ig_url}" target="_blank" rel="noopener" class="text-sm font-medium text-mira-700 hover:text-sand-500 inline-flex items-center gap-2">
          <span data-i18n="home.instagram.follow">Follow on Instagram</span> <span>→</span>
        </a>
      </div>
      <div class="grid grid-cols-3 md:grid-cols-6 gap-1.5">
        {ig_grid}
      </div>
    """, bg="bg-white")

    return h + intro + three + concept_band + testimonial + gallery_teaser + instagram + location_teaser


def about(root: str) -> str:
    # 4-slide garden hero — sweeping, evocative, real Mira Palace photography
    hero_urls = [f"{root}{u}" for u in (IMG_POOL, IMG_GARDEN_2, IMG_GARDEN_3, IMG_GARDEN_4)]
    h = hero_slideshow(
        hero_urls,
        '<span data-i18n="about.hero.kicker">Our story</span>',
        '<span data-i18n="about.hero.h1">Small hotel. Big intent.</span>',
        '<span data-i18n="about.hero.sub">Opened in May 2022 by a family who believed the Turkish Riviera deserved a boutique option between the sprawling resorts and the guesthouses — where service feels personal and the design tells a story.</span>',
        height="70vh",
    )
    story = section(f"""
      <div class="grid lg:grid-cols-12 gap-12">
        <div class="lg:col-span-4">
          <p class="uppercase tracking-[0.22em] text-mira-600 text-xs font-semibold" data-i18n="about.story.eyebrow">Since 2022</p>
          <h2 class="font-display text-3xl sm:text-4xl md:text-5xl text-mira-900 leading-tight" data-i18n="about.story.h2">How Mira Palace began.</h2>
        </div>
        <div class="lg:col-span-8 text-mira-700 leading-relaxed space-y-5 text-lg">
          <p data-i18n="about.story.p1">The property opened its doors in May 2022 after three years of design and construction. Thirty-four suites were built instead of a hundred — because we wanted a kitchen that could cook to order, a pool team that could remember how your family likes its towels, and a front desk that never feels overwhelmed.</p>
          <p data-i18n="about.story.p2">The building sits in Evrenseki, a quiet village east of Side, surrounded by citrus orchards and pomegranate trees. Many of those were there before the hotel was; some have been planted since. The restaurant's winter menu leans heavily on what the orchard gives us — pomegranate molasses, bitter orange marmalade, quince paste, lemon curd.</p>
          <p data-i18n="about.story.p3">We are open twelve months of the year. Summer is pools and beach; winter is the lobby fireplace, the hammam, and the quiet. Both seasons have the same number of smiles at reception.</p>
        </div>
      </div>
    """, bg="bg-white")
    values = section(f"""
      <p class="uppercase tracking-[0.22em] text-sand-600 text-xs font-semibold" data-i18n="about.values.eyebrow">What we care about</p>
      <h2 class="font-display text-3xl sm:text-4xl md:text-5xl text-mira-900 leading-tight" data-i18n="about.values.h2">Three promises, kept quietly.</h2>
      <div class="grid md:grid-cols-3 gap-7 mt-12">
        <div class="p-8 bg-white rounded-lg shadow-lux"><div class="font-display text-3xl text-sand-500">01</div><h3 class="mt-4 font-display text-2xl text-mira-900" data-i18n="about.values.1.title">Small enough to notice</h3><p class="mt-3 text-mira-700 text-sm leading-relaxed" data-i18n="about.values.1.body">Thirty-four suites means the bar knows your drink, the kitchen remembers your allergy, the spa recognises your voice. Not because of a system — because there are only thirty-four of you.</p></div>
        <div class="p-8 bg-white rounded-lg shadow-lux"><div class="font-display text-3xl text-sand-500">02</div><h3 class="mt-4 font-display text-2xl text-mira-900" data-i18n="about.values.2.title">Honest all-inclusive</h3><p class="mt-3 text-mira-700 text-sm leading-relaxed" data-i18n="about.values.2.body">No wristbands, no fine print, no up-sell. The food you see on the menu is the food included. The wine poured at dinner is the same wine poured at lunch. Extras are clearly marked; almost nothing is an extra.</p></div>
        <div class="p-8 bg-white rounded-lg shadow-lux"><div class="font-display text-3xl text-sand-500">03</div><h3 class="mt-4 font-display text-2xl text-mira-900" data-i18n="about.values.3.title">Of the place</h3><p class="mt-3 text-mira-700 text-sm leading-relaxed" data-i18n="about.values.3.body">Furniture from Antalya workshops. Linens from Denizli cotton. Olive oil from a single grove eight kilometres away. Tiles from a ceramicist in Iznik. If we can source it locally, we do.</p></div>
      </div>
    """, bg="bg-mira-50")
    cta = cta_band(
        '<span data-i18n="about.cta.h2">Come and meet us.</span>',
        '<span data-i18n="about.cta.body">Every review we read starts with the same sentence: it felt like a home. Book direct and get a bottle of local wine on arrival, a late check-out when it\'s possible, and a welcome from the owner\'s family.</span>',
        f"{root}contact.html#enquiry",
        '<span data-i18n="about.cta.btn">Plan your stay</span>',
        f"{root}{IMG_POOL}",
    )
    return h + story + values + cta


PAGES = [
    {"path": "index.html", "active": "home",
     "title": "Mira Palace · Boutique all-inclusive on the Turkish Riviera",
     "description": "A 34-suite boutique all-inclusive on the Turkish Riviera. Two pools, a full Turkish hammam, and Evrenseki's Blue-Flag public beach a seven-minute walk down the lane.",
     "body": home},
    {"path": "about.html", "active": "about",
     "title": "About · Mira Palace",
     "description": "The story of Mira Palace — a small Turkish-Riviera hotel opened in 2022 with thirty-four suites and one simple idea.",
     "body": about},
]
