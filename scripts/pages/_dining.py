"""World-class Dining pages for Mira Palace.

Structure mirrors the R017 Spa page rebuild — the same 8-section blueprint
that top-tier hotel dining pages use (Aman gastronomy, Rosewood dining,
Six Senses restaurants, Mandarin Oriental):

  1. Cinematic hero slideshow
  2. Philosophy intro (kitchen voice)
  3. Three venue cards (Main Restaurant / Pool Bar / Lobby Bar)
  4. Every-visit inclusions strip (reassurance)
  5. Ingredients showcase (six pillars of the pantry)
  6. Chef voice quote in a dark champagne-gold block
  7. Etiquette grid (dress code, kids, dietary, private events)
  8. Direct dining contact block

Imagery notes (R019):
- The two "real" restaurant photos below are hot-linked from the existing
  live sidemirapalace.com site while DNS access is unavailable. At R021
  URL cutover we import them locally into `assets/img/dining/` and swap
  the URLs. Cross-domain hot-linking is fine for the demo phase.
- Everything else is from images.unsplash.com — stable CDN URLs, replaced
  with real Mira Palace photography when the hotel provides shots.
"""

from common import (
    hero_slideshow, section, eyebrow, heading, SITE_META,
)


# ------------------------------------------------------------------ imagery

# The two real restaurant/bar photos discovered on the live site (R019 audit).
# Bar hero — polished dark wood counter with backlit yellow spirits shelves.
IMG_LIVE_BAR   = "https://sidemirapalace.com/img/restaurant/20240713110135_88159.png"
# Casual dining space — wooden benches under string-lit ceiling.
IMG_LIVE_HALL  = "https://sidemirapalace.com/img/imkanlar/20240713112112_56335.png"

# Detail shots — Unsplash CDN, chosen for the champagne/gold + dark Midnight
# palette. Each is picked deliberately: warm amber tones, shallow depth of
# field, no faces (so no consent issue).
IMG_WHISKY     = "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&w=1600&q=80"
IMG_COFFEE     = "https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=1600&q=80"
IMG_WINE_POUR  = "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?auto=format&fit=crop&w=1600&q=80"
IMG_COCKTAIL   = "https://images.unsplash.com/photo-1587223962930-cb7f31384c19?auto=format&fit=crop&w=1600&q=80"
IMG_ESPRESSO   = "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=1600&q=80"
IMG_BREAKFAST  = "https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=1600&q=80"
IMG_PLATE_FISH = "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=1600&q=80"
IMG_BAKLAVA    = "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?auto=format&fit=crop&w=1600&q=80"
IMG_OLIVE_OIL  = "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?auto=format&fit=crop&w=1600&q=80"
IMG_BREAD      = "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=1600&q=80"
IMG_MEZZE      = "https://images.unsplash.com/photo-1544378730-6d5c9bea174d?auto=format&fit=crop&w=1600&q=80"
IMG_CHEF       = "https://images.unsplash.com/photo-1607301405390-d831c242f59b?auto=format&fit=crop&w=1600&q=80"
IMG_POOLSIDE   = "https://images.unsplash.com/photo-1470337458703-46ad1756a187?auto=format&fit=crop&w=1600&q=80"
IMG_LOUNGE     = "https://images.unsplash.com/photo-1572116469696-31de0f17cc34?auto=format&fit=crop&w=1600&q=80"


# ------------------------------------------------------------------ index

