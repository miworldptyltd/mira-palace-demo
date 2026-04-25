from common import hero, section, eyebrow, heading, card

IMG_MAIN = "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=1600&q=80"
IMG_POOL = "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?auto=format&fit=crop&w=1600&q=80"
IMG_LOBBY = "https://images.unsplash.com/photo-1470337458703-46ad1756a187?auto=format&fit=crop&w=1600&q=80"
IMG_BREAK = "https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=1200&q=80"
IMG_BAR = "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&w=1200&q=80"
IMG_FOOD = "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=1200&q=80"


def dining_index(root: str) -> str:
    h = hero(IMG_MAIN, "Dining",
             "Four outlets. One kitchen.<br/>Thirty-four guests watching.",
             "A restaurant small enough that the chef plates every pass, a pool grill that does nothing except pide and wood-fired pizza extraordinarily well, and two bars with long wine lists.",
             height="70vh")
    body = section(f"""
      {eyebrow('Where to eat and drink')}
      {heading('Our dining rooms.')}
      <div class="grid md:grid-cols-2 gap-7 mt-12">
        {card(IMG_MAIN, "Mira — main restaurant", "The indoor dining room. Open buffet for breakfast and lunch; plated à-la-carte-style dinner with a rotating themed menu each evening.", f"{root}dining/main-restaurant.html", "View the restaurant")}
        {card(IMG_POOL, "Deniz — pool restaurant", "Casual lunch by the pool. Wood-fired pide and pizza, a mezze bar, salads, grilled fish of the day, and ice-cream cart in the afternoon.", f"{root}dining/pool-bar.html", "View the pool restaurant")}
        {card(IMG_LOBBY, "Lobby bar", "All-day and late-night. Coffee and pastries in the morning, cocktails and piano after dark. Open 10:00–01:00.", f"{root}dining/lobby-bar.html", "View the lobby bar")}
        {card(IMG_BAR, "Orchard bar", "Our pool bar — fresh juices and smoothies in the day, classic cocktails in the late afternoon, and the hotel’s best sundowner spot. Open 10:00–00:00.", f"{root}dining/lobby-bar.html", "At the pool")}
      </div>
    """, bg="bg-sand-50", id="dining-rooms")
    starters = [
        ("Grilled octopus", "white-bean purée, pul biber oil"),
        ("Chilled tomato &amp; pomegranate soup", "basil granita, dill"),
        ("Warm halloumi", "walnut &amp; rocket salad, sumac vinaigrette"),
        ("Smoked aubergine", "yoghurt, walnuts, pomegranate seeds"),
    ]
    woodfired = [
        ("Whole sea bass", "lemon, thyme, olive oil"),
        ("Dorade in salt crust", "for two — cracked at the table"),
        ("Lamb shoulder", "pomegranate molasses, bulgur, fennel"),
        ("Wood-fired pide", "minced lamb &amp; tomato, or four cheese"),
    ]
    mains = [
        ("Chicken şiş", "garlic yoghurt, pilav, chilli butter"),
        ("Slow-braised beef cheek", "mashed potato, roasted shallots, jus"),
        ("Vegetable moussaka", "pine nuts, feta, oregano"),
        ("Saffron risotto", "seafood of the day, lemon zest"),
    ]
    desserts = [
        ("Baklava", "with kaymak and pistachio"),
        ("Poached quince", "clotted cream, walnut praline"),
        ("Antalya cheese plate", "fig jam, honeycomb, walnut bread"),
        ("Turkish coffee &amp; lokum", "the way it should be"),
    ]
    def book_section(title, items):
        rows = "".join(
            f'<div class="menu-row"><div class="name">{n}</div><div class="desc">{d}</div></div>'
            for n, d in items
        )
        return f'<section class="menu-section"><h4 class="menu-section-title">{title}</h4>{rows}</section>'

    sample = section(f"""
      <span id="sample-menu" class="block -mt-24 pt-24" aria-hidden="true"></span>
      {eyebrow('Sample evening menu')}
      {heading('Tonight at Mira.', 3)}
      <div class="mt-10 max-w-3xl mx-auto">
        <div class="menu-card rounded-md">
          <h3>Mira Restaurant</h3>
          <span class="menu-tag">A Monday in May · From the chef</span>
          {book_section("To start", starters)}
          {book_section("From the wood oven", woodfired)}
          {book_section("Mains", mains)}
          {book_section("To finish", desserts)}
          <p class="mt-10 text-center text-xs italic" style="color:var(--mira-700); font-family:Inter,sans-serif; letter-spacing:.05em;">Menu rotates weekly · vegan, gluten-free and allergy adjustments are made by the chef on the day · just say a word at the maître d'.</p>
        </div>
      </div>
    """, bg="bg-white")
    return h + body + sample


