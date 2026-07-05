from common import hero, section, eyebrow, heading, PRICES

IMG_ACT = "https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&w=1920&q=80"
IMG_KIDS = "https://images.unsplash.com/photo-1596394516093-501ba68a0ba6?auto=format&fit=crop&w=1600&q=80"
IMG_EVE = "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&w=1600&q=80"
IMG_SIDE = "https://images.unsplash.com/photo-1589489873962-88a30d7aa96c?auto=format&fit=crop&w=1920&q=80"
IMG_MAP = "https://images.unsplash.com/photo-1524661135-423995f22d0b?auto=format&fit=crop&w=1600&q=80"
# R023: airport-transfer VIP MINIBUS (Mercedes V-Class / Vito Tourer, black
# executive fit-out — the vehicle actually used for Antalya-Alanya VIP
# transfers). Was: a passenger-car sedan Unsplash shot that didn't match
# the "minibus" description in the copy. This image + a wide-search
# minibus fallback both point to Unsplash's stable CDN.
IMG_VAN = "https://images.unsplash.com/photo-1571043733612-d5444ff5d766?auto=format&fit=crop&w=1600&q=80"
# Nearby experiences for the "Beyond the gates" gallery.
IMG_ASPENDOS = "https://images.unsplash.com/photo-1518709268805-4e9042af2176?auto=format&fit=crop&w=1200&q=80"
IMG_FALLS    = "https://images.unsplash.com/photo-1467810563316-b5476525c0f9?auto=format&fit=crop&w=1200&q=80"
IMG_HARBOR   = "https://images.unsplash.com/photo-1583244532610-2a234b5b8e7a?auto=format&fit=crop&w=1200&q=80"


def activities(root: str) -> str:
    """Activities holding page — content disabled in R007.

    The original daily programme + kids' club + wellness blocks live in
    git history; restore by reverting the R007 commit when the activities
    programme is ready to publish."""
    h = hero(IMG_ACT,
             '<span data-i18n="activities.hero.kicker">Activities &amp; entertainment</span>',
             '<span data-i18n="activities.hero.h1">Coming soon.</span>',
             '<span data-i18n="activities.hero.sub">Our activities programme is being polished before launch — kids\' club, daily wellness classes and an evening line-up are on their way. Pools, beach, spa, dining and the All-Inclusive concept are all live; come back here in a few weeks for the full schedule.</span>',
             height="62vh")
    body = section(f"""
      <div class="max-w-2xl mx-auto text-center">
        <p class="uppercase tracking-[0.22em] text-sand-600 text-xs font-semibold" data-i18n="activities.body.kicker">Coming soon</p>
        <h2 class="font-display text-4xl sm:text-5xl text-mira-900 mt-3 leading-tight" data-i18n="activities.body.h2">An activities programme worth waiting for.</h2>
        <p class="mt-6 text-mira-700 leading-relaxed" data-i18n="activities.body.p1">
          We're working with the hotel team on a deliberately soft daily programme — wellness classes by the pool, a kids' club for guests with children, live acoustic music in the lobby before dinner, and themed evenings twice a week.
          Until that's finalised, we've taken this page down to avoid sharing dates and times we can't guarantee.
        </p>
        <p class="mt-6 text-mira-700 leading-relaxed">
          <span data-i18n="activities.body.p2_pre">In the meantime, the rest of the experience is fully live:</span>
          <a href="{root}rooms/" class="underline underline-offset-2 text-sand-600 hover:text-sand-500" data-i18n="activities.body.p2.explore">explore the suites</a>,
          <a href="{root}concept.html" class="underline underline-offset-2 text-sand-600 hover:text-sand-500" data-i18n="activities.body.p2.concept">read about our All-Inclusive concept</a>,
          <span>or</span>
          <a href="{root}book.html" class="underline underline-offset-2 text-sand-600 hover:text-sand-500" data-i18n="activities.body.p2.book">book a stay</a><span data-i18n="activities.body.p2_post">, and we'll send the full activities schedule to you a week before arrival.</span>
        </p>
        <div class="mt-10 inline-flex items-center gap-2 px-5 py-3 bg-sand-100 border border-sand-300/50 rounded-full text-sm text-mira-800">
          <span class="w-2 h-2 rounded-full bg-sand-400"></span>
          <span data-i18n="activities.body.chip">Want to know the moment it goes live?</span> <a href="{root}contact.html" class="ml-1 underline underline-offset-2 font-medium hover:text-mira-900" data-i18n="activities.body.chip.cta">Drop us a line.</a>
        </div>
      </div>
    """, bg="bg-white")
    return h + body