def dining_index(root: str) -> str:
    """World-class dining hub page.

    Same 8-section blueprint as the spa page. Every string is tagged with a
    data-i18n key so the TR/DE/RU pass in R020 is mechanical.
    """
    m = SITE_META

    # 5-slide hero: real bar + real hall + three detail shots
    hero_urls = [IMG_LIVE_BAR, IMG_LIVE_HALL, IMG_WINE_POUR, IMG_BREAKFAST, IMG_PLATE_FISH]
    h = hero_slideshow(
        hero_urls,
        '<span data-i18n="din.hero.kicker">Dining &amp; Bars</span>',
        '<span data-i18n="din.hero.h1">Antalya on the plate. Türkiye in the glass.</span>',
        '<span data-i18n="din.hero.sub">Three settings, one Mediterranean philosophy — a chef-led main restaurant, a pool bar for long lunches, and a lobby bar that stays open late. Every ingredient sourced within a hundred kilometres wherever the season allows.</span>',
        primary_href=f"{root}book.html",
        primary_label='<span data-i18n="din.hero.cta">Reserve a table</span>',
        height="76vh",
    )

    # --------------- 2. Philosophy intro ---------------
    intro = section(f"""
      <div class="grid lg:grid-cols-12 gap-12 items-start">
        <div class="lg:col-span-4">
          <p class="uppercase tracking-[0.22em] text-mira-600 text-xs font-semibold" data-i18n="din.intro.eyebrow">Our kitchen</p>
          <h2 class="font-display text-3xl sm:text-4xl md:text-5xl text-mira-900 leading-tight" data-i18n="din.intro.h2">Cooked short. Served slowly.</h2>
        </div>
        <div class="lg:col-span-8 text-mira-700 leading-relaxed space-y-4 text-lg">
          <p data-i18n="din.intro.p1">Our menu is short because the pantry is short. Fish from the Manavgat morning market, lamb from the Toros foothills, vegetables from three farms we buy from directly, citrus from the grove ten minutes down the coast road. If it can't be brought in fresh that morning, we don't put it on the pass.</p>
          <p data-i18n="din.intro.p2">Everything we serve leans Turkish-Mediterranean, but the pace is our own: unhurried, warm, precise on the plate and generous at the table. Thirty-four suites means every dinner service fits in one seating — the chef comes out, the sommelier remembers your wine, no one is rushed for the next cover.</p>
        </div>
      </div>
    """, bg="bg-white")

    # --------------- 3. Three venue cards ---------------
    venues = [
        {
            "key": "main",
            "name_i18n": "din.v.main.name",
            "long_name": "Mira Restaurant",
            "img": IMG_LIVE_HALL,
            "tag_i18n": "din.v.main.tag",
            "tag_label": "Signature dining",
            "tagline": "Turkish-Mediterranean plating in the main dining room — the heart of the hotel.",
            "hours_i18n": "din.v.main.hours",
            "hours_label": "07:00 – 10:30 · 12:30 – 14:30 · 19:00 – 22:00",
            "bullets": [
                ("din.v.b.chef",       "Chef-led plated dinner service"),
                ("din.v.b.buffet",     "Open-kitchen breakfast &amp; lunch buffets"),
                ("din.v.b.rotating",   "Rotating regional theme every evening"),
                ("din.v.b.wine",       "Turkish and Old-World wine pairings"),
                ("din.v.b.window",     "Open kitchen, window onto the garden"),
            ],
            "href": f"{root}dining/main-restaurant.html",
        },
        {
            "key": "pool",
            "name_i18n": "din.v.pool.name",
            "long_name": "Pool Bar",
            "img": IMG_POOLSIDE,
            "tag_i18n": "din.v.pool.tag",
            "tag_label": "All-day poolside",
            "tagline": "Mezze, wood-fired pide and long lunches under the pergola — swimsuits welcome.",
            "hours_i18n": "din.v.pool.hours",
            "hours_label": "10:00 – 19:00 · Ice-cream cart 15:00 – 17:00",
            "bullets": [
                ("din.v.b.mezze",      "Twenty small mezze plates, changing daily"),
                ("din.v.b.pide",       "Wood-fired pide &amp; pizza to order"),
                ("din.v.b.grill",      "Grilled fish of the morning market"),
                ("din.v.b.icecream",   "Afternoon ice-cream cart for the children"),
                ("din.v.b.jasmine",    "Pergola shade heavy with jasmine in July"),
            ],
            "href": f"{root}dining/pool-bar.html",
        },
        {
            "key": "lobby",
            "name_i18n": "din.v.lobby.name",
            "long_name": "Lobby Bar",
            "img": IMG_LIVE_BAR,
            "tag_i18n": "din.v.lobby.tag",
            "tag_label": "Nightcaps &amp; espresso",
            "tagline": "Morning espresso to midnight cocktails — the polished-wood counter that anchors the ground floor.",
            "hours_i18n": "din.v.lobby.hours",
            "hours_label": "10:00 – 01:00 · Piano 20:00 – 23:00",
            "bullets": [
                ("din.v.b.house",      "House cocktails built around rakı &amp; pomegranate"),
                ("din.v.b.reserve",    "Reserve list — small-batch Turkish &amp; Old-World spirits"),
                ("din.v.b.piano",      "Live piano four evenings a week"),
                ("din.v.b.coffee",     "Fresh-roasted Turkish coffee, served properly"),
                ("din.v.b.late",       "Last call at 00:45 — no one is rushed out"),
            ],
            "href": f"{root}dining/lobby-bar.html",
        },
    ]

    def _venue_card(v, is_middle=False):
        badge = ('<span class="absolute top-4 right-4 bg-sand-300 text-mira-900 text-[10px] font-semibold '
                 'tracking-widest uppercase px-3 py-1 rounded-full" data-i18n="din.venues.most_loved">Most loved</span>' if is_middle else '')
        bullets = "".join(
            f'<li class="flex gap-3 text-sm text-mira-700 leading-relaxed">'
            f'<span class="text-sand-500 shrink-0 mt-0.5">✓</span><span data-i18n="{k}">{item}</span></li>'
            for k, item in v["bullets"]
        )
        highlight_ring = 'ring-2 ring-sand-300 shadow-2xl' if is_middle else 'shadow-lux'
        return f"""
        <article class="relative bg-white rounded-2xl overflow-hidden {highlight_ring} flex flex-col">
          {badge}
          <div class="aspect-[16/10] bg-cover bg-center" style="background-image:url('{v['img']}')"></div>
          <div class="p-8 flex-1 flex flex-col">
            <p class="text-[10px] uppercase tracking-widest text-sand-600 font-semibold" data-i18n="{v['tag_i18n']}">{v['tag_label']}</p>
            <h3 class="mt-2 font-display text-3xl text-mira-900 leading-none" data-i18n="{v['name_i18n']}">{v['long_name']}</h3>
            <p class="mt-3 text-sm italic text-sand-600" data-i18n="din.v.{v['key']}.tagline">{v['tagline']}</p>
            <div class="mt-6 pt-6 border-t border-mira-100">
              <div class="text-[10px] uppercase tracking-widest text-mira-500 font-semibold mb-3" data-i18n="din.venues.on_the_menu">On the menu</div>
              <ul class="space-y-2">{bullets}</ul>
            </div>
            <div class="mt-6 pt-4 border-t border-mira-100 text-xs">
              <div class="text-[10px] uppercase tracking-widest text-mira-500 font-semibold" data-i18n="din.venues.hours">Hours</div>
              <div class="mt-1 text-mira-700" data-i18n="{v['hours_i18n']}">{v['hours_label']}</div>
            </div>
            <a href="{v['href']}"
               class="mt-8 w-full inline-flex items-center justify-center gap-2 px-6 py-3.5 bg-mira-800 text-white rounded-full font-medium text-sm hover:bg-mira-900 transition">
              <span data-i18n="din.venues.explore">Explore</span> <span data-i18n="{v['name_i18n']}">{v['long_name']}</span> <span>→</span>
            </a>
          </div>
        </article>
        """

    venue_cards = "".join(_venue_card(v, is_middle=(i == 0)) for i, v in enumerate(venues))

    venues_section = section(f"""
      <div class="text-center max-w-2xl mx-auto">
        <p class="uppercase tracking-[0.22em] text-sand-600 text-xs font-semibold" data-i18n="din.venues.eyebrow">Three settings</p>
        <h2 class="font-display text-3xl sm:text-4xl md:text-5xl text-mira-900 leading-tight" data-i18n="din.venues.h2">Where to eat and drink.</h2>
        <p class="mt-5 text-mira-700 leading-relaxed" data-i18n="din.venues.lead">
          One kitchen. Three different moods. Move between them however the day wants to unfold — swimsuit at lunch, something linen at dinner, a nightcap on the way to bed.
        </p>
      </div>
      <div class="grid md:grid-cols-3 gap-7 mt-14">{venue_cards}</div>
      <p class="mt-8 text-center text-xs text-mira-500 italic">
        <span data-i18n="din.venues.foot">Table reservations recommended for dinner. Reserve online, or call reception directly —</span>
        <a class="underline hover:text-sand-500" href="tel:{m['phone_tel']}">{m['phone_display']}</a>.
      </p>
    """, bg="bg-sand-50")

    # --------------- 4. Every-visit inclusions strip ---------------
    every_visit = section(f"""
      <div class="max-w-5xl mx-auto text-center">
        <p class="uppercase tracking-[0.22em] text-mira-600 text-xs font-semibold" data-i18n="din.every.eyebrow">In every meal</p>
        <h2 class="font-display text-3xl sm:text-4xl md:text-5xl text-mira-900 leading-tight" data-i18n="din.every.h2">What is always there.</h2>
        <p class="mt-5 text-mira-700 leading-relaxed" data-i18n="din.every.lead">
          Regardless of which room you're eating in — these are the constants.
        </p>
        <div class="mt-12 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-6">
          <div class="text-center">
            <div class="text-4xl">🍞</div>
            <div class="mt-2 font-display text-lg text-mira-900" data-i18n="din.every.bread.t">Warm bread</div>
            <div class="text-xs text-mira-600 mt-1" data-i18n="din.every.bread.s">Baked in-house every morning</div>
          </div>
          <div class="text-center">
            <div class="text-4xl">🫒</div>
            <div class="mt-2 font-display text-lg text-mira-900" data-i18n="din.every.oil.t">Aegean olive oil</div>
            <div class="text-xs text-mira-600 mt-1" data-i18n="din.every.oil.s">Cold-pressed, single estate</div>
          </div>
          <div class="text-center">
            <div class="text-4xl">☕</div>
            <div class="mt-2 font-display text-lg text-mira-900" data-i18n="din.every.coffee.t">Turkish coffee</div>
            <div class="text-xs text-mira-600 mt-1" data-i18n="din.every.coffee.s">Copper cezve, the old way</div>
          </div>
          <div class="text-center">
            <div class="text-4xl">👶</div>
            <div class="mt-2 font-display text-lg text-mira-900" data-i18n="din.every.kids.t">Kids' menu</div>
            <div class="text-xs text-mira-600 mt-1" data-i18n="din.every.kids.s">Small plates, gentle spice</div>
          </div>
          <div class="text-center">
            <div class="text-4xl">🌱</div>
            <div class="mt-2 font-display text-lg text-mira-900" data-i18n="din.every.dietary.t">Dietary swaps</div>
            <div class="text-xs text-mira-600 mt-1" data-i18n="din.every.dietary.s">Vegan, gluten-free, allergy</div>
          </div>
          <div class="text-center">
            <div class="text-4xl">🍇</div>
            <div class="mt-2 font-display text-lg text-mira-900" data-i18n="din.every.wine.t">Turkish wine</div>
            <div class="text-xs text-mira-600 mt-1" data-i18n="din.every.wine.s">By the glass, the bottle, the story</div>
          </div>
        </div>
      </div>
    """, bg="bg-white")

    # --------------- 5. Ingredients showcase (six pillars of the pantry) ---------------
    pantry = [
        ("din.pantry.oil.t", "Aegean olive oil",
         "din.pantry.oil.d", "Single-estate, cold-pressed, from an orchard forty kilometres west of the hotel. The house oil sits on every table. The finishing oil comes out for the plated dishes.",
         IMG_OLIVE_OIL),
        ("din.pantry.citrus.t", "Antalya citrus",
         "din.pantry.citrus.d", "The valley behind us grows some of Türkiye's best oranges, lemons and pomegranates. What arrives in the kitchen at 6 a.m. is on the plate by lunch.",
         IMG_WHISKY),  # amber tone matches
        ("din.pantry.lamb.t", "Toros lamb",
         "din.pantry.lamb.d", "Raised in the Toros foothills on wild herb pasture. Butchered by a partner in Manavgat we've worked with for five years. Slow-cooked, grilled over vine wood, or braised in pomegranate molasses.",
         IMG_PLATE_FISH),
        ("din.pantry.herbs.t", "Wild herbs",
         "din.pantry.herbs.d", "Sage, thyme, oregano, mountain mint — foraged in season by the same family who supplies the local restaurants of Side. Dried herbs for winter, fresh cut every morning in season.",
         IMG_MEZZE),
        ("din.pantry.bread.t", "Bread &amp; simit",
         "din.pantry.bread.d", "Every loaf, pide, simit and lavash is baked in the hotel bakery from the day's flour. Sourdough starter is the same one we brought over from the family bakery in Antalya, kept alive since 1998.",
         IMG_BREAD),
        ("din.pantry.coffee.t", "Turkish coffee",
         "din.pantry.coffee.d", "Roasted in-house each week from a single-origin Kurukahveci Mehmet Efendi partnership blend. Ground fine, brewed in copper cezve, served with a glass of water and a piece of lokum.",
         IMG_ESPRESSO),
    ]
    pantry_cards = "".join(
        f'<article class="bg-white rounded-lg overflow-hidden shadow-lux group">'
        f'  <div class="aspect-[4/3] bg-cover bg-center transition duration-500 group-hover:scale-[1.03]" style="background-image:url(\'{img}\')"></div>'
        f'  <div class="p-6">'
        f'    <h3 class="font-display text-xl text-mira-900" data-i18n="{ti}">{title}</h3>'
        f'    <p class="mt-2 text-sm text-mira-700 leading-relaxed" data-i18n="{bi}">{body}</p>'
        f'  </div>'
        f'</article>'
        for ti, title, bi, body, img in pantry
    )
    pantry_section = section(f"""
      <p class="uppercase tracking-[0.22em] text-mira-600 text-xs font-semibold" data-i18n="din.pantry.eyebrow">The pantry</p>
      <h2 class="font-display text-3xl sm:text-4xl md:text-5xl text-mira-900 leading-tight" data-i18n="din.pantry.h2">Six things the kitchen is built on.</h2>
      <p class="mt-5 max-w-2xl text-mira-700 leading-relaxed" data-i18n="din.pantry.lead">
        We buy short and we buy local, but we're strict about what we buy. These six pillars are the backbone of almost everything we serve — from breakfast to a late-night whisky.
      </p>
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-7 mt-10">{pantry_cards}</div>
    """, bg="bg-sand-50")

    # --------------- 6. Chef voice quote (dark champagne-gold block) ---------------
    chef_quote = section(f"""
      <div class="max-w-5xl mx-auto bg-mira-900 text-white rounded-2xl overflow-hidden shadow-lux">
        <div class="grid lg:grid-cols-5 items-stretch">
          <div class="aspect-[4/3] lg:aspect-auto lg:col-span-2 bg-cover bg-center" style="background-image:url('{IMG_CHEF}')"></div>
          <div class="lg:col-span-3 p-10 lg:p-14">
            <p class="uppercase tracking-[0.22em] text-sand-300 text-xs font-semibold" data-i18n="din.chef.eyebrow">From the kitchen</p>
            <blockquote class="mt-5 font-display text-2xl sm:text-3xl leading-snug" data-i18n="din.chef.quote">
              &ldquo;Thirty-four suites means one seating. That's a rare thing, and it changes how you cook. Nothing sits under a heat lamp. Nothing is rushed to the pass. Every plate gets checked before it leaves the kitchen — and if the fish came in poor that morning, we tell you and change the menu.&rdquo;
            </blockquote>
            <div class="mt-6 flex items-center gap-4">
              <div class="w-12 h-px bg-sand-300"></div>
              <div>
                <div class="font-display text-lg" data-i18n="din.chef.name">Chef Kaan Demir</div>
                <div class="text-xs uppercase tracking-widest text-sand-300 mt-0.5" data-i18n="din.chef.role">Head Chef · Mira Palace</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    """, bg="bg-white")

    # --------------- 7. Etiquette grid ---------------
    etiquette = section(f"""
      <div class="max-w-4xl mx-auto">
        <p class="uppercase tracking-[0.22em] text-mira-600 text-xs font-semibold" data-i18n="din.etq.eyebrow">A few things to know</p>
        <h3 class="font-display text-2xl sm:text-3xl text-mira-900 leading-tight" data-i18n="din.etq.h2">Small courtesies of the house.</h3>
        <div class="mt-10 grid md:grid-cols-2 gap-x-12 gap-y-6 text-mira-700 text-sm leading-relaxed">
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900" data-i18n="din.etq.1.t">Dress code is easy.</span> <span data-i18n="din.etq.1.d">Swimwear at the pool bar; something linen or a shirt at dinner. No jacket required — this isn't that kind of hotel.</span></div></div>
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900" data-i18n="din.etq.2.t">Children are welcome everywhere.</span> <span data-i18n="din.etq.2.d">A dedicated small-plates menu, high chairs at every table, and the kitchen will happily plate any main in a smaller portion.</span></div></div>
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900" data-i18n="din.etq.3.t">Allergies &amp; dietary at booking.</span> <span data-i18n="din.etq.3.d">Tell us at reservation and again at the table. Vegan, vegetarian, gluten-free, nut-free — the chef adjusts every dish, not a separate menu.</span></div></div>
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900" data-i18n="din.etq.4.t">Private dining, chef's table.</span> <span data-i18n="din.etq.4.d">The small private room seats eight and is available for family celebrations, small tastings, or a birthday dinner. Twenty-four hours' notice.</span></div></div>
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900" data-i18n="din.etq.5.t">Corkage is fine.</span> <span data-i18n="din.etq.5.d">Bring a bottle if you've been travelling with something special — the sommelier will pour it for a modest corkage. Just ask at the maître d'.</span></div></div>
          <div class="flex gap-3"><span class="text-sand-500 shrink-0">✓</span><div><span class="font-medium text-mira-900" data-i18n="din.etq.6.t">Cancellations 4 hours before.</span> <span data-i18n="din.etq.6.d">A courtesy for the kitchen and the sommelier who will have started prepping for your table. Same-day changes — text WhatsApp.</span></div></div>
        </div>
      </div>
    """, bg="bg-sand-50")

    # --------------- 8. Direct dining contact block ---------------
    contact = section(f"""
      <div class="max-w-5xl mx-auto bg-mira-900 text-white rounded-2xl overflow-hidden shadow-lux">
        <div class="grid lg:grid-cols-2 items-stretch">
          <div class="aspect-[4/3] lg:aspect-auto bg-cover bg-center" style="background-image:url('{IMG_LIVE_BAR}')"></div>
          <div class="p-10 lg:p-12">
            <div class="text-[10px] uppercase tracking-widest text-sand-300 font-semibold" data-i18n="din.contact.eyebrow">Reserve a table</div>
            <h3 class="font-display text-4xl mt-3" data-i18n="din.contact.h3">Reception takes reservations directly.</h3>
            <p class="mt-5 text-white/80 leading-relaxed" data-i18n="din.contact.p">
              Book online in ninety seconds, or call reception — evenings sell out on weekends, and we hold a handful of tables until the day of arrival.
            </p>
            <div class="mt-8 space-y-4">
              <a href="tel:{m['phone_tel']}" class="flex items-center gap-4 group">
                <div class="w-12 h-12 rounded-full bg-white/10 grid place-items-center text-2xl">☎</div>
                <div>
                  <div class="text-xs uppercase tracking-widest text-sand-300" data-i18n="din.contact.reception">Hotel reception</div>
                  <div class="font-display text-2xl group-hover:text-sand-200 transition">{m['phone_display']}</div>
                </div>
              </a>
              <a href="{m['whatsapp']}" rel="noopener" class="flex items-center gap-4 group">
                <div class="w-12 h-12 rounded-full bg-white/10 grid place-items-center text-2xl">💬</div>
                <div>
                  <div class="text-xs uppercase tracking-widest text-sand-300" data-i18n="din.contact.whatsapp_label">WhatsApp</div>
                  <div class="font-display text-2xl group-hover:text-sand-200 transition" data-i18n="din.contact.whatsapp_v">Same number, faster</div>
                </div>
              </a>
              <a href="tel:{m['phone_landline_tel']}" class="flex items-center gap-4 group">
                <div class="w-12 h-12 rounded-full bg-white/10 grid place-items-center text-2xl">📞</div>
                <div>
                  <div class="text-xs uppercase tracking-widest text-sand-300" data-i18n="din.contact.landline">Landline</div>
                  <div class="font-display text-2xl group-hover:text-sand-200 transition">{m['phone_landline_display']}</div>
                </div>
              </a>
            </div>
            <a href="{root}book.html" class="mt-10 inline-flex items-center gap-3 px-8 py-4 bg-sand-300 text-mira-900 rounded-full font-semibold hover:bg-sand-200 transition">
              <span data-i18n="din.contact.cta">Reserve online</span> <span>→</span>
            </a>
          </div>
        </div>
      </div>
    """, bg="bg-white")

    return h + intro + venues_section + every_visit + pantry_section + chef_quote + etiquette + contact


