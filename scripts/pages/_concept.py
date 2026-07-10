from common import hero, section, eyebrow, heading, lead, cta_band, PRICES

IMG_HERO = "https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=1920&q=80"
IMG_BREAK = "https://images.unsplash.com/photo-1504754524776-8f4f37790ca0?auto=format&fit=crop&w=1200&q=80"


def concept(root: str) -> str:
    included = [
        ("concept.inc1", "Dining", "Breakfast, lunch and dinner at the main restaurant. Light lunch at the pool restaurant. 24-hour in-room dining. One weekly à-la-carte dinner per stay (reservation required). Turkish afternoon tea with pastry. Late-night snack bar, 23:00–01:00."),
        ("concept.inc2", "Drinks", "Unlimited domestic and imported spirits, beers, wines, soft drinks, fresh juices, coffees, teas, and mineral water — all bars, all hours. House cocktail of the day. Fresh watermelon at the pool bar."),
        ("concept.inc3", "Pools & beach", "Both pools (outdoor and heated indoor). Sun loungers, mattresses, parasols, towels. Evrenseki Halk Plajı — the Blue-Flag public beach — is a seven-minute walk from reception."),
        ("concept.inc4", "Spa facilities", "Full use of the hammam complex: Turkish bath chamber, sauna, steam room, cold plunge, relaxation room. Two fitness classes per day (yoga, aqua-fit, stretch). Gym access, 06:00–22:00."),
        ("concept.inc5", "Entertainment", "Evening programme: live music twice a week, folk night, pianist in the lobby every evening. Adult animation team with a deliberately soft touch — no microphones at the pool."),
        ("concept.inc6", "Kids & families", "Kids' club (4–12 years), 10:00–17:00 with a break for lunch. In-room cot, high-chair at the restaurant, child menu. Teen lounge with console games, 14:00–22:00."),
    ]
    extras = [
        ("concept.ex1", "Premium spirits", "A short list of reserve spirits (single-malt, aged rum, vintage cognac) at a surcharge. The standard bar is all-inclusive."),
        ("concept.ex2", "À la carte", "One included per stay. Additional evenings are €35 per person."),
        ("concept.ex3", "Spa treatments", "Massages, rituals, facials and scrubs priced à la carte. Hammam and facilities included."),
        ("concept.ex4", "Laundry", "Per-item laundry and dry-cleaning, returned same day if before 10:00."),
        ("concept.ex5", "Airport transfer", f"Private VIP minibus from Antalya (60 km, ~45 minutes): €{PRICES['transfer_airport_private']} one way for up to four passengers. Shared shuttles from €{PRICES['transfer_airport_shared']}/person on request."),
        ("concept.ex6", "Excursions", "Concierge-arranged: Aspendos theatre, Manavgat waterfalls, boat to Alanya, Taurus mountain jeep safari."),
    ]
    schedule = [
        ("concept.sched1", "07:00–10:30", "Breakfast — open buffet, egg station, fresh juice bar"),
        ("concept.sched2", "10:30–12:00", "Late breakfast — continental corner at the lobby bar"),
        ("concept.sched3", "12:30–14:30", "Lunch — hot buffet at the main restaurant; wood-oven pizza at the pool"),
        ("concept.sched4", "15:30–17:00", "Turkish afternoon tea with baklava and şekerpare"),
        ("concept.sched5", "19:00–22:00", "Dinner — rotating themed buffets, weekly à la carte"),
        ("concept.sched6", "23:00–01:00", "Late-night snack bar — soup, meze, pides, desserts"),
        ("concept.sched7", "All day",     "Pool bar 10:00–00:00 · Lobby bar 10:00–01:00"),
    ]

    inc_cards = "".join(
        f'<div class="p-7 bg-white rounded-lg shadow-lux"><div class="text-xs uppercase tracking-widest text-sand-600" data-i18n="concept.tag.included">Included</div><h3 class="mt-2 font-display text-2xl text-mira-900" data-i18n="{key}.t">{k}</h3><p class="mt-3 text-mira-700 text-sm leading-relaxed" data-i18n="{key}.d">{v}</p></div>'
        for key, k, v in included
    )
    ex_cards = "".join(
        f'<div class="p-7 border border-mira-200 rounded-lg"><div class="text-xs uppercase tracking-widest text-mira-500" data-i18n="concept.tag.additional">Additional</div><h3 class="mt-2 font-display text-2xl text-mira-900" data-i18n="{key}.t">{k}</h3><p class="mt-3 text-mira-700 text-sm leading-relaxed" data-i18n="{key}.d">{v}</p></div>'
        for key, k, v in extras
    )
    sched_rows = "".join(
        f'<tr class="border-t border-mira-200"><td class="py-3 pr-6 font-medium text-mira-800 whitespace-nowrap" data-i18n="{key}.t">{t}</td><td class="py-3 text-mira-700" data-i18n="{key}.d">{d}</td></tr>'
        for key, t, d in schedule
    )

    h = hero(IMG_HERO,
             '<span data-i18n="concept.hero.kicker">All-Inclusive at Mira Palace</span>',
             '<span data-i18n="concept.hero.h1">Everything included.<br/>Nothing forgotten.</span>',
             '<span data-i18n="concept.hero.sub">Unlike many &#8216;all-inclusive&#8217; resorts, we do not down-grade the wine at lunch, hide the real menu behind an extras list, or bracelet you. What&#8217;s on this page is what&#8217;s in your stay.</span>',
             primary_href=f"{root}offers.html", primary_label='<span data-i18n="concept.hero.cta">See current offers</span>', height="70vh")

    a = section(f"""
      {eyebrow('What’s included in every rate')}
      {heading('Your stay, fully covered.')}
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-7 mt-12">{inc_cards}</div>
    """, bg="bg-sand-50")

    b = section(f"""
      {eyebrow('Daily rhythm')}
      {heading('A typical day, on the clock.', 3)}
      {lead('You are free to skip any and all of this — the spa is usually quieter around breakfast and the beach is at its best between 16:00 and sundown.')}
      <div class="mt-10 overflow-x-auto"><table class="w-full text-left"><tbody>{sched_rows}</tbody></table></div>
    """, bg="bg-white")

    c = section(f"""
      {eyebrow('What costs extra', 'text-sand-600')}
      {heading('The honest extras list.')}
      {lead('We keep it short on purpose. Everything below is clearly priced in your room, at the bar, and at the spa reception — no surprise on checkout.')}
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mt-10">{ex_cards}</div>
    """, bg="bg-sand-50")

    cta = cta_band("Ready to plan a stay?",
                   "Best rates are always direct. Write to us with your dates and we’ll get back with a quote and a few small extras reserved for direct guests.",
                   f"{root}contact.html#enquiry", "Send an enquiry", IMG_BREAK)

    return h + a + b + c + cta


PAGES = [
    {"path": "concept.html", "active": "concept",
     "title": "All-Inclusive Concept · Mira Palace",
     "description": "Exactly what's included in your stay at Mira Palace — meals, drinks, pools, beach, hammam, entertainment — and the short honest list of what isn't.",
     "body": concept},
]