def location(root: str) -> str:
    # R023: removed "Mediterranean beach (private)" (there is no private
    # beach — the nearest is Evrenseki Halk Plajı, a Blue-Flag public
    # beach ~700 m down the lane), and removed the fabricated
    # "complimentary shuttle twice daily to Side" — Side is a taxi ride.
    distances = [
        ("Evrenseki Halk Plajı (public, Blue Flag)", "700 m", "~7-minute walk down the cypress-lined lane; sand, sunbeds, kiosks on the front"),
        ("Evrenseki village centre", "1.5 km", "Small bakery, pharmacy, ATM, Saturday market"),
        ("Side old town (ancient harbour, Apollo temple)", "12 km", "15–20 minutes by taxi"),
        ("Manavgat waterfalls", "18 km", "25 minutes by car; popular half-day excursion"),
        ("Aspendos Roman theatre", "33 km", "45 minutes; summer evening performances"),
        ("Antalya International Airport (AYT)", "60 km", "~45 minutes; private transfer arranged on request"),
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
    # R023: transfer block — swapped Mercedes Vito car copy + image to
    # VIP minibus (the actual vehicle used on Antalya-Alanya routes).
    # Prices now pull from PRICES so a one-line edit changes them everywhere.
    b = section(f"""
      <div class="grid lg:grid-cols-2 gap-10 items-center">
        <div>{eyebrow('From the airport')}
          {heading('Transfer options.', 3)}
          <ul class="mt-6 space-y-4 text-mira-700">
            <li><span class="font-semibold text-mira-900">Private VIP minibus:</span> €{PRICES['transfer_airport_private']} one way for up to four passengers, with waiting time included. Executive-fit minibus (Mercedes V-Class or equivalent) — the same vehicle used on the popular Antalya–Alanya VIP transfer route. Arrange on booking or on arrival.</li>
            <li><span class="font-semibold text-mira-900">Shared shuttle:</span> €{PRICES['transfer_airport_shared']} per person, subject to availability, routed with other Mira Palace arrivals. Journey time 75–90 minutes.</li>
            <li><span class="font-semibold text-mira-900">Taxi:</span> approx. €70 one way; we recommend booking via the hotel to agree the fare in advance.</li>
            <li><span class="font-semibold text-mira-900">Self-drive:</span> ~45 minutes via the D-400 coast road. Complimentary hotel parking.</li>
          </ul>
        </div>
        <div class="relative">
          <div class="aspect-[4/3] rounded-lg bg-cover bg-center shadow-lux" style="background-image:url('{IMG_VAN}')"></div>
          <div class="absolute bottom-4 left-4 bg-white/90 backdrop-blur px-4 py-2 rounded shadow-lux">
            <div class="text-[10px] uppercase tracking-widest text-mira-600">VIP MINIBUS</div>
            <div class="text-sm font-medium text-mira-900">Antalya airport transfer</div>
          </div>
        </div>
      </div>
    """, bg="bg-sand-50")
    # R025: Nearby treasures — real Wikimedia Commons images sourced by the
    # travel SME research, with two-sentence verified copy for each site.
    # All four images are CC BY-SA — the /credits page (added in R025) lists
    # each photographer for licence compliance. Two [VERIFY] items flagged
    # for owner: Aspendos 2026 opera festival dates and Manavgat 2026
    # entrance fee — do NOT publish specific numbers on those without owner
    # confirmation.
    IMG_APOLLO_TEMPLE  = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Apollon_Tempel_in_Side.jpg/1600px-Apollon_Tempel_in_Side.jpg"
    IMG_ASPENDOS_R025  = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Aspendos_02.jpg/1600px-Aspendos_02.jpg"
    IMG_MANAVGAT_R025  = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Manavgat_waterfall_by_tomgensler.JPG/1600px-Manavgat_waterfall_by_tomgensler.JPG"
    IMG_KALEICI_R025   = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Antalya_-_Kalei%C3%A7i.JPG/1600px-Antalya_-_Kalei%C3%A7i.JPG"

    nearby = [
        (IMG_APOLLO_TEMPLE, "Side & the temple of Apollo",
         "12 km — five sunlit marble columns rising straight out of the Mediterranean, at the tip of Side's old-town peninsula. Come 45 minutes before sunset: the marble turns honey-gold, the tourist coaches have left, and the little fishing harbour behind you fills up for dinner."),
        (IMG_ASPENDOS_R025, "Aspendos Roman theatre",
         "33 km — the best-preserved Roman theatre anywhere in the ancient world, built in 155 AD and still standing almost exactly as Marcus Aurelius left it. The acoustics are so intact that a coin dropped centre-stage is audible from the top row — try it before the tour groups arrive around 10 am."),
        (IMG_MANAVGAT_R025, "Manavgat waterfalls",
         "18 km — a wide, low curtain of turquoise water dropping across the full breadth of the Manavgat River, ringed by tea gardens under plane trees. Go mid-morning when the sun is behind you and the river-boat crowds haven't arrived — order a glass of çay on the terrace and stay for lunch."),
        (IMG_KALEICI_R025, "Antalya old town (Kaleiçi)",
         "65 km — the walled Ottoman old town wrapped around a horseshoe harbour of wooden gulets, best entered on foot through Hadrian's Gate. Lose an afternoon on the cobbled lanes behind the harbour, then take the clifftop lift down to Mermerli beach for a swim before the drive back."),
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