def main_restaurant(root: str) -> str:
    h = hero(IMG_MAIN, "Mira — main restaurant", "Mira restaurant.",
             "The indoor dining room. Open buffet for breakfast and lunch, and a plated, menu-led dinner with a rotating theme every evening.", height="68vh")
    body = section(f"""
      <div class="grid lg:grid-cols-12 gap-12">
        <div class="lg:col-span-7 text-mira-700 leading-relaxed text-lg space-y-5">
          <p>The main restaurant seats sixty at full capacity, which means even a full house fits in one service. Breakfast is a proper open-kitchen buffet: an egg station, a fresh-juice bar, a hot corner with simit, menemen and sucuklu yumurta, a bread station, and an espresso machine we take seriously.</p>
          <p>Lunch is similar, lighter, with the soup and grilled station leading. Dinner is the evening’s theme — a different country or region of Türkiye each night — plated and served with a wine pairing if you want it.</p>
          <p>We don’t fuss over dress code. Flip-flops are fine at breakfast; at dinner, most guests change into something light. Nothing that requires a jacket.</p>
        </div>
        <aside class="lg:col-span-5">
          <div class="bg-white rounded-lg shadow-lux p-7">
            <h3 class="font-display text-2xl text-mira-900">Service times</h3>
            <dl class="mt-5 grid grid-cols-2 gap-y-3 text-sm">
              <dt class="text-mira-600">Breakfast</dt><dd class="text-right font-medium">07:00 – 10:30</dd>
              <dt class="text-mira-600">Late breakfast</dt><dd class="text-right font-medium">10:30 – 12:00 (lobby)</dd>
              <dt class="text-mira-600">Lunch</dt><dd class="text-right font-medium">12:30 – 14:30</dd>
              <dt class="text-mira-600">Dinner</dt><dd class="text-right font-medium">19:00 – 22:00</dd>
              <dt class="text-mira-600">À la carte night</dt><dd class="text-right font-medium">Fri &amp; Sat · booking</dd>
              <dt class="text-mira-600">Dress</dt><dd class="text-right font-medium">Smart casual at dinner</dd>
            </dl>
            <a href="{root}concept.html" class="mt-5 inline-flex items-center gap-2 text-sm font-medium text-mira-700 hover:text-sand-600">What’s included →</a>
          </div>
        </aside>
      </div>
    """, bg="bg-white")
    gallery = section(f"""
      <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{IMG_BREAK}')"></div>
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{IMG_FOOD}')"></div>
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{IMG_MAIN}')"></div>
        <div class="aspect-[4/5] bg-cover bg-center rounded" style="background-image:url('{IMG_POOL}')"></div>
      </div>
    """, bg="bg-sand-50")
    return h + body + gallery


