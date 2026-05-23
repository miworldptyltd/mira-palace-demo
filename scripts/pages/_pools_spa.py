from common import hero, hero_slideshow, section, eyebrow, heading, cta_band

# Real Mira Palace photography (copied + resized by Copy-Photos.ps1)
IMG_GARDEN_1 = "assets/img/garden/garden-01.jpg"
IMG_GARDEN_2 = "assets/img/garden/garden-02.jpg"
IMG_GARDEN_3 = "assets/img/garden/garden-03.jpg"
IMG_GARDEN_4 = "assets/img/garden/garden-04.jpg"
IMG_SPA_1 = "assets/img/spa/spa-01.jpg"
IMG_SPA_2 = "assets/img/spa/spa-02.jpg"
IMG_SPA_3 = "assets/img/spa/spa-03.jpg"
IMG_SPA_4 = "assets/img/spa/spa-04.jpg"
IMG_SPA_5 = "assets/img/spa/spa-05.jpg"
IMG_SPA_6 = "assets/img/spa/spa-06.jpg"


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
    # 4-slide hero from the spa folder
    hero_urls = [f"{root}{u}" for u in (IMG_SPA_1, IMG_SPA_2, IMG_SPA_3, IMG_SPA_4)]
    h = hero_slideshow(hero_urls, "Spa & Wellness",
             "A hammam in the old way.<br/>A spa menu in the quiet way.",
             "A full Turkish hammam — marble göbek taşı, two saunas, a steam room, a cold plunge, a relaxation room — plus six treatment rooms for massage, facial and body work.",
             primary_href=f"{root}spa-treatments.html", primary_label="See the treatment menu",
             height="72vh")
    fac = [
        ("Turkish hammam", "Marble chamber heated from underneath, round göbek taşı in the centre, cold-water basins along the walls. Peştemal-wrapped attendants with over a decade of experience."),
        ("Saunas & steam", "A traditional dry sauna, an aroma sauna scented lightly with eucalyptus, and a steam room with Anatolian herbs."),
        ("Cold plunge", "12 °C. The short sharp contrast that people come to Turkish hammams for in the first place."),
        ("Relaxation room", "A dim, softly-heated room with reclining chaises, fresh mint water, and stacks of fresh towels. The place to land after a hammam ritual."),
        ("Fitness studio", "Cardio (treadmill, rower, bike) and light weights. Two group classes per day — typically yoga in the morning and stretch or aqua-fit in the afternoon."),
        ("Six treatment rooms", "Two single, two double, and two specialist rooms (wet room for body scrubs, hammam-side room for scrub + massage combinations). Heated tables, quiet."),
    ]
    cards = "".join(
        f'<div class="p-7 bg-white rounded-lg shadow-lux"><h3 class="font-display text-2xl text-mira-900">{t}</h3><p class="mt-3 text-mira-700 text-sm leading-relaxed">{d}</p></div>'
        for t, d in fac
    )
    a = section(f"""
      {eyebrow('What’s in the spa')}
      {heading('Facilities (included in your stay).')}
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-7 mt-10">{cards}</div>
    """, bg="bg-sand-50")
    b = section(f"""
      <div class="grid lg:grid-cols-2 gap-12 items-center">
        <div class="aspect-[4/3] bg-cover bg-center rounded-lg shadow-lux" style="background-image:url('{root}{IMG_SPA_5}')"></div>
        <div>{eyebrow('The hammam ritual')}
          {heading('Ninety minutes, five stages.', 3)}
          <ol class="mt-6 space-y-4 text-mira-700">
            <li><span class="font-semibold text-mira-900">1. Warm.</span> Fifteen minutes on the heated marble, lying on a cotton peştemal. The room is quiet; the heat is soft but thorough.</li>
            <li><span class="font-semibold text-mira-900">2. Exfoliate.</span> An attendant works with a kese glove — the Turkish coarse silk mitt. Nothing stays that wasn’t going to.</li>
            <li><span class="font-semibold text-mira-900">3. Foam.</span> A soap-cloud bath, olive-oil soap whipped to meringue, poured over you in waves.</li>
            <li><span class="font-semibold text-mira-900">4. Rinse.</span> Warm then cooler, in the marble basins.</li>
            <li><span class="font-semibold text-mira-900">5. Rest.</span> Wrapped in a fresh dry peştemal, laid on a chaise, offered a mint tea. Fifteen to thirty minutes — stay as long as you want.</li>
          </ol>
          <a href="{root}spa-treatments.html" class="mt-8 inline-flex items-center gap-2 text-mira-700 font-medium hover:text-sand-600">Full treatment menu &amp; prices <span>→</span></a>
        </div>
      </div>
    """, bg="bg-white")
    return h + a + b


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
