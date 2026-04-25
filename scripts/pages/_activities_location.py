from common import hero, section, eyebrow, heading

IMG_ACT = "https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&w=1920&q=80"
IMG_KIDS = "https://images.unsplash.com/photo-1596394516093-501ba68a0ba6?auto=format&fit=crop&w=1600&q=80"
IMG_EVE = "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&w=1600&q=80"
IMG_SIDE = "https://images.unsplash.com/photo-1589489873962-88a30d7aa96c?auto=format&fit=crop&w=1920&q=80"
IMG_MAP = "https://images.unsplash.com/photo-1524661135-423995f22d0b?auto=format&fit=crop&w=1600&q=80"
# A black Mercedes — stands in for the airport-transfer Vito.
IMG_VAN = "https://images.unsplash.com/photo-1494976388531-d1058494cdd8?auto=format&fit=crop&w=1600&q=80"
# Nearby experiences for the "Beyond the gates" gallery.
IMG_ASPENDOS = "https://images.unsplash.com/photo-1518709268805-4e9042af2176?auto=format&fit=crop&w=1200&q=80"
IMG_FALLS    = "https://images.unsplash.com/photo-1467810563316-b5476525c0f9?auto=format&fit=crop&w=1200&q=80"
IMG_HARBOR   = "https://images.unsplash.com/photo-1583244532610-2a234b5b8e7a?auto=format&fit=crop&w=1200&q=80"


def activities(root: str) -> str:
    daily = [
        ("09:00", "Morning yoga (pool deck)",      "Beginners welcome. Mats provided. 45 min."),
        ("10:30", "Aqua-fit class",                "In the main pool. 30 min."),
        ("11:30", "Kids’ club opens",         "Age 4–12. Art, games, short walks, swim coaching."),
        ("14:00", "Pilates / stretch (studio)",    "Level 1–2. 45 min."),
        ("15:00", "Darts / table tennis tournament","Prizes for the winners. Every afternoon."),
        ("16:30", "Beach volleyball",              "Friendly, on the beach-club court."),
        ("18:00", "Live acoustic guitar, lobby bar", "30 min, then a set break before dinner."),
        ("21:30", "Evening programme",             "Varies by night — live music, folk night, themed DJ, cinema under the stars."),
    ]
    rows = "".join(
        f'<tr class="border-t border-mira-200"><td class="py-4 pr-6 font-medium text-mira-900 whitespace-nowrap">{t}</td><td class="py-4 pr-6 text-mira-800">{n}</td><td class="py-4 text-mira-600 text-sm">{d}</td></tr>'
        for t, n, d in daily
    )
    h = hero(IMG_ACT, "Activities & entertainment",
             "Do as much or as little as you like.",
             "A deliberately soft programme: no microphones at the pool, no mandatory animation, but enough going on that you never look for something to do. Kids' club, evening entertainment, wellness classes.", height="68vh")
    a = section(f"""
      {eyebrow('A typical day')}
      {heading('Today’s programme.', 3)}
      <div class="mt-8 overflow-x-auto"><table class="w-full text-left"><tbody>{rows}</tbody></table></div>
      <p class="mt-8 text-xs text-mira-500 italic">Programme rotates weekly. A full schedule is posted each Sunday on your room TV and at the lobby.</p>
    """, bg="bg-white")
    cards = [
        (IMG_KIDS, "Kids’ club (4–12)", "Our kids’ team runs a daily programme from 10:30 to 17:00 with a lunch break. Art, games, short nature walks, swim coaching, a weekly movie-and-popcorn afternoon. Parents can drop in any time."),
        (IMG_ACT, "Wellness classes", "Two classes a day — yoga, pilates, aqua-fit, stretch. Levels are labelled. Mats, blocks, straps and weights are all provided."),
        (IMG_EVE, "Evenings", "Live acoustic music before dinner. Piano in the lobby every evening. Twice a week, a guest performer: jazz duo, Turkish folk, or a string trio from the Antalya conservatoire."),
    ]
    blocks = "".join(
        f'<div class="grid md:grid-cols-2 gap-8 items-center"><div class="aspect-[4/3] bg-cover bg-center rounded-lg shadow-lux" style="background-image:url(\'{img}\')"></div><div><h3 class="font-display text-3xl text-mira-900">{t}</h3><p class="mt-4 text-mira-700 leading-relaxed">{d}</p></div></div>'
        for img, t, d in cards
    )
    b = section(f"""
      <div class="space-y-16">{blocks}</div>
    """, bg="bg-sand-50")
    return h + a + b


