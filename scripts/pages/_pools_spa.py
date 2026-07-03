from common import hero, hero_slideshow, section, eyebrow, heading, cta_band, SITE_META

# Real Mira Palace photography (copied + resized by Copy-Photos.ps1)
IMG_GARDEN_1 = "assets/img/garden/garden-01.jpg"
IMG_GARDEN_2 = "assets/img/garden/garden-02.jpg"
IMG_GARDEN_3 = "assets/img/garden/garden-03.jpg"
IMG_GARDEN_4 = "assets/img/garden/garden-04.jpg"
IMG_SPA_1  = "assets/img/spa/spa-01.jpg"   # hammam chamber
IMG_SPA_2  = "assets/img/spa/spa-02.jpg"   # steam room
IMG_SPA_3  = "assets/img/spa/spa-03.jpg"   # marble göbek taşı
IMG_SPA_4  = "assets/img/spa/spa-04.jpg"   # massage suite
IMG_SPA_5  = "assets/img/spa/spa-05.jpg"   # scrub / foam
IMG_SPA_6  = "assets/img/spa/spa-06.jpg"   # treatment room
IMG_SPA_7  = "assets/img/spa/spa-07.jpg"   # sauna
IMG_SPA_8  = "assets/img/spa/spa-08.jpg"   # relaxation lounge
IMG_SPA_9  = "assets/img/spa/spa-09.jpg"   # aromatherapy room
IMG_SPA_10 = "assets/img/spa/spa-10.jpg"   # facility detail
IMG_SPA_11 = "assets/img/spa/spa-11.jpg"   # spa entrance
IMG_SPA_12 = "assets/img/spa/spa-12.jpg"   # spa detail