# ------------------------------------------------------------------ sub-pages

def _venue_page(root: str, *, hero_img: str, kicker: str, headline: str,
                sub: str, essence_paragraphs: list[str],
                highlights_title: str, highlights: list[tuple[str, str]],
                hours_rows: list[tuple[str, str]],
                voice_quote: str, voice_name: str, voice_role: str,
                voice_img: str, book_cta_label: str, keys_prefix: str) -> str:
    """Shared skeleton for the three venue sub-pages.

    keys_prefix is e.g. "din.main" — makes every i18n key deterministic.
    """
    m = SITE_META

    h = hero_slideshow(
        [hero_img],
        f'<span data-i18n="{keys_prefix}.hero.kicker">{kicker}</span>',
        f'<span data-i18n="{keys_prefix}.hero.h1">{headline}</span>',
        f'<span data-i18n="{keys_prefix}.hero.sub">{sub}</span>',
        primary_href=f"{root}book.html",
        primary_label=f'<span data-i18n="{keys_prefix}.hero.cta">{book_cta_label}</span>',
        height="68vh",
    )

    # Essence + hours sidebar
    paras_html = "".join(
        f'<p data-i18n="{keys_prefix}.p{i+1}">{p}</p>' for i, p in enumerate(essence_paragraphs)
    )
    hours_dl = "".join(
        f'<dt class="text-mira-600" data-i18n="{keys_prefix}.hours.{i}.k">{k}</dt>'
        f'<dd class="text-right font-medium" data-i18n="{keys_prefix}.hours.{i}.v">{v}</dd>'
        for i, (k, v) in enumerate(hours_rows)
    )
    body = section(f"""
      <div class="grid lg:grid-cols-12 gap-12">
        <div class="lg:col-span-7 text-mira-700 leading-relaxed text-lg space-y-5">
          {paras_html}
        </div>
        <aside class="lg:col-span-5">
          <div class="bg-white rounded-lg shadow-lux p-7">
            <h3 class="font-display text-2xl text-mira-900" data-i18n="{keys_prefix}.hours.h3">Hours &amp; house rules</h3>
            <dl class="mt-5 grid grid-cols-2 gap-y-3 text-sm">{hours_dl}</dl>
            <a href="{root}book.html" class="mt-6 inline-flex items-center gap-2 text-sm font-medium text-mira-800 hover:text-sand-600">
              <span data-i18n="{keys_prefix}.hours.cta">Reserve a table</span> →
            </a>
          </div>
        </aside>
      </div>
    """, bg="bg-white")

    # Highlights list
    hl_rows = "".join(
        f'<div class="menu-row"><div class="name" data-i18n="{keys_prefix}.hl.{i}.n">{n}</div>'
        f'<div class="desc" data-i18n="{keys_prefix}.hl.{i}.d">{d}</div></div>'
        for i, (n, d) in enumerate(highlights)
    )
    highlights_html = section(f"""
      <span id="menu" class="block -mt-24 pt-24" aria-hidden="true"></span>
      <div class="text-center max-w-2xl mx-auto">
        <p class="uppercase tracking-[0.22em] text-sand-600 text-xs font-semibold" data-i18n="{keys_prefix}.hl.eyebrow">Signature moments</p>
        <h2 class="font-display text-3xl sm:text-4xl md:text-5xl text-mira-900 leading-tight" data-i18n="{keys_prefix}.hl.h2">{highlights_title}</h2>
      </div>
      <div class="mt-10 max-w-3xl mx-auto">
        <div class="menu-card rounded-md">
          {hl_rows}
        </div>
        <p class="mt-8 text-center text-xs italic" style="color:var(--mira-700); font-family:Inter,sans-serif; letter-spacing:.05em;" data-i18n="{keys_prefix}.hl.foot">Menu rotates with the season &middot; vegan, gluten-free &amp; allergy adjustments made at the table.</p>
      </div>
    """, bg="bg-sand-50")

    # Voice quote block
    voice_html = section(f"""
      <div class="max-w-4xl mx-auto bg-mira-900 text-white rounded-2xl overflow-hidden shadow-lux">
        <div class="grid md:grid-cols-5 items-stretch">
          <div class="aspect-[4/3] md:aspect-auto md:col-span-2 bg-cover bg-center" style="background-image:url('{voice_img}')"></div>
          <div class="md:col-span-3 p-8 md:p-10">
            <p class="uppercase tracking-[0.22em] text-sand-300 text-xs font-semibold" data-i18n="{keys_prefix}.voice.eyebrow">In their words</p>
            <blockquote class="mt-4 font-display text-xl sm:text-2xl leading-snug" data-i18n="{keys_prefix}.voice.quote">
              &ldquo;{voice_quote}&rdquo;
            </blockquote>
            <div class="mt-6">
              <div class="font-display text-lg" data-i18n="{keys_prefix}.voice.name">{voice_name}</div>
              <div class="text-xs uppercase tracking-widest text-sand-300 mt-0.5" data-i18n="{keys_prefix}.voice.role">{voice_role}</div>
            </div>
          </div>
        </div>
      </div>
    """, bg="bg-white")

    return h + body + highlights_html + voice_html


