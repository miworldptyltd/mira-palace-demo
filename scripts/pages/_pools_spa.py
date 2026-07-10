from common import hero, hero_slideshow, section, eyebrow, heading, cta_band, SITE_META

# Real Mira Palace photography (copied + resized by Copy-Photos.ps1)
IMG_GARDEN_1 = "assets/img/garden/garden-01.webp"
IMG_GARDEN_2 = "assets/img/garden/garden-02.webp"
IMG_GARDEN_3 = "assets/img/garden/garden-03.webp"
IMG_GARDEN_4 = "assets/img/garden/garden-04.webp"
IMG_SPA_1  = "assets/img/spa/spa-01.webp"   # hammam chamber
IMG_SPA_2  = "assets/img/spa/spa-02.webp"   # steam room
IMG_SPA_3  = "assets/img/spa/spa-03.webp"   # marble göbek taşı
IMG_SPA_4  = "assets/img/spa/spa-04.webp"   # massage suite
IMG_SPA_5  = "assets/img/spa/spa-05.webp"   # scrub / foam
IMG_SPA_6  = "assets/img/spa/spa-06.webp"   # treatment room
IMG_SPA_7  = "assets/img/spa/spa-07.webp"   # sauna
IMG_SPA_8  = "assets/img/spa/spa-08.webp"   # relaxation lounge
IMG_SPA_9  = "assets/img/spa/spa-09.webp"   # aromatherapy room
IMG_SPA_10 = "assets/img/spa/spa-10.webp"   # facility detail
IMG_SPA_11 = "assets/img/spa/spa-11.webp"   # spa entrance
IMG_SPA_12 = "assets/img/spa/spa-12.webp"   # spa detail


def pools(root: str) -> str:
    # R023: was four pools with fabricated dimensions + "private beach club".
    # Reality: TWO pools (outdoor + heated indoor), and the nearest beach is
    # Evrenseki Halk Plajı — a Blue-Flag public beach ~700 m down the lane.
    hero_urls = [f"{root}{u}" for u in (IMG_GARDEN_1, IMG_GARDEN_2, IMG_GARDEN_3, IMG_GARDEN_4)]
    h = hero_slideshow(hero_urls,
             '<span data-i18n="pools.hero.kicker">Pools &amp; Beach</span>',
             '<span data-i18n="pools.hero.h1">Two pools. One sea.<br/>Your choice of shade.</span>',
             '<span data-i18n="pools.hero.sub">A generous outdoor pool through the season, a heated indoor pool for the winter months and cold mornings, and the Blue-Flag public beach at Evrenseki a seven-minute walk down the cypress lane.</span>',
             height="72vh")
    pools_data = [
        ("pools.outdoor", "Outdoor pool",
         "Open through the season, sun loungers on three sides and shaded pergolas around the terrace. Towel service at the pool bar. Kids welcome — the shallow end is gentle."),
        ("pools.indoor", "Indoor pool",
         "Heated year-round for winter guests and early risers who want a lap before breakfast. Adjacent to the spa, so a swim naturally leads to the hammam."),
    ]
    pool_cards = "".join(
        f'<div class="p-7 bg-white rounded-lg shadow-lux"><h3 class="font-display text-2xl text-mira-900" data-i18n="{k}.title">{t}</h3><p class="mt-3 text-mira-700 text-sm leading-relaxed" data-i18n="{k}.body">{d}</p></div>'
        for k, t, d in pools_data
    )
    a = section(f"""
      {eyebrow('Our pools')}
      {heading('One for summer. One for the rest of the year.')}
      <div class="grid md:grid-cols-2 gap-7 mt-10">{pool_cards}</div>
    """, bg="bg-sand-50")
    b = section(f"""
      <div class="grid lg:grid-cols-2 gap-12 items-center">
        <div>{eyebrow('The beach')}
          {heading('Evrenseki Halk Plajı, seven minutes on foot.')}
          <p class="mt-5 text-mira-700 leading-relaxed" data-i18n="pools.beach.p"><strong>Evrenseki Halk Plajı</strong> is the Blue-Flag public beach at the end of the lane — the same soft sandy strip that runs the length of Evrenseki. Turn left out of reception, walk down the cypress-lined path, and you're on the sand in about seven minutes. Sunbeds, umbrellas and a beach kiosk on the front.</p>
          <ul class="mt-6 space-y-3 text-sm text-mira-700">
            <li class="flex gap-3"><span class="text-sand-500">✓</span><span data-i18n="pools.beach.b1">Blue Flag since 2010 — soft, family-friendly sand</span></li>
            <li class="flex gap-3"><span class="text-sand-500">✓</span><span data-i18n="pools.beach.b2">Sunbeds, parasols, showers and changing rooms on the beach (public)</span></li>
            <li class="flex gap-3"><span class="text-sand-500">✓</span><span data-i18n="pools.beach.b3">Gentle shallow entry — good for young children</span></li>
            <li class="flex gap-3"><span class="text-sand-500">✓</span><span data-i18n="pools.beach.b4">Kiosks and cafés along the promenade for drinks and light bites</span></li>
            <li class="flex gap-3"><span class="text-sand-500">✓</span><span data-i18n="pools.beach.b5">Ask reception for a fresh towel to take with you</span></li>
          </ul>
        </div>
        <div class="aspect-[4/5] bg-cover bg-center rounded-lg shadow-lux" style="background-image:url('{root}{IMG_GARDEN_2}')"></div>
      </div>
    """, bg="bg-white")
    c = section(f"""
      <div class="aspect-[16/6] rounded-lg bg-cover bg-center shadow-lux" style="background-image:url('{root}{IMG_GARDEN_3}')"></div>
    """, bg="bg-sand-50")
    cta = cta_band('<span data-i18n="pools.cta.h2">A pool for every mood — and a spa for when the sun is too much.</span>',
                   '<span data-i18n="pools.cta.body">Our Turkish hammam, two saunas, a steam room, a cold plunge and a small but considered treatment menu sit next to the indoor pool.</span>',
                   f"{root}spa.html", '<span data-i18n="pools.cta.btn">Visit the spa</span>', f"{root}{IMG_SPA_1}")
    return h + a + b + c + cta