def pools(root: str) -> str:
    # 4-slide hero from the garden folder
    hero_urls = [f"{root}{u}" for u in (IMG_GARDEN_1, IMG_GARDEN_2, IMG_GARDEN_3, IMG_GARDEN_4)]
    h = hero_slideshow(hero_urls, "Pools & Beach",
             "Four pools. One sea.<br/>Your choice of shade.",
             "A main pool for families, an adults-only infinity pool, a heated indoor pool for mornings and winter, and a children's pool with its own small slide. Plus 600 m of shoreline we've made easy to reach.",
             height="72vh")
    pools_data = [
        ("Main pool", "25 × 12 m, 1.3–1.6 m deep. Open 08:00–19:00. Sun loungers on three sides, shaded pergola at the west end. Towel service at the pool bar."),
        ("Infinity pool (adults only)", "A quieter 18 × 8 m pool raised above the orchard, with sun loungers and private cabanas on request. Open 09:00–19:00. Minimum age 16."),
        ("Indoor pool", "14 × 7 m, heated year-round. Open 07:00–22:00 — ideal for morning swims before breakfast and for winter guests. Adjacent to the spa."),
        ("Children's pool", "0.4 m deep with a gentle slide. A team member is at the pool 10:00–17:00. Parents welcome; shallow enough to sit in."),
    ]
    pool_cards = "".join(
        f'<div class="p-7 bg-white rounded-lg shadow-lux"><h3 class="font-display text-2xl text-mira-900">{t}</h3><p class="mt-3 text-mira-700 text-sm leading-relaxed">{d}</p></div>'
        for t, d in pools_data
    )
    a = section(f"""
      {eyebrow('Our pools')}
      {heading('Four to choose from.')}
      <div class="grid md:grid-cols-2 gap-7 mt-10">{pool_cards}</div>
    """, bg="bg-sand-50")
    b = section(f"""
      <div class="grid lg:grid-cols-2 gap-12 items-center">
        <div>{eyebrow('The beach')}
          {heading('600 metres from your room.')}
          <p class="mt-5 text-mira-700 leading-relaxed">Our private beach club sits at the end of a cypress-lined lane, ten minutes on foot from the hotel or three minutes on the shuttle buggy that runs every thirty minutes. Sun loungers and parasols are reserved for Mira Palace guests; fresh towels are at the cabana.</p>
          <ul class="mt-6 space-y-3 text-sm text-mira-700">
            <li class="flex gap-3"><span class="text-sand-500">✓</span>Lifeguards on duty 10:00–18:00 in season</li>
            <li class="flex gap-3"><span class="text-sand-500">✓</span>Showers, changing rooms, toilets, small bar</li>
            <li class="flex gap-3"><span class="text-sand-500">✓</span>Light lunch served 12:30–15:00 (club sandwich, grilled fish, salads)</li>
            <li class="flex gap-3"><span class="text-sand-500">✓</span>SUPs, paddles, kayaks, snorkel gear — free to use</li>
            <li class="flex gap-3"><span class="text-sand-500">✓</span>Watersports (jet-ski, banana boat) operated by third-party at surcharge</li>
          </ul>
        </div>
        <div class="aspect-[4/5] bg-cover bg-center rounded-lg shadow-lux" style="background-image:url('{root}{IMG_GARDEN_2}')"></div>
      </div>
    """, bg="bg-white")
    c = section(f"""
      <div class="aspect-[16/6] rounded-lg bg-cover bg-center shadow-lux" style="background-image:url('{root}{IMG_GARDEN_3}')"></div>
    """, bg="bg-sand-50")
    cta = cta_band("A pool for every mood — and a spa for when the sun is too much.",
                   "Our Turkish hammam, two saunas, a steam room, a cold plunge and a small but considered treatment menu sit next to the indoor pool.",
                   f"{root}spa.html", "Visit the spa", f"{root}{IMG_SPA_1}")
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
        "Spa &amp; Wellness",
        "A hammam in the old way.<br/>A spa menu in the quiet way.",
        "A full Turkish hammam — marble göbek taşı, two saunas, a steam room, a cold plunge, a relaxation lounge — and three curated packages designed around the ritual, not the clock.",
        primary_href=f"{root}spa-book.html",
        primary_label="Book a spa session",
        height="76vh",
    )

    # ------------------- Philosophy intro -------------------
    intro = section(f"""
      <div class="grid lg:grid-cols-12 gap-12 items-start">
        <div class="lg:col-span-4">
          {eyebrow('Our approach')}
          {heading('An old ritual, done properly.')}
        </div>
        <div class="lg:col-span-8 text-mira-700 leading-relaxed space-y-4 text-lg">
          <p>The Turkish hammam is not a spa treatment. It is a way of being still, together, in warm marble. Everything we do at the Mira Palace Spa is arranged around that idea — the heat is deliberate, the pace is unhurried, and the attendants have been doing this for a decade or more.</p>
          <p>We keep the menu short on purpose. Three packages, each built on the same foundation of scrub, foam, sauna, steam and rest — with a treatment of your choice layered in. Nothing is added that isn't going to help.</p>
        </div>
      </div>
    """, bg="bg-white")

    # ------------------- The three packages (from the printed menu PDF) -------------------
    # Kept identical to _spa_book.py to keep names + prices + inclusions in
    # sync across the spa page and the booking page.
    packages = [
        {
            "key": "classic",
            "name": "Classic",
            "long_name": "Classic Package",
            "price": "€32",
            "duration": "60 min",
            "img": IMG_SPA_1,
            "tagline": "The introduction — the ritual in its simplest, most honest form.",
            "included": [
                "20 min Turkish scrub &amp; foam",
                "40 min classic massage",
                "Sauna and steam room access",
                "Face mask after each massage",
                "Herbal tea or coffee service",
                "Free shuttle service — round trip",
            ],
        },
        {
            "key": "relax",
            "name": "Relax",
            "long_name": "Relax Package",
            "price": "€43",
            "duration": "80 min",
            "img": IMG_SPA_6,
            "tagline": "Longer, deeper, more therapeutic — for those who want to properly unwind.",
            "included": [
                "20 min Turkish scrub &amp; foam",
                "60 min mix therapy",
                "Sauna and steam room access",
                "Face mask after each massage",
                "Herbal tea or coffee service",
                "Free shuttle service — round trip",
            ],
        },
        {
            "key": "aroma",
            "name": "Aromatherapy",
            "long_name": "Aromatherapy Package",
            "price": "€59",
            "duration": "110 min",
            "img": IMG_SPA_9,
            "tagline": "Our most indulgent ritual, with a long aromatherapy massage using essential oils.",
            "included": [
                "20 min Turkish scrub &amp; foam",
                "90 min aromatherapy",
                "Sauna and steam room access",
                "Face mask after each massage",
                "Freshly squeezed orange juice",
                "Free shuttle service — round trip",
            ],
        },
    ]

    def _package_card(p, is_middle=False):
        badge = ('<span class="absolute top-4 right-4 bg-sand-300 text-mira-900 text-[10px] font-semibold '
                 'tracking-widest uppercase px-3 py-1 rounded-full">Most booked</span>' if is_middle else '')
        bullets = "".join(
            f'<li class="flex gap-3 text-sm text-mira-700 leading-relaxed">'
            f'<span class="text-sand-500 shrink-0 mt-0.5">✓</span><span>{item}</span></li>'
            for item in p["included"]
        )
        highlight_ring = 'ring-2 ring-sand-300 shadow-2xl' if is_middle else 'shadow-lux'
        return f"""
        <article class="relative bg-white rounded-2xl overflow-hidden {highlight_ring} flex flex-col">
          {badge}
          <div class="aspect-[16/10] bg-cover bg-center" style="background-image:url('{root}{p['img']}')"></div>
          <div class="p-8 flex-1 flex flex-col">
            <div class="flex items-baseline justify-between gap-4 mb-1">
              <h3 class="font-display text-3xl text-mira-900 leading-none">{p['long_name']}</h3>
              <div class="text-right shrink-0">
                <div class="font-display text-4xl text-mira-900 leading-none">{p['price']}</div>
                <div class="text-[11px] uppercase tracking-widest text-mira-500 mt-1">per person · {p['duration']}</div>
              </div>
            </div>
            <p class="mt-2 text-sm italic text-sand-600">{p['tagline']}</p>
            <div class="mt-6 pt-6 border-t border-mira-100">
              <div class="text-[10px] uppercase tracking-widest text-mira-500 font-semibold mb-3">Included</div>
              <ul class="space-y-2">{bullets}</ul>
            </div>
            <a href="{root}spa-book.html?package={p['key']}"
               class="mt-8 w-full inline-flex items-center justify-center gap-2 px-6 py-3.5 bg-mira-800 text-white rounded-full font-medium text-sm hover:bg-mira-900 transition">
              Book the {p['name']} package <span>→</span>
            </a>
          </div>
        </article>
        """

    package_cards = "".join(
        _package_card(p, is_middle=(i == 1)) for i, p in enumerate(packages)
    )

    packages_section = section(f"""
      <div class="text-center max-w-2xl mx-auto">
        {eyebrow('Spa packages', 'text-sand-600')}
        {heading('Three ways to spend an afternoon.')}
        <p class="mt-5 text-mira-700 leading-relaxed">
          Every package includes the hammam ritual (scrub &amp; foam), sauna, steam, herbal tea, and our complimentary shuttle both ways from the hotel. Pick the layer that suits you.
        </p>
      </div>
      <div class="grid md:grid-cols-3 gap-7 mt-14">{package_cards}</div>
      <p class="mt-8 text-center text-xs text-mira-500 italic">
        Prices shown in Euro. Turkish Lira and USD available at the reception desk.
        Couples arrangements &amp; private hammam sessions available on request —
        please call <a class="underline hover:text-sand-500" href="tel:{m['spa_phone_tel']}">{m['spa_phone_display']}</a>.
      </p>
    """, bg="bg-sand-50")

    # ------------------- Included in every visit (reassurance) -------------------
    included_every = section(f"""
      <div class="max-w-5xl mx-auto text-center">
        {eyebrow('In every visit')}
        {heading('What you always get.')}
        <p class="mt-5 text-mira-700 leading-relaxed">
          Regardless of the package you pick — these are on the house, every time.
        </p>
        <div class="mt-12 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-6">
          <div class="text-center">
            <div class="text-4xl">🧖</div>
            <div class="mt-2 font-display text-lg text-mira-900">Hammam access</div>
            <div class="text-xs text-mira-600 mt-1">Marble chamber, göbek taşı</div>
          </div>
          <div class="text-center">
            <div class="text-4xl">🔥</div>
            <div class="mt-2 font-display text-lg text-mira-900">Two saunas</div>
            <div class="text-xs text-mira-600 mt-1">Dry + aroma</div>
          </div>
          <div class="text-center">
            <div class="text-4xl">💨</div>
            <div class="mt-2 font-display text-lg text-mira-900">Steam room</div>
            <div class="text-xs text-mira-600 mt-1">Anatolian herbs</div>
          </div>
          <div class="text-center">
            <div class="text-4xl">🧊</div>
            <div class="mt-2 font-display text-lg text-mira-900">Cold plunge</div>
            <div class="text-xs text-mira-600 mt-1">12 °C — brief &amp; sharp</div>
          </div>
          <div class="text-center">
            <div class="text-4xl">🍵</div>
            <div class="mt-2 font-display text-lg text-mira-900">Herbal tea</div>
            <div class="text-xs text-mira-600 mt-1">Or freshly-pressed juice</div>
          </div>
          <div class="text-center">
            <div class="text-4xl">🚐</div>
            <div class="mt-2 font-display text-lg text-mira-900">Shuttle service</div>
            <div class="text-xs text-mira-600 mt-1">From your room, both ways</div>
          </div>
        </div>
      </div>
    """, bg="bg-white")

    # ------------------- Facilities showcase -------------------
    facilities = [
        ("Turkish hammam",
         "Marble chamber heated from underneath, round göbek taşı in the centre, cold-water basins along the walls. Peştemal-wrapped attendants with over a decade of experience.",
         IMG_SPA_1),
        ("Two saunas",
         "A traditional dry sauna and an aroma sauna scented lightly with eucalyptus. Both quiet, both timed at 75-85 °C — hot enough to matter, gentle enough to stay.",
         IMG_SPA_7),
        ("Steam room",
         "Anatolian herbs infused into the steam — pine, sage, lavender rotated through the week. 100% humidity, ~45 °C.",
         IMG_SPA_2),
        ("Cold plunge",
         "12 °C. The short sharp contrast that people come to Turkish hammams for in the first place. Twenty seconds is plenty.",
         IMG_SPA_12),
        ("Relaxation lounge",
         "A dim, softly-heated room with reclining chaises, fresh mint water, and stacks of fresh towels. The place to land after a hammam ritual.",
         IMG_SPA_8),
        ("Treatment rooms",
         "Six rooms — two single, two double, plus specialist rooms for wet-room body scrubs and hammam-side scrub-and-massage combinations. Heated tables, quiet.",
         IMG_SPA_4),
    ]
    fac_cards = "".join(
        f'<article class="bg-white rounded-lg overflow-hidden shadow-lux group">'
        f'  <div class="aspect-[4/3] bg-cover bg-center transition duration-500 group-hover:scale-[1.03]" style="background-image:url(\'{root}{img}\')"></div>'
        f'  <div class="p-6">'
        f'    <h3 class="font-display text-xl text-mira-900">{title}</h3>'
        f'    <p class="mt-2 text-sm text-mira-700 leading-relaxed">{body}</p>'
        f'  </div>'
        f'</article>'
        for title, body, img in facilities
    )
    facilities_section = section(f"""
      {eyebrow('Facilities')}
      {heading('Everything under one roof.')}
      <p class="mt-5 max-w-2xl text-mira-700 leading-relaxed">
        The spa is on the ground floor of the main building, adjoining the indoor pool. Enter from reception in a robe and slippers — we'll take you the rest of the way.
      </p>
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-7 mt-10">{fac_cards}</div>
    """, bg="bg-sand-50")

    # ------------------- The ritual journey (5 stages) -------------------
    journey = section(f"""
      <div class="grid lg:grid-cols-2 gap-16 items-center">
        <div class="aspect-[4/5] bg-cover bg-center rounded-lg shadow-lux" style="background-image:url('{root}{IMG_SPA_3}')"></div>
        <div>
          {eyebrow('The hammam ritual')}
          {heading('Five stages, roughly ninety minutes.', 3)}
          <ol class="mt-8 space-y-6 text-mira-700">
            <li class="flex gap-5">
              <span class="font-display text-3xl text-sand-500 shrink-0 leading-none w-8">1</span>
              <div>
                <div class="font-medium text-mira-900">Warm.</div>
                <p class="text-sm mt-1">Fifteen minutes on the heated marble, lying on a cotton peştemal. The room is quiet; the heat is soft but thorough.</p>
              </div>
            </li>
            <li class="flex gap-5">
              <span class="font-display text-3xl text-sand-500 shrink-0 leading-none w-8">2</span>
              <div>
                <div class="font-medium text-mira-900">Exfoliate.</div>
                <p class="text-sm mt-1">An attendant works with a kese glove — the Turkish coarse silk mitt. Nothing stays that wasn't going to.</p>
              </div>
            </li>
            <li class="flex gap-5">
              <span class="font-display text-3xl text-sand-500 shrink-0 leading-none w-8">3</span>
              <div>
                <div class="font-medium text-mira-900">Foam.</div>
                <p class="text-sm mt-1">A soap-cloud bath, olive-oil soap whipped to meringue, poured over you in waves.</p>
              </div>
            </li>
            <li class="flex gap-5">
              <span class="font-display text-3xl text-sand-500 shrink-0 leading-none w-8">4</span>
              <div>
                <div class="font-medium text-mira-900">Rinse.</div>
                <p class="text-sm mt-1">Warm then cooler, in the marble basins.</p>
              </div>
            </li>
            <li class="flex gap-5">
              <span class="font-display text-3xl text-sand-500 shrink-0 leading-none w-8">5</span>
              <div>
                <div class="font-medium text-mira-900">Rest.</div>
                <p class="text-sm mt-1">Wrapped in a fresh dry peştemal, laid on a chaise, offered a mint tea. Fifteen to thirty minutes — stay as long as you want.</p>
              </div>
            </li>
          </ol>
        </div>
      </div>
    """, bg="bg-white")

    # ------------------- Before you visit (etiquette / what to bring) -------------------
    etiquette = section(f"""
      <div class="max-w-4xl mx-auto">
        {eyebrow('Before you visit')}
        {heading('A few small things to know.', 3)}
        <div class="mt-10 grid md:grid-cols-2 gap-x-12 gap-y-6 text-mira-700 text-sm leading-relaxed">
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900">Robe, slippers &amp; towels are provided.</span> Come from your room in a robe; we'll do the rest.</div></div>
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900">Wear a swimsuit if you prefer.</span> In the hammam and pool areas, swimwear is normal; disposable underwear is available for treatments.</div></div>
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900">Arrive 15 minutes early.</span> The spa reception has cold herbal water and a quiet lounge to change out of the outside world.</div></div>
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900">Phones stay in the locker.</span> The spa is a quiet zone.</div></div>
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900">Tell us about pregnancy, injury or allergy at booking.</span> We adjust every ritual to your body.</div></div>
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900">Cancellations 24 hours before.</span> Same-day changes are fine — text the WhatsApp on the sidebar.</div></div>
        </div>
      </div>
    """, bg="bg-sand-50")

    # ------------------- Direct spa contact block -------------------
    contact = section(f"""
      <div class="max-w-5xl mx-auto bg-mira-900 text-white rounded-2xl overflow-hidden shadow-lux">
        <div class="grid lg:grid-cols-2 items-stretch">
          <div class="aspect-[4/3] lg:aspect-auto bg-cover bg-center" style="background-image:url('{root}{IMG_SPA_11}')"></div>
          <div class="p-10 lg:p-12">
            <div class="text-[10px] uppercase tracking-widest text-sand-300 font-semibold">Reserve your session</div>
            <h3 class="font-display text-4xl mt-3">The spa desk answers directly.</h3>
            <p class="mt-5 text-white/80 leading-relaxed">
              Book online in ninety seconds, or call the spa reception straight — different number to the front desk so we can dispatch without tying up the main line.
            </p>
            <div class="mt-8 space-y-4">
              <a href="tel:{m['spa_phone_tel']}" class="flex items-center gap-4 group">
                <div class="w-12 h-12 rounded-full bg-white/10 grid place-items-center text-2xl">☎</div>
                <div>
                  <div class="text-xs uppercase tracking-widest text-sand-300">Spa reception</div>
                  <div class="font-display text-2xl group-hover:text-sand-200 transition">{m['spa_phone_display']}</div>
                </div>
              </a>
              <a href="{m['spa_whatsapp']}" rel="noopener" class="flex items-center gap-4 group">
                <div class="w-12 h-12 rounded-full bg-white/10 grid place-items-center text-2xl">💬</div>
                <div>
                  <div class="text-xs uppercase tracking-widest text-sand-300">WhatsApp</div>
                  <div class="font-display text-2xl group-hover:text-sand-200 transition">Same number, faster</div>
                </div>
              </a>
              <a href="{m['spa_instagram_url']}" rel="noopener" class="flex items-center gap-4 group">
                <div class="w-12 h-12 rounded-full bg-white/10 grid place-items-center text-2xl">📷</div>
                <div>
                  <div class="text-xs uppercase tracking-widest text-sand-300">Instagram</div>
                  <div class="font-display text-2xl group-hover:text-sand-200 transition">@{m['spa_instagram_handle'].lower()}</div>
                </div>
              </a>
            </div>
            <a href="{root}spa-book.html" class="mt-10 inline-flex items-center gap-3 px-8 py-4 bg-sand-300 text-mira-900 rounded-full font-semibold hover:bg-sand-200 transition">
              Book online <span>→</span>
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

    h = hero(f"{root}{IMG_SPA_6}", "Spa · Treatments",
             "The treatment menu.",
             "Massage, facial, body work, hammam rituals. Prices in Euro. Hammam and facility access are included in your stay; treatments below are priced per serve and can be booked at the spa reception or via WhatsApp.",
             height="60vh")
    body = section(f"""
      {blocks}
      <p class="mt-10 text-xs text-mira-500 italic">Prices illustrative for the demo site. Real pricing will be supplied by the hotel on content hand-off. A 24-hour cancellation policy applies; a no-show is charged at 50 per cent.</p>
      <a href="{root}contact.html#enquiry" class="mt-8 inline-flex items-center px-6 py-3 bg-mira-700 text-white rounded-full font-medium hover:bg-mira-800">Book a treatment</a>
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