def main_restaurant(root: str) -> str:
    return _venue_page(
        root,
        hero_img=IMG_LIVE_HALL,
        kicker="Mira Restaurant",
        headline="The main dining room.",
        sub="Turkish-Mediterranean plating in the heart of the ground floor — thirty-four suites means one seating, and one seating means the chef checks every plate before it leaves the pass.",
        essence_paragraphs=[
            "Sixty covers at capacity — enough that a full house is a proper room, small enough that the maître d' knows every table. Breakfast and lunch are open-kitchen buffets, always with a hot corner, an egg station, a fresh-juice bar and an espresso machine we take seriously.",
            "Dinner is a plated, menu-led evening service with a rotating regional theme — a different corner of Türkiye each night, from Aegean fish to Southeastern kebab, with a small à-la-carte column running underneath for the classics. Wine pairings suggested by the sommelier if you want them.",
            "The room opens onto the garden through floor-to-ceiling glass; in season, the doors fold back and half the tables spill onto the terrace. In winter, the fireplace at the north end draws the room together.",
        ],
        highlights_title="Tonight at Mira.",
        highlights=[
            ("Grilled octopus",           "white-bean purée, pul biber oil, lemon"),
            ("Chilled tomato soup",       "basil granita, dill, olive oil"),
            ("Whole sea bass, wood-fired","lemon, thyme, salt-baked potato"),
            ("Slow-braised beef cheek",   "smoked aubergine, pomegranate molasses, jus"),
            ("Vegetable moussaka",        "pine nuts, feta, oregano, tahini yoghurt"),
            ("Baklava with kaymak",       "walnut &amp; pistachio, warm from the oven"),
            ("Antalya cheese board",      "fig jam, honeycomb, walnut bread"),
            ("Turkish coffee &amp; lokum",     "the way it should be — with a glass of water"),
        ],
        hours_rows=[
            ("Breakfast",  "07:00 – 10:30"),
            ("Lunch",      "12:30 – 14:30"),
            ("Dinner",     "19:00 – 22:00"),
            ("Dress",      "Smart casual"),
            ("Children",   "Welcome, kids' menu"),
            ("Private room", "Seats 8, on request"),
        ],
        voice_quote="One seating is a discipline. We cook for the room we can see, and we finish when the last table wants to. If a guest asks for something off-menu, we look at what came in that morning and do our best — that answer is almost always yes.",
        voice_name="Chef Kaan Demir",
        voice_role="Head Chef · Mira Restaurant",
        voice_img=IMG_CHEF,
        book_cta_label="Reserve a table",
        keys_prefix="din.main",
    )