def spa(root: str) -> str:
    """World-class Spa & Wellness page.

    Structure inspired by Aman Spa, Six Senses, Rosewood Sense, Mandarin
    Oriental spas — the elements that consistently appear on top-tier spa
    sites: cinematic hero, philosophy intro, package cards with clear
    pricing + duration, "included in every visit" reassurance, facilities
    showcase, the ritual journey, direct spa contact.
    """
    m = SITE_META

    # 4-slide hero from the strongest spa photos.
    hero_urls = [f"{root}{u}" for u in (IMG_SPA_1, IMG_SPA_8, IMG_SPA_3, IMG_SPA_11)]
    h = hero_slideshow(
        hero_urls,
        '<span data-i18n="spa.hero.kicker">Spa &amp; Wellness</span>',
        '<span data-i18n="spa.hero.h1">A hammam in the old way. A spa menu in the quiet way.</span>',
        '<span data-i18n="spa.hero.sub">A full Turkish hammam — marble göbek taşı, two saunas, a steam room, a cold plunge, a relaxation lounge — and three curated packages designed around the ritual, not the clock.</span>',
        primary_href=f"{root}spa-book.html",
        primary_label='<span data-i18n="spa.hero.cta">Book a spa session</span>',
        height="76vh",
    )

    # ------------------- Philosophy intro -------------------
    intro = section(f"""
      <div class="grid lg:grid-cols-12 gap-12 items-start">
        <div class="lg:col-span-4">
          <p class="uppercase tracking-[0.22em] text-mira-600 text-xs font-semibold" data-i18n="spa.intro.eyebrow">Our approach</p>
          <h2 class="font-display text-3xl sm:text-4xl md:text-5xl text-mira-900 leading-tight" data-i18n="spa.intro.h2">An old ritual, done properly.</h2>
        </div>
        <div class="lg:col-span-8 text-mira-700 leading-relaxed space-y-4 text-lg">
          <p data-i18n="spa.intro.p1">The Turkish hammam is not a spa treatment. It is a way of being still, together, in warm marble. Everything we do at the Mira Palace Spa is arranged around that idea — the heat is deliberate, the pace is unhurried, and the attendants have been doing this for a decade or more.</p>
          <p data-i18n="spa.intro.p2">We keep the menu short on purpose. Three packages, each built on the same foundation of scrub, foam, sauna, steam and rest — with a treatment of your choice layered in. Nothing is added that isn't going to help.</p>
        </div>
      </div>
    """, bg="bg-white")

    # ------------------- The three packages (from the printed menu PDF) -------------------
    # Kept identical to _spa_book.py to keep names + prices + inclusions in
    # sync across the spa page and the booking page. Each bullet carries an
    # i18n key so the same list translates cleanly per language (R018).
    packages = [
        {
            "key": "classic",
            "name": "Classic",
            "name_i18n": "spa.pkg.classic.name",
            "long_name": "Classic Package",
            "price": "€32",
            "duration": "60 min",
            "img": IMG_SPA_1,
            "tag_i18n": "spa.pkg.classic.tag",
            "tagline": "The introduction — the ritual in its simplest, most honest form.",
            "bullets": [
                ("spa.pkg.b.scrub20",  "20 min Turkish scrub &amp; foam"),
                ("spa.pkg.b.classic40", "40 min classic massage"),
                ("spa.pkg.b.sauna",     "Sauna and steam room access"),
                ("spa.pkg.b.mask",      "Face mask after each massage"),
                ("spa.pkg.b.tea",       "Herbal tea or coffee service"),
                ("spa.pkg.b.shuttle",   "Free shuttle service — round trip"),
            ],
        },
        {
            "key": "relax",
            "name": "Relax",
            "name_i18n": "spa.pkg.relax.name",
            "long_name": "Relax Package",
            "price": "€43",
            "duration": "80 min",
            "img": IMG_SPA_6,
            "tag_i18n": "spa.pkg.relax.tag",
            "tagline": "Longer, deeper, more therapeutic — for those who want to properly unwind.",
            "bullets": [
                ("spa.pkg.b.scrub20",  "20 min Turkish scrub &amp; foam"),
                ("spa.pkg.b.mix60",     "60 min mix therapy"),
                ("spa.pkg.b.sauna",     "Sauna and steam room access"),
                ("spa.pkg.b.mask",      "Face mask after each massage"),
                ("spa.pkg.b.tea",       "Herbal tea or coffee service"),
                ("spa.pkg.b.shuttle",   "Free shuttle service — round trip"),
            ],
        },
        {
            "key": "aroma",
            "name": "Aromatherapy",
            "name_i18n": "spa.pkg.aroma.name",
            "long_name": "Aromatherapy Package",
            "price": "€59",
            "duration": "110 min",
            "img": IMG_SPA_9,
            "tag_i18n": "spa.pkg.aroma.tag",
            "tagline": "Our most indulgent ritual, with a long aromatherapy massage using essential oils.",
            "bullets": [
                ("spa.pkg.b.scrub20",  "20 min Turkish scrub &amp; foam"),
                ("spa.pkg.b.aroma90",   "90 min aromatherapy"),
                ("spa.pkg.b.sauna",     "Sauna and steam room access"),
                ("spa.pkg.b.mask",      "Face mask after each massage"),
                ("spa.pkg.b.oj",        "Freshly squeezed orange juice"),
                ("spa.pkg.b.shuttle",   "Free shuttle service — round trip"),
            ],
        },
    ]

    def _package_card(p, is_middle=False):
        badge = ('<span class="absolute top-4 right-4 bg-sand-300 text-mira-900 text-[10px] font-semibold '
                 'tracking-widest uppercase px-3 py-1 rounded-full" data-i18n="spa.pkgs.most_booked">Most booked</span>' if is_middle else '')
        bullets = "".join(
            f'<li class="flex gap-3 text-sm text-mira-700 leading-relaxed">'
            f'<span class="text-sand-500 shrink-0 mt-0.5">✓</span><span data-i18n="{k}">{item}</span></li>'
            for k, item in p["bullets"]
        )
        highlight_ring = 'ring-2 ring-sand-300 shadow-2xl' if is_middle else 'shadow-lux'
        return f"""
        <article class="relative bg-white rounded-2xl overflow-hidden {highlight_ring} flex flex-col">
          {badge}
          <div class="aspect-[16/10] bg-cover bg-center" style="background-image:url('{root}{p['img']}')"></div>
          <div class="p-8 flex-1 flex flex-col">
            <div class="flex items-baseline justify-between gap-4 mb-1">
              <h3 class="font-display text-3xl text-mira-900 leading-none" data-i18n="{p['name_i18n']}">{p['long_name']}</h3>
              <div class="text-right shrink-0">
                <div class="font-display text-4xl text-mira-900 leading-none">{p['price']}</div>
                <div class="text-[11px] uppercase tracking-widest text-mira-500 mt-1"><span data-i18n="spa.pkgs.pp">per person</span> · {p['duration']}</div>
              </div>
            </div>
            <p class="mt-2 text-sm italic text-sand-600" data-i18n="{p['tag_i18n']}">{p['tagline']}</p>
            <div class="mt-6 pt-6 border-t border-mira-100">
              <div class="text-[10px] uppercase tracking-widest text-mira-500 font-semibold mb-3" data-i18n="spa.pkgs.included">Included</div>
              <ul class="space-y-2">{bullets}</ul>
            </div>
            <a href="{root}spa-book.html?package={p['key']}"
               class="mt-8 w-full inline-flex items-center justify-center gap-2 px-6 py-3.5 bg-mira-800 text-white rounded-full font-medium text-sm hover:bg-mira-900 transition">
              <span data-i18n="spa.pkgs.book_prefix">Book the</span> <span data-i18n="{p['name_i18n']}">{p['long_name']}</span> <span data-i18n="spa.pkgs.book_suffix">package</span> <span>→</span>
            </a>
          </div>
        </article>
        """

    package_cards = "".join(
        _package_card(p, is_middle=(i == 1)) for i, p in enumerate(packages)
    )

    packages_section = section(f"""
      <div class="text-center max-w-2xl mx-auto">
        <p class="uppercase tracking-[0.22em] text-sand-600 text-xs font-semibold" data-i18n="spa.pkgs.eyebrow">Spa packages</p>
        <h2 class="font-display text-3xl sm:text-4xl md:text-5xl text-mira-900 leading-tight" data-i18n="spa.pkgs.h2">Three ways to spend an afternoon.</h2>
        <p class="mt-5 text-mira-700 leading-relaxed" data-i18n="spa.pkgs.lead">
          Every package includes the hammam ritual (scrub &amp; foam), sauna, steam, herbal tea, and our complimentary shuttle both ways from the hotel. Pick the layer that suits you.
        </p>
      </div>
      <div class="grid md:grid-cols-3 gap-7 mt-14">{package_cards}</div>
      <p class="mt-8 text-center text-xs text-mira-500 italic">
        <span data-i18n="spa.pkgs.foot">Prices shown in Euro. Turkish Lira and USD available at the reception desk. Couples arrangements &amp; private hammam sessions available on request — please call</span>
        <a class="underline hover:text-sand-500" href="tel:{m['spa_phone_tel']}">{m['spa_phone_display']}</a>.
      </p>
    """, bg="bg-sand-50")

    # ------------------- Included in every visit (reassurance) -------------------
    included_every = section(f"""
      <div class="max-w-5xl mx-auto text-center">
        <p class="uppercase tracking-[0.22em] text-mira-600 text-xs font-semibold" data-i18n="spa.every.eyebrow">In every visit</p>
        <h2 class="font-display text-3xl sm:text-4xl md:text-5xl text-mira-900 leading-tight" data-i18n="spa.every.h2">What you always get.</h2>
        <p class="mt-5 text-mira-700 leading-relaxed" data-i18n="spa.every.lead">
          Regardless of the package you pick — these are on the house, every time.
        </p>
        <div class="mt-12 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-6">
          <div class="text-center">
            <div class="text-4xl">🧖</div>
            <div class="mt-2 font-display text-lg text-mira-900" data-i18n="spa.every.hammam.t">Hammam access</div>
            <div class="text-xs text-mira-600 mt-1" data-i18n="spa.every.hammam.s">Marble chamber, göbek taşı</div>
          </div>
          <div class="text-center">
            <div class="text-4xl">🔥</div>
            <div class="mt-2 font-display text-lg text-mira-900" data-i18n="spa.every.sauna.t">Two saunas</div>
            <div class="text-xs text-mira-600 mt-1" data-i18n="spa.every.sauna.s">Dry + aroma</div>
          </div>
          <div class="text-center">
            <div class="text-4xl">💨</div>
            <div class="mt-2 font-display text-lg text-mira-900" data-i18n="spa.every.steam.t">Steam room</div>
            <div class="text-xs text-mira-600 mt-1" data-i18n="spa.every.steam.s">Anatolian herbs</div>
          </div>
          <div class="text-center">
            <div class="text-4xl">🧊</div>
            <div class="mt-2 font-display text-lg text-mira-900" data-i18n="spa.every.plunge.t">Cold plunge</div>
            <div class="text-xs text-mira-600 mt-1" data-i18n="spa.every.plunge.s">12 °C — brief &amp; sharp</div>
          </div>
          <div class="text-center">
            <div class="text-4xl">🍵</div>
            <div class="mt-2 font-display text-lg text-mira-900" data-i18n="spa.every.tea.t">Herbal tea</div>
            <div class="text-xs text-mira-600 mt-1" data-i18n="spa.every.tea.s">Or freshly-pressed juice</div>
          </div>
          <div class="text-center">
            <div class="text-4xl">🚐</div>
            <div class="mt-2 font-display text-lg text-mira-900" data-i18n="spa.every.shuttle.t">Shuttle service</div>
            <div class="text-xs text-mira-600 mt-1" data-i18n="spa.every.shuttle.s">From your room, both ways</div>
          </div>
        </div>
      </div>
    """, bg="bg-white")

    # ------------------- Facilities showcase -------------------
    facilities = [
        ("spa.fac.hammam.t", "Turkish hammam",
         "spa.fac.hammam.d", "Marble chamber heated from underneath, round göbek taşı in the centre, cold-water basins along the walls. Peştemal-wrapped attendants with over a decade of experience.",
         IMG_SPA_1),
        ("spa.fac.saunas.t", "Two saunas",
         "spa.fac.saunas.d", "A traditional dry sauna and an aroma sauna scented lightly with eucalyptus. Both quiet, both timed at 75-85 °C — hot enough to matter, gentle enough to stay.",
         IMG_SPA_7),
        ("spa.fac.steam.t", "Steam room",
         "spa.fac.steam.d", "Anatolian herbs infused into the steam — pine, sage, lavender rotated through the week. 100% humidity, ~45 °C.",
         IMG_SPA_2),
        ("spa.fac.plunge.t", "Cold plunge",
         "spa.fac.plunge.d", "12 °C. The short sharp contrast that people come to Turkish hammams for in the first place. Twenty seconds is plenty.",
         IMG_SPA_12),
        ("spa.fac.lounge.t", "Relaxation lounge",
         "spa.fac.lounge.d", "A dim, softly-heated room with reclining chaises, fresh mint water, and stacks of fresh towels. The place to land after a hammam ritual.",
         IMG_SPA_8),
        ("spa.fac.rooms.t", "Treatment rooms",
         "spa.fac.rooms.d", "Six rooms — two single, two double, plus specialist rooms for wet-room body scrubs and hammam-side scrub-and-massage combinations. Heated tables, quiet.",
         IMG_SPA_4),
    ]
    fac_cards = "".join(
        f'<article class="bg-white rounded-lg overflow-hidden shadow-lux group">'
        f'  <div class="aspect-[4/3] bg-cover bg-center transition duration-500 group-hover:scale-[1.03]" style="background-image:url(\'{root}{img}\')"></div>'
        f'  <div class="p-6">'
        f'    <h3 class="font-display text-xl text-mira-900" data-i18n="{ti}">{title}</h3>'
        f'    <p class="mt-2 text-sm text-mira-700 leading-relaxed" data-i18n="{bi}">{body}</p>'
        f'  </div>'
        f'</article>'
        for ti, title, bi, body, img in facilities
    )
    facilities_section = section(f"""
      <p class="uppercase tracking-[0.22em] text-mira-600 text-xs font-semibold" data-i18n="spa.fac.eyebrow">Facilities</p>
      <h2 class="font-display text-3xl sm:text-4xl md:text-5xl text-mira-900 leading-tight" data-i18n="spa.fac.h2">Everything under one roof.</h2>
      <p class="mt-5 max-w-2xl text-mira-700 leading-relaxed" data-i18n="spa.fac.lead">
        The spa is on the ground floor of the main building, adjoining the indoor pool. Enter from reception in a robe and slippers — we'll take you the rest of the way.
      </p>
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-7 mt-10">{fac_cards}</div>
    """, bg="bg-sand-50")

    # ------------------- The ritual journey (5 stages) -------------------
    journey = section(f"""
      <div class="grid lg:grid-cols-2 gap-16 items-center">
        <div class="aspect-[4/5] bg-cover bg-center rounded-lg shadow-lux" style="background-image:url('{root}{IMG_SPA_3}')"></div>
        <div>
          <p class="uppercase tracking-[0.22em] text-mira-600 text-xs font-semibold" data-i18n="spa.rit.eyebrow">The hammam ritual</p>
          <h3 class="font-display text-2xl sm:text-3xl text-mira-900 leading-tight" data-i18n="spa.rit.h2">Five stages, roughly ninety minutes.</h3>
          <ol class="mt-8 space-y-6 text-mira-700">
            <li class="flex gap-5">
              <span class="font-display text-3xl text-sand-500 shrink-0 leading-none w-8">1</span>
              <div>
                <div class="font-medium text-mira-900" data-i18n="spa.rit.1.t">Warm.</div>
                <p class="text-sm mt-1" data-i18n="spa.rit.1.d">Fifteen minutes on the heated marble, lying on a cotton peştemal. The room is quiet; the heat is soft but thorough.</p>
              </div>
            </li>
            <li class="flex gap-5">
              <span class="font-display text-3xl text-sand-500 shrink-0 leading-none w-8">2</span>
              <div>
                <div class="font-medium text-mira-900" data-i18n="spa.rit.2.t">Exfoliate.</div>
                <p class="text-sm mt-1" data-i18n="spa.rit.2.d">An attendant works with a kese glove — the Turkish coarse silk mitt. Nothing stays that wasn't going to.</p>
              </div>
            </li>
            <li class="flex gap-5">
              <span class="font-display text-3xl text-sand-500 shrink-0 leading-none w-8">3</span>
              <div>
                <div class="font-medium text-mira-900" data-i18n="spa.rit.3.t">Foam.</div>
                <p class="text-sm mt-1" data-i18n="spa.rit.3.d">A soap-cloud bath, olive-oil soap whipped to meringue, poured over you in waves.</p>
              </div>
            </li>
            <li class="flex gap-5">
              <span class="font-display text-3xl text-sand-500 shrink-0 leading-none w-8">4</span>
              <div>
                <div class="font-medium text-mira-900" data-i18n="spa.rit.4.t">Rinse.</div>
                <p class="text-sm mt-1" data-i18n="spa.rit.4.d">Warm then cooler, in the marble basins.</p>
              </div>
            </li>
            <li class="flex gap-5">
              <span class="font-display text-3xl text-sand-500 shrink-0 leading-none w-8">5</span>
              <div>
                <div class="font-medium text-mira-900" data-i18n="spa.rit.5.t">Rest.</div>
                <p class="text-sm mt-1" data-i18n="spa.rit.5.d">Wrapped in a fresh dry peştemal, laid on a chaise, offered a mint tea. Fifteen to thirty minutes — stay as long as you want.</p>
              </div>
            </li>
          </ol>
        </div>
      </div>
    """, bg="bg-white")

    # ------------------- Before you visit (etiquette / what to bring) -------------------
    etiquette = section(f"""
      <div class="max-w-4xl mx-auto">
        <p class="uppercase tracking-[0.22em] text-mira-600 text-xs font-semibold" data-i18n="spa.etq.eyebrow">Before you visit</p>
        <h3 class="font-display text-2xl sm:text-3xl text-mira-900 leading-tight" data-i18n="spa.etq.h2">A few small things to know.</h3>
        <div class="mt-10 grid md:grid-cols-2 gap-x-12 gap-y-6 text-mira-700 text-sm leading-relaxed">
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900" data-i18n="spa.etq.1.t">Robe, slippers &amp; towels are provided.</span> <span data-i18n="spa.etq.1.d">Come from your room in a robe; we'll do the rest.</span></div></div>
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900" data-i18n="spa.etq.2.t">Wear a swimsuit if you prefer.</span> <span data-i18n="spa.etq.2.d">In the hammam and pool areas, swimwear is normal; disposable underwear is available for treatments.</span></div></div>
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900" data-i18n="spa.etq.3.t">Arrive 15 minutes early.</span> <span data-i18n="spa.etq.3.d">The spa reception has cold herbal water and a quiet lounge to change out of the outside world.</span></div></div>
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900" data-i18n="spa.etq.4.t">Phones stay in the locker.</span> <span data-i18n="spa.etq.4.d">The spa is a quiet zone.</span></div></div>
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900" data-i18n="spa.etq.5.t">Tell us about pregnancy, injury or allergy at booking.</span> <span data-i18n="spa.etq.5.d">We adjust every ritual to your body.</span></div></div>
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900" data-i18n="spa.etq.6.t">Cancellations 24 hours before.</span> <span data-i18n="spa.etq.6.d">Same-day changes are fine — text the WhatsApp on the sidebar.</span></div></div>
        </div>
      </div>
    """, bg="bg-sand-50")

    # ------------------- Direct spa contact block -------------------
    contact = section(f"""
      <div class="max-w-5xl mx-auto bg-mira-900 text-white rounded-2xl overflow-hidden shadow-lux">
        <div class="grid lg:grid-cols-2 items-stretch">
          <div class="aspect-[4/3] lg:aspect-auto bg-cover bg-center" style="background-image:url('{root}{IMG_SPA_11}')"></div>
          <div class="p-10 lg:p-12">
            <div class="text-[10px] uppercase tracking-widest text-sand-300 font-semibold" data-i18n="spa.contact.eyebrow">Reserve your session</div>
            <h3 class="font-display text-4xl mt-3" data-i18n="spa.contact.h3">The spa desk answers directly.</h3>
            <p class="mt-5 text-white/80 leading-relaxed" data-i18n="spa.contact.p">
              Book online in ninety seconds, or call the spa reception straight — different number to the front desk so we can dispatch without tying up the main line.
            </p>
            <div class="mt-8 space-y-4">
              <a href="tel:{m['spa_phone_tel']}" class="flex items-center gap-4 group">
                <div class="w-12 h-12 rounded-full bg-white/10 grid place-items-center text-2xl">☎</div>
                <div>
                  <div class="text-xs uppercase tracking-widest text-sand-300" data-i18n="spa.contact.reception">Spa reception</div>
                  <div class="font-display text-2xl group-hover:text-sand-200 transition">{m['spa_phone_display']}</div>
                </div>
              </a>
              <a href="{m['spa_whatsapp']}" rel="noopener" class="flex items-center gap-4 group">
                <div class="w-12 h-12 rounded-full bg-white/10 grid place-items-center text-2xl">💬</div>
                <div>
                  <div class="text-xs uppercase tracking-widest text-sand-300" data-i18n="spa.contact.whatsapp_label">WhatsApp</div>
                  <div class="font-display text-2xl group-hover:text-sand-200 transition" data-i18n="spa.contact.whatsapp_v">Same number, faster</div>
                </div>
              </a>
              <a href="{m['spa_instagram_url']}" rel="noopener" class="flex items-center gap-4 group">
                <div class="w-12 h-12 rounded-full bg-white/10 grid place-items-center text-2xl">📷</div>
                <div>
                  <div class="text-xs uppercase tracking-widest text-sand-300" data-i18n="spa.contact.instagram">Instagram</div>
                  <div class="font-display text-2xl group-hover:text-sand-200 transition">@{m['spa_instagram_handle'].lower()}</div>
                </div>
              </a>
            </div>
            <a href="{root}spa-book.html" class="mt-10 inline-flex items-center gap-3 px-8 py-4 bg-sand-300 text-mira-900 rounded-full font-semibold hover:bg-sand-200 transition">
              <span data-i18n="spa.contact.cta">Book online</span> <span>→</span>
            </a>
          </div>
        </div>
      </div>
    """, bg="bg-white")

    return h + intro + packages_section + included_every + facilities_section + journey + etiquette + contact