def pool_bar(root: str) -> str:
    h = hero(IMG_POOL, "Deniz — pool restaurant", "Deniz — by the pool.",
             "Our casual lunch by the main pool. Wood-fired pide and pizza, a mezze bar, grilled fish, salads — and an ice-cream cart between 15:00 and 17:00 that always runs out of pistachio.", height="68vh")
    body = section(f"""
      <div class="grid lg:grid-cols-12 gap-12">
        <div class="lg:col-span-7 text-mira-700 leading-relaxed text-lg space-y-5">
          <p>Open only for lunch (the main restaurant handles dinner), Deniz is deliberately informal. You can walk up in your swimsuit, a sarong or a towel — the chef will plate your pide just the same.</p>
          <p>The heart of the space is the mezze bar: twenty small dishes, changing daily — grilled aubergine, haydari, ezme, cacık, piyaz, muhammara, fried artichokes, chickpea salad, tarama. The centrepiece is a wood oven that turns out pides to order — minced lamb, spinach and feta, four-cheese, ispanaklı — and a handful of pizzas for the children.</p>
          <p>There is a grill for fish. Dorade, sea bass, calamari, octopus when the morning market has it. A simple side salad, lemon, olive oil. Eaten under a pergola heavy with jasmine in July.</p>
        </div>
        <aside class="lg:col-span-5">
          <div class="bg-white rounded-lg shadow-lux p-7">
            <h3 class="font-display text-2xl text-mira-900">At a glance</h3>
            <dl class="mt-5 grid grid-cols-2 gap-y-3 text-sm">
              <dt class="text-mira-600">Lunch</dt><dd class="text-right font-medium">12:30 – 14:30</dd>
              <dt class="text-mira-600">Ice cream</dt><dd class="text-right font-medium">15:00 – 17:00</dd>
              <dt class="text-mira-600">Seating</dt><dd class="text-right font-medium">Pergola, 40 covers</dd>
              <dt class="text-mira-600">Dress</dt><dd class="text-right font-medium">Anything, really</dd>
              <dt class="text-mira-600">Kids’ menu</dt><dd class="text-right font-medium">Yes</dd>
            </dl>
          </div>
        </aside>
      </div>
    """, bg="bg-white")
    return h + body


def lobby_bar(root: str) -> str:
    h = hero(IMG_LOBBY, "Lobby &amp; Orchard bars", "Two bars, one late night.",
             "The Lobby Bar opens for espresso at 10:00 and stays open until 01:00. The Orchard Bar, by the main pool, runs until midnight. Between them they cover the whole day.", height="66vh")
    drinks = [
        ("House cocktails",
         ["Rakı Sour — rakı, lemon, egg-white, cherry",
          "Side Spritz — bitter orange, prosecco, thyme",
          "Pomegranate Sour — pomegranate molasses, vodka, lime",
          "Orchard Mojito — fresh mint, basil, white rum, lime"]),
        ("Wine list (All-Inclusive)",
         ["Doluca Kav — white, Emir grape, Cappadocia",
          "Kavaklıdere Yakut — red blend, Anatolia",
          "Sevilen Majestic — rosé, İzmir",
          "Prosecco DOC — by the glass or bottle"]),
        ("Reserve list (extra charge)",
         ["Corvus Rüzgar — premium Turkish red",
          "Billecart-Salmon Brut Reserve champagne",
          "The Balvenie 14 DoubleWood",
          "Rémy Martin VSOP"]),
    ]
    blocks = "".join(
        f'<div class="p-7 bg-white rounded-lg shadow-lux"><h3 class="font-display text-2xl text-mira-900">{t}</h3><ul class="mt-4 space-y-2 text-sm text-mira-700">{"".join(f"<li>{i}</li>" for i in items)}</ul></div>'
        for t, items in drinks
    )
    body = section(f"""
      {eyebrow('On the menu')}
      {heading('A short list of what we make well.', 3)}
      <div class="grid md:grid-cols-3 gap-7 mt-10">{blocks}</div>
      <p class="mt-8 text-xs text-mira-500 italic">Reserve list is charged per serve and billed on checkout. Everything else is included in your All-Inclusive stay.</p>
    """, bg="bg-sand-50")
    return h + body


PAGES = [
    {"path": "dining/index.html", "active": "dining",
     "title": "Dining · Mira Palace",
     "description": "Four dining outlets at Mira Palace — main restaurant, pool restaurant, lobby bar, orchard bar.",
     "body": dining_index},
    {"path": "dining/main-restaurant.html", "active": "dining",
     "title": "Mira main restaurant · Mira Palace",
     "description": "The main restaurant at Mira Palace — breakfast and lunch open buffet, evening menu-led dinner with weekly themes.",
     "body": main_restaurant},
    {"path": "dining/pool-bar.html", "active": "dining",
     "title": "Pool restaurant (Deniz) · Mira Palace",
     "description": "Casual poolside lunch with wood-fired pide and pizza, mezze bar, grilled fish.",
     "body": pool_bar},
    {"path": "dining/lobby-bar.html", "active": "dining",
     "title": "Lobby & Orchard bars · Mira Palace",
     "description": "All-day and late-night bars at Mira Palace — coffee, cocktails, wine list, reserve spirits.",
     "body": lobby_bar},
]