def pool_bar(root: str) -> str:
    return _venue_page(
        root,
        hero_img=IMG_POOLSIDE,
        kicker="Pool Bar",
        headline="Long lunches by the pool.",
        sub="Twenty small mezze plates, wood-fired pide, grilled fish of the morning market — served under a pergola heavy with jasmine, with the pool three metres away.",
        essence_paragraphs=[
            "Open only for lunch — the main restaurant takes dinner — the pool bar is deliberately informal. Walk up from the water in your swimsuit, a sarong or a towel; the chef will plate your pide just the same. No dress code, no fuss, no reservation needed.",
            "The heart of the space is the mezze bar: twenty small dishes rotated daily — smoked aubergine, haydari, ezme, cacık, piyaz, muhammara, fried artichokes, chickpea salad, tarama. Alongside it, a wood oven that turns out pides and pizzas to order, and a small grill for the fish that came off the boat that morning.",
            "In the afternoon, an ice-cream cart wheels out between 15:00 and 17:00 — pistachio, sour cherry, mastic, chocolate. It always runs out of pistachio.",
        ],
        highlights_title="At the pool today.",
        highlights=[
            ("Mezze bar",                 "twenty small plates, changing daily"),
            ("Wood-fired pide",           "lamb, spinach &amp; feta, four-cheese"),
            ("Grilled dorade",            "lemon, oregano, olive oil, tomato salad"),
            ("Fisherman's grill platter", "octopus, calamari, king prawns, dill"),
            ("Kids' pide &amp; chips",         "portion-sized, milder spice"),
            ("Ice-cream cart",            "pistachio, sour cherry, mastic, dark chocolate"),
            ("Fresh watermelon &amp; feta",    "flat-leaf mint, cracked black pepper"),
            ("Turkish coffee under the pergola", "or an espresso, whichever way the day is going"),
        ],
        hours_rows=[
            ("Lunch",       "12:30 – 15:00"),
            ("All-day mezze", "10:00 – 18:00"),
            ("Ice cream",   "15:00 – 17:00"),
            ("Seating",     "Pergola, 40 covers"),
            ("Dress",       "Swimwear is fine"),
            ("Kids' menu",  "Yes"),
        ],
        voice_quote="Lunch by the pool is a mood. You come off a chaise still warm from the sun, you're not in the frame of mind for a fifteen-course tasting menu. So we cook things that share well and reach for a glass of white — mezze, pide, a piece of fish. That's the room.",
        voice_name="Sous Chef Selin Aydın",
        voice_role="Sous Chef · Pool Bar",
        voice_img=IMG_MEZZE,
        book_cta_label="Reserve poolside",
        keys_prefix="din.pool",
    )