def spa_treatments(root: str) -> str:
    menu = [
        ("Hammam rituals", [
            ("Classic hammam ritual", "90 min", "€90", "Heat, kese exfoliation, foam bath, rinse, rest."),
            ("Signature Mira ritual", "120 min", "€140", "Classic hammam + 30-minute aromatherapy massage."),
            ("Royal hammam", "150 min", "€180", "Hammam + full-body oil massage + facial cleanse."),
            ("Couples hammam", "90 min", "€170 per couple", "In the private hammam room — reserve in advance."),
        ]),
        ("Massage", [
            ("Relaxation massage", "60 min", "€75", "Warm oil, long strokes, gentle pressure."),
            ("Deep tissue", "60 min", "€90", "Firmer, specific, for shoulders, back, legs."),
            ("Hot stone", "75 min", "€100", "Basalt stones warmed to body temperature."),
            ("Four-hand ritual", "60 min", "€150", "Two therapists, perfectly synchronised."),
        ]),
        ("Facials", [
            ("Mediterranean glow", "50 min", "€70", "Cleanse, exfoliate, mask, massage — olive-leaf and pomegranate."),
            ("Age-reset facial", "75 min", "€110", "Retinol-free but effective; collagen mask, gua sha lift."),
            ("Men’s deep-clean", "45 min", "€60", "Steam, extraction, cool mask, soothing balm."),
        ]),
        ("Body", [
            ("Salt &amp; citrus body scrub", "45 min", "€60", "In the wet room. Aegean sea salt, orange, bergamot."),
            ("Mud wrap", "60 min", "€80", "Mineral-rich wrap, scalp massage while you steam."),
            ("Post-sun soothing", "45 min", "€55", "After-sun gel, aloe, cold stones."),
        ]),
    ]
    blocks = ""
    for sec_t, rows in menu:
        row_html = "".join(
            f'<tr class="border-t border-mira-200"><td class="py-4 pr-6 align-top"><div class="font-medium text-mira-900">{name}</div><div class="mt-1 text-xs text-mira-600">{desc}</div></td><td class="py-4 px-3 text-sm text-mira-700 whitespace-nowrap align-top">{dur}</td><td class="py-4 pl-3 text-sm font-medium text-mira-900 whitespace-nowrap align-top text-right">{price}</td></tr>'
            for name, dur, price, desc in rows
        )
        blocks += f'<div class="mt-12 first:mt-0"><h3 class="font-display text-2xl text-mira-900">{sec_t}</h3><table class="w-full mt-4"><tbody>{row_html}</tbody></table></div>'

    h = hero(f"{root}{IMG_SPA_6}",
             '<span data-i18n="spat.hero.kicker">Spa · Treatments</span>',
             '<span data-i18n="spat.hero.h1">The treatment menu.</span>',
             '<span data-i18n="spat.hero.sub">Massage, facial, body work, hammam rituals. Prices in Euro. Hammam and facility access are included in your stay; treatments below are priced per serve and can be booked at the spa reception or via WhatsApp.</span>',
             height="60vh")
    body = section(f"""
      {blocks}
      <p class="mt-10 text-xs text-mira-500 italic" data-i18n="spat.foot">Prices illustrative for the demo site. Real pricing will be supplied by the hotel on content hand-off. A 24-hour cancellation policy applies; a no-show is charged at 50 per cent.</p>
      <a href="{root}contact.html#enquiry" class="mt-8 inline-flex items-center px-6 py-3 bg-mira-700 text-white rounded-full font-medium hover:bg-mira-800" data-i18n="spat.book_cta">Book a treatment</a>
    """, bg="bg-white")
    return h + body


PAGES = [
    # Pools & Beach page retired in R005 — owner removed it from the nav.
    # Pools content now surfaces on the home page + dining/pool-bar page.
    {"path": "spa.html", "active": "spa",
     "title": "Spa & Wellness · Mira Palace",
     "description": "Turkish hammam, saunas, steam room, cold plunge, fitness studio, and a treatment menu of massage, facial and body work.",
     "body": spa},
    {"path": "spa-treatments.html", "active": "spa",
     "title": "Spa Treatments · Mira Palace",
     "description": "The Mira Palace spa treatment menu — hammam rituals, massage, facial, and body therapies.",
     "body": spa_treatments},
]