def location(root: str) -> str:
    distances = [
        ("Mediterranean beach (private)", "600 m", "8–10 min walk on a cypress lane, or a 3-minute shuttle every half hour"),
        ("Evrenseki village centre", "1.5 km", "Small bakery, pharmacy, ATM, Saturday market"),
        ("Side old town (ancient harbour, Apollo temple)", "12 km", "15–20 minutes by taxi; complimentary shuttle twice daily"),
        ("Manavgat waterfalls", "18 km", "25 minutes by car; popular half-day excursion"),
        ("Aspendos Roman theatre", "33 km", "45 minutes; summer evening performances"),
        ("Antalya International Airport (AYT)", "60 km", "45–60 minutes; private transfer arranged on request"),
        ("Alanya castle", "65 km", "75 minutes east along the coast"),
        ("Köprülü Canyon (rafting)", "55 km", "1 hour; full-day white-water excursion available"),
    ]
    rows = "".join(
        f'<tr class="border-t border-mira-200"><td class="py-4 pr-6 font-medium text-mira-900">{n}</td><td class="py-4 pr-6 text-mira-800 whitespace-nowrap">{d}</td><td class="py-4 text-mira-600 text-sm">{note}</td></tr>'
        for n, d, note in distances
    )
    h = hero(IMG_SIDE, "Location & transfers",
             "On the edge of Side.<br/>Halfway along the Turkish Riviera.",
             "Mira Palace is in Evrenseki, between Side and Manavgat — central enough to reach the major sights in under an hour, quiet enough that you can hear the sea from the terrace.", height="70vh")
    a = section(f"""
      {eyebrow('Getting around')}
      {heading('Distances from the hotel.')}
      <div class="mt-8 overflow-x-auto"><table class="w-full text-left"><tbody>{rows}</tbody></table></div>
    """, bg="bg-white")
    # Transfer block — text on the left, hero image of the Vito on the right.
    b = section(f"""
      <div class="grid lg:grid-cols-2 gap-10 items-center">
        <div>{eyebrow('From the airport')}
          {heading('Transfer options.', 3)}
          <ul class="mt-6 space-y-4 text-mira-700">
            <li><span class="font-semibold text-mira-900">Private transfer:</span> €85 one way for up to four passengers in a Mercedes Vito, with waiting included. Arrange on booking or on arrival.</li>
            <li><span class="font-semibold text-mira-900">Shared shuttle:</span> €25 per person, subject to availability, routed with other Mira Palace arrivals. Journey time 75–90 minutes.</li>
            <li><span class="font-semibold text-mira-900">Taxi:</span> approx. €70 one way; we recommend booking via the hotel to agree the fare in advance.</li>
            <li><span class="font-semibold text-mira-900">Self-drive:</span> 45–60 minutes via the D-400 coast road. Complimentary hotel parking.</li>
          </ul>
        </div>
        <div class="relative">
          <div class="aspect-[4/3] rounded-lg bg-cover bg-center shadow-lux" style="background-image:url('{IMG_VAN}')"></div>
          <div class="absolute bottom-4 left-4 bg-white/90 backdrop-blur px-4 py-2 rounded shadow-lux">
            <div class="text-[10px] uppercase tracking-widest text-mira-600">Mercedes-Benz</div>
            <div class="text-sm font-medium text-mira-900">Private airport transfer</div>
          </div>
        </div>
      </div>
    """, bg="bg-sand-50")
    # Nearby treasures gallery — gives the page the same visual cadence as
    # Rooms / Dining / Spa.
    nearby = [
        (IMG_SIDE,     "Side & the temple of Apollo",
         "12 km — wander the ancient harbour at golden hour, then dinner along the seafront promenade."),
        (IMG_ASPENDOS, "Aspendos Roman theatre",
         "33 km — one of antiquity's best-preserved theatres; opera and ballet evenings in summer."),
        (IMG_FALLS,    "Manavgat waterfalls",
         "18 km — a wide curtain of cool water on the Manavgat river, breakfast cafés on the bank."),
        (IMG_HARBOR,   "Antalya old town (Kaleiçi)",
         "65 km — Roman, Seljuk and Ottoman layers wrapped around the small marina."),
    ]
    cards = "".join(
        f'<a class="group block bg-white rounded-lg overflow-hidden shadow-lux hover:-translate-y-1 transition will-change-transform">'
        f'<div class="aspect-[4/3] bg-cover bg-center transition group-hover:scale-[1.04]" style="background-image:url(\'{img}\')"></div>'
        f'<div class="p-6"><h3 class="font-display text-xl text-mira-900">{t}</h3>'
        f'<p class="mt-2 text-sm text-mira-700 leading-relaxed">{d}</p></div></a>'
        for img, t, d in nearby
    )
    c = section(f"""
      {eyebrow('Beyond the gates')}
      {heading('Nearby treasures, easy half-days.')}
      <div class="mt-10 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">{cards}</div>
    """, bg="bg-white")
    # Map embed — wrapped in a polished frame so it looks like part of the
    # page rather than a raw widget.
    d = section(f"""
      <div class="grid lg:grid-cols-3 gap-10 items-start">
        <div class="lg:col-span-1">
          {eyebrow('Find us')}
          {heading('On the map.', 3)}
          <p class="mt-4 text-mira-700 leading-relaxed">Evrenseki Mahallesi, between Side and Manavgat. The map below is interactive — drag, zoom, or open in Google Maps for turn-by-turn directions.</p>
          <a href="https://maps.app.goo.gl/psUsJCW22broH4nQ8" target="_blank" rel="noopener" class="mt-5 inline-flex items-center gap-2 px-4 py-2 bg-mira-900 text-white text-sm rounded-full hover:bg-mira-800 transition">
            Open in Google Maps
            <svg viewBox="0 0 20 20" class="w-4 h-4" fill="currentColor"><path d="M11 3a1 1 0 100 2h2.586L8.293 10.293a1 1 0 101.414 1.414L15 6.414V9a1 1 0 102 0V4a1 1 0 00-1-1h-5z"/><path d="M5 5a2 2 0 00-2 2v8a2 2 0 002 2h8a2 2 0 002-2v-3a1 1 0 10-2 0v3H5V7h3a1 1 0 100-2H5z"/></svg>
          </a>
        </div>
        <div class="lg:col-span-2">
          <iframe src="https://www.google.com/maps?q=36.7748,31.3888&amp;hl=en&amp;z=12&amp;output=embed" class="w-full aspect-[16/10] rounded-lg shadow-lux border-0" loading="lazy" title="Map of Mira Palace"></iframe>
          <p class="mt-3 text-xs text-mira-600">Approximate location shown; the detailed directions sent with your booking confirmation are authoritative.</p>
        </div>
      </div>
    """, bg="bg-sand-50")
    return h + a + b + c + d


PAGES = [
    {"path": "activities.html", "active": "activities",
     "title": "Activities & entertainment · Mira Palace",
     "description": "Daily programme, kids' club, wellness classes, and evening entertainment at Mira Palace.",
     "body": activities},
    {"path": "location.html", "active": "location",
     "title": "Location & transfers · Mira Palace",
     "description": "Where Mira Palace is — distances to Side, Manavgat, Aspendos, Antalya airport, and transfer options.",
     "body": location},
]