def lobby_bar(root: str) -> str:
    return _venue_page(
        root,
        hero_img=IMG_LIVE_BAR,
        kicker="Lobby Bar",
        headline="Espresso in the morning. Nightcaps at midnight.",
        sub="The polished-wood counter that anchors the ground floor — coffee and pastries at daybreak, cocktails and piano after dark. Open every day, 10:00 to 01:00.",
        essence_paragraphs=[
            "The lobby bar is the beating heart of the ground floor. It opens for espresso and freshly-baked pastries at 10:00, keeps pouring through the afternoon for those who never quite left, and shifts into cocktails at 17:00 as the light drops. The piano starts at eight most evenings; last call is 00:45 and no one is rushed to the door.",
            "The house cocktail list leans Turkish — rakı sours, pomegranate-molasses spritzes, orchard mojitos with mint from the garden — with a longer reserve list of small-batch Turkish spirits, Old-World whiskies, cognac and Champagne for the guests who want the good bottle from the top shelf.",
            "The bar itself is polished dark wood with backlit yellow shelving behind — the room the architect got right first time. Sit at the counter, order the sommelier's evening pour, and watch the barman do the honest work.",
        ],
        highlights_title="From the bar tonight.",
        highlights=[
            ("Rakı sour",                 "rakı, lemon, egg-white, morello cherry"),
            ("Side spritz",               "bitter orange, prosecco, thyme, ice"),
            ("Pomegranate martini",       "pomegranate molasses, vodka, lime, sumac rim"),
            ("Orchard mojito",            "garden mint, basil, white rum, lime"),
            ("Turkish coffee, the way it should be", "copper cezve, glass of water, lokum on the side"),
            ("Reserve pour",              "Balvenie 14 · Balcones single malt · Corvus Rüzgar red"),
            ("Late-night mezze",          "olives, cheese, warm bread, honeycomb"),
            ("Signature baklava",         "with a glass of Turkish tea, at any hour"),
        ],
        hours_rows=[
            ("Bar open",    "10:00 – 01:00"),
            ("Espresso",    "10:00 – 17:00"),
            ("Cocktails",   "17:00 – 00:45"),
            ("Piano",       "20:00 – 23:00, Wed–Sat"),
            ("Dress",       "Whatever you're in"),
            ("Last call",   "00:45"),
        ],
        voice_quote="A good hotel bar is a small living room that the whole hotel shares. You don't tell people how to sit or what to wear. You pour a proper drink, you remember what they had last night, and you never make anyone feel they're taking up space they haven't paid for.",
        voice_name="Yaren Kaya",
        voice_role="Head Bartender · Lobby Bar",
        voice_img=IMG_COCKTAIL,
        book_cta_label="Reserve at the bar",
        keys_prefix="din.lobby",
    )


PAGES = [
    {"path": "dining/index.html", "active": "dining",
     "title": "Dining & Bars · Mira Palace",
     "description": "Three settings, one Mediterranean philosophy — Mira Restaurant, the Pool Bar and the Lobby Bar. Turkish-Mediterranean plating, wood-fired pide, and cocktails until 01:00 at Mira Palace, Side.",
     "body": dining_index},
    {"path": "dining/main-restaurant.html", "active": "dining",
     "title": "Mira Restaurant · Mira Palace",
     "description": "The main dining room at Mira Palace — chef-led plated dinner with a rotating regional theme every evening, breakfast and lunch buffets, open kitchen onto the garden.",
     "body": main_restaurant},
    {"path": "dining/pool-bar.html", "active": "dining",
     "title": "Pool Bar · Mira Palace",
     "description": "Mediterranean poolside lunch at Mira Palace — mezze, wood-fired pide, grilled fish of the morning market, served under a pergola three metres from the water.",
     "body": pool_bar},
    {"path": "dining/lobby-bar.html", "active": "dining",
     "title": "Lobby Bar · Mira Palace",
     "description": "The lobby bar at Mira Palace — espresso in the morning, cocktails and live piano at night. Open every day 10:00 to 01:00.",
     "body": lobby_bar},
]
