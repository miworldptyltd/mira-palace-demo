"""Booking page — rebuild for R006.

Layout (desktop md+):
  Slim title bar > Suite tabs > Two-column main:
    LEFT  = booking form (dates, guests, contact, expandable add-ons, total, submit)
    RIGHT = hero photo, info cards (Basics / Capacity / Amenities), photo tile grid

Layout (mobile <md):
  Stacks single column. VISUALS show first (hero + info + tiles) so the guest sees
  what they're booking; FORM follows below.

All prices are illustrative placeholders. In R010 the admin panel writes real
prices into the DB; this page reads from a JSON blob set by site.js. For now
the placeholders live in BOOK_DATA below and are mirrored into window.BOOK_DATA
via inline <script> so the front-end can swap currencies without a rebuild.
"""
from __future__ import annotations
import json
from common import SITE_META, PRICES, FX_RATES, price as _p

# --- Suite data ------------------------------------------------------------
# Each suite pulls its rate from the central PRICES dict in common.py.
# (R023: was 4 sets of hardcoded TRY/EUR/USD numbers scattered here — now
# every published price is defined in one place and converted on the fly.)

def _prices(key: str) -> dict:
    """Build the {try, eur, usd} triple from the EUR base in PRICES."""
    return {"try": _p(key, "try"), "eur": PRICES[key], "usd": _p(key, "usd")}


SUITES = {
    "standard": {
        "name": "Standard Suite",
        # R023: added A4/A5/B4/B5 (previously unaccounted) — total 19 rooms.
        "rooms_label": "A4, A5, B4, B5 + C1–C15 · 19 rooms",
        "sub": "Garden-facing comfort · sleeps 2",
        "prices": _prices("room_standard"),
        "photos": [
            ("assets/img/standard/standard-01.webp", "Bedroom"),
            ("assets/img/standard/standard-04.webp", "Bed detail"),
            ("assets/img/standard/standard-06.webp", "Bathroom"),
            ("assets/img/standard/standard-09.webp", "Wardrobe"),
            ("assets/img/standard/standard-12.webp", "Garden view"),
            ("assets/img/standard/standard-14.webp", "Entrance"),
        ],
        "basics": [
            ("Rooms", "A4, A5, B4, B5, C1–C15"),
            ("Type", "Standard"),
            ("Size", "22 m²"),
            ("Floor", "Ground / 1st"),
            ("View", "Garden"),
            ("Available", "19 of 19"),
        ],
        "capacity": [
            ("Adults", "Up to 2"),
            ("Children", "Up to 1"),
            ("Queen bed", "1"),
            ("Sofa bed", "0"),
            ("Cot", "On request"),
            ("Smoking", "Non-smoking"),
        ],
        "amenities": [
            ("wifi", "Wi-Fi"), ("snowflake", "Air-con"), ("bath", "Marble bath"),
            ("flower", "Garden"), ("coffee", "Kettle"), ("device-tv", "Smart TV"),
            ("lock", "Safe"), ("glass", "Minibar"), ("hanger", "Wardrobe"),
            ("wind", "Hair dryer"),
        ],
    },
    "deluxe": {
        "name": "Deluxe Suite",
        "rooms_label": "A1, A2, A3, A7 + B1, B2, B3, B6, B7, B10 · 10 rooms",
        "sub": "Sea view · kitchenette in most · sleeps 2",
        "prices": _prices("room_deluxe"),
        "photos": [
            ("assets/img/deluxe/deluxe-01.webp", "Bedroom"),
            ("assets/img/deluxe/deluxe-04.webp", "Sitting area"),
            ("assets/img/deluxe/deluxe-08.webp", "Marble bath"),
            ("assets/img/deluxe/deluxe-10.webp", "Sea view"),
            ("assets/img/deluxe/deluxe-16.webp", "Kitchenette"),
            ("assets/img/deluxe/deluxe-22.webp", "Balcony"),
        ],
        "basics": [
            ("Rooms", "A1, A2, A3, A7, B1–B10"),
            ("Type", "Deluxe"),
            ("Size", "28 m²"),
            ("Floor", "1st–2nd"),
            ("View", "Sea"),
            ("Available", "10 of 10"),
        ],
        "capacity": [
            ("Adults", "Up to 2"),
            ("Children", "Up to 1"),
            ("King bed", "1"),
            ("Sofa bed", "0"),
            ("Kitchen", "8 of 10 rooms"),
            ("Cot", "On request"),
        ],
        "amenities": [
            ("wifi", "Wi-Fi"), ("snowflake", "Air-con"), ("bath", "Marble bath"),
            ("eye", "Sea view"), ("flower", "Balcony"), ("coffee", "Nespresso"),
            ("device-tv", "Smart TV"), ("lock", "Safe"), ("glass", "Minibar"),
            ("tools-kitchen-2", "Kitchenette"), ("hanger", "Wardrobe"),
            ("wind", "Hair dryer"),
        ],
    },
    "family": {
        "name": "Family Suite",
        "rooms_label": "A8, A9, B8, B9 · 4 rooms",
        "sub": "Connecting layout · sleeps 4",
        "prices": _prices("room_family"),
        "photos": [
            ("assets/img/family/family-01.webp", "Family bedroom"),
            ("assets/img/standard/standard-06.webp", "Marble bath"),
            ("assets/img/standard/standard-09.webp", "Connecting room"),
            ("assets/img/standard/standard-12.webp", "Garden view"),
            ("assets/img/garden/garden-03.webp", "Garden walk"),
            ("assets/img/standard/standard-14.webp", "Entrance"),
        ],
        "basics": [
            ("Rooms", "A8, A9, B8, B9"),
            ("Type", "Family"),
            ("Size", "34 m²"),
            ("Floor", "1st"),
            ("View", "Garden"),
            ("Available", "4 of 4"),
        ],
        "capacity": [
            ("Adults", "Up to 2"),
            ("Children", "Up to 2"),
            ("King bed", "1"),
            ("Single beds", "2"),
            ("Sofa bed", "0"),
            ("Cot", "Available"),
        ],
        "amenities": [
            ("wifi", "Wi-Fi"), ("snowflake", "Air-con"), ("bath", "Marble bath"),
            ("flower", "Garden"), ("coffee", "Nespresso"), ("device-tv", "Smart TV"),
            ("lock", "Safe"), ("glass", "Minibar"), ("baby-carriage", "Cot ready"),
            ("hanger", "Wardrobe"), ("wind", "Hair dryer"),
        ],
    },
    "king": {
        "name": "King Suite — A6",
        "rooms_label": "A6 · 1 of 1",
        "sub": "Sea view · the signature suite · sleeps 2",
        "prices": _prices("room_king"),
        "photos": [
            ("assets/img/king/king-01.webp", "Bedroom"),
            ("assets/img/king/king-04.webp", "Marble bath"),
            ("assets/img/king/king-05.webp", "Sitting area"),
            ("assets/img/king/king-09.webp", "Terrace"),
            ("assets/img/king/king-11.webp", "Sea view"),
            ("assets/img/king/king-14.webp", "Entrance"),
        ],
        "basics": [
            ("Room", "A6"),
            ("Type", "King"),
            ("Size", "42 m²"),
            ("Floor", "2nd"),
            ("View", "Sea view"),
            ("Available", "1 of 1"),
        ],
        "capacity": [
            ("Adults", "Up to 2"),
            ("Children", "Up to 1"),
            ("King bed", "1"),
            ("Sofa bed", "0"),
            ("Cot", "On request"),
            ("Extra bed", "On request"),
        ],
        "amenities": [
            ("wifi", "Wi-Fi"), ("snowflake", "Air-con"), ("bath", "Marble bath"),
            ("eye", "Sea view"), ("flower", "Terrace"), ("coffee", "Nespresso"),
            ("device-tv", "Smart TV"), ("lock", "Safe"), ("glass", "Minibar"),
            ("hanger", "Wardrobe"), ("wind", "Hair dryer"), ("iron", "Iron"),
        ],
    },
}

# Order in which suite tabs appear left-to-right.
SUITE_ORDER = ["standard", "deluxe", "family", "king"]

# --- Spa packages (the "Spa" add-on expands to these) ----------------------
SPA_PACKAGES = [
    {
        "key": "classic",
        "name": "Classic Package",
        "prices": {"try": 1120, "eur": 32, "usd": 35},
        "bullets": [
            "20 min Turkish scrub & foam",
            "40 min classic massage",
            "Sauna and steam room access",
            "Face mask after each massage",
            "Herbal tea or coffee service",
            "Free shuttle service — round trip",
        ],
    },
    {
        "key": "relax",
        "name": "Relax Package",
        "prices": {"try": 1505, "eur": 43, "usd": 47},
        "bullets": [
            "20 min Turkish scrub & foam",
            "60 min mix therapy",
            "Sauna and steam room access",
            "Face mask after each massage",
            "Herbal tea or coffee service",
            "Free shuttle service — round trip",
        ],
    },
    {
        "key": "aroma",
        "name": "Aromatherapy Package",
        "prices": {"try": 2065, "eur": 59, "usd": 64},
        "bullets": [
            "20 min Turkish scrub & foam",
            "90 min aromatherapy",
            "Sauna and steam room access",
            "Face mask after each massage",
            "Freshly squeezed orange juice",
            "Free shuttle service — round trip",
        ],
    },
]

# --- Other add-ons ----------------------------------------------------------
AIRPORTS = [
    {"key": "ayt", "label": "Antalya (AYT)", "prices": {"try": 2800, "eur": 80, "usd": 87}},
    {"key": "gzp", "label": "Gazipaşa (GZP)", "prices": {"try": 4200, "eur": 120, "usd": 130}},
]

OTOGARS = [
    {"key": "antalya", "label": "Antalya Otogar", "prices": {"try": 1800, "eur": 52, "usd": 56}},
    {"key": "manavgat", "label": "Manavgat Otogar", "prices": {"try": 800, "eur": 23, "usd": 25}},
    {"key": "alanya", "label": "Alanya Otogar", "prices": {"try": 1500, "eur": 43, "usd": 47}},
]

# Major Turkish intercity bus operators — admin can extend in R010.
BUS_OPERATORS = [
    "Kamil Koç", "Metro Turizm", "Pamukkale Turizm", "Varan Turizm",
    "Truva Turizm", "Lüks Karadeniz", "Nilüfer Turizm", "Önder Turizm",
    "Star Turizm", "Lider Turizm", "Süha Turizm", "Has Turizm",
    "Aspendos Turizm", "Akdeniz Turizm", "Boss Turizm", "Reysaş Turizm",
    "Hareket Turizm", "Mersin Seyahat", "Beydağı Turizm", "Erciyes Turizm",
    "İğdır Doğu Kars", "Aksaray Cesur", "Doğu Tur", "Best Van Turizm",
    "Şanlıurfa Jet",
]

# Common airlines flying into AYT/GZP — flight prefix (IATA) → airline name.
# Used by JS to auto-fill the airline field as the guest types a flight number.
AIRLINE_LOOKUP = {
    "TK": "Turkish Airlines", "TC": "Turkish Airlines",
    "PC": "Pegasus Airlines",
    "XQ": "SunExpress", "XG": "SunExpress",
    "EW": "Eurowings", "EWG": "Eurowings",
    "LH": "Lufthansa", "DLH": "Lufthansa",
    "BA": "British Airways", "BAW": "British Airways",
    "KL": "KLM", "KLM": "KLM",
    "AF": "Air France", "AFR": "Air France",
    "LX": "Swiss", "SWR": "Swiss",
    "OS": "Austrian Airlines",
    "AY": "Finnair",
    "SK": "SAS",
    "LO": "LOT Polish Airlines",
    "AZ": "ITA Airways",
    "AA": "American Airlines",
    "DL": "Delta Air Lines",
    "W6": "Wizz Air",
    "FR": "Ryanair",
    "U2": "easyJet",
    "DY": "Norwegian",
    "IB": "Iberia",
    "SU": "Aeroflot",
    "S7": "S7 Airlines",
    "FZ": "flydubai",
    "EK": "Emirates",
    "QR": "Qatar Airways",
    "ET": "Ethiopian",
    "MS": "EgyptAir",
    "SV": "Saudia",
    "EY": "Etihad",
}

# Currency symbol prefixes for display.
CUR_SYM = {"try": "₺", "eur": "€", "usd": "$"}

# Late checkout policy
LATE_CHECKOUT = {
    "prices": {"try": 1000, "eur": 28, "usd": 30},
    "available_blurb": "Fixed late-checkout fee up to 17:00. Anything beyond 17:00, a full additional night is charged.",
    "unavailable_blurb": "Unfortunately late checkout is unavailable — the suite is reserved for arrival in the early afternoon. Luggage storage at reception is available.",
    "slots": ["13:00", "14:00", "15:00", "16:00", "17:00"],
    "checkout_default": "12:00",
    "checkin_default": "14:00",
}

WINE = {"prices": {"try": 1575, "eur": 45, "usd": 49}}


# --- Render helpers --------------------------------------------------------

def _fmt_price(prices: dict, cur: str = "eur") -> str:
    """Format a price dict for initial render in EUR (JS swaps on currency change)."""
    return f"{CUR_SYM[cur]}{prices[cur]:,}"


def _info_card(title: str, rows) -> str:
    """A clean info card — label-left, value-right, matching the v6 mockup."""
    inner = "".join(
        f'<div class="bk-row"><span class="k">{k}</span><span class="v">{v}</span></div>'
        for k, v in rows
    )
    return f'<div class="bk-card"><h3>{title}</h3>{inner}</div>'


def _amen_card(amenities) -> str:
    chips = "".join(
        f'<span class="bk-chip"><i class="ti ti-{icon}" aria-hidden="true"></i>{label}</span>'
        for icon, label in amenities
    )
    return f'<div class="bk-card bk-card-full"><h3>Features &amp; Amenities</h3><div class="bk-chips">{chips}</div></div>'


def _photo_tiles(photos, root: str) -> str:
    tiles = "".join(
        f'<button type="button" class="bk-tile" data-photo="{root}{path}" data-label="{label}" aria-label="{label}">'
        f'<span class="bk-tile-img" style="background-image:url(\'{root}{path}\')"></span>'
        f'<span class="bk-tile-tag">{label}</span></button>'
        for path, label in photos
    )
    return f'<div class="bk-tiles">{tiles}</div>'


def _suite_tab(key: str, selected: bool) -> str:
    s = SUITES[key]
    sel = ' data-sel="true"' if selected else ""
    short = s["name"].replace(" Suite", "").replace(" — A6", "")
    sub_left = s["sub"].split(" · ")[0]
    return (
        f'<button type="button" class="bk-tab" data-suite="{key}"{sel}>'
        f'  <span class="bk-tab-nm">{short}</span>'
        f'  <span class="bk-tab-pr" data-prices=\'{json.dumps(s["prices"])}\'>{sub_left} · from {_fmt_price(s["prices"])}</span>'
        f'</button>'
    )


# --- Add-on render helpers -------------------------------------------------

def _addon_airport(root: str) -> str:
    options = "".join(
        f'<label class="bk-radio-opt" data-airport="{a["key"]}">'
        f'<span class="bk-dot"></span>'
        f'<span class="bk-radio-lbl">{a["label"]}</span>'
        f'<span class="bk-radio-px" data-prices=\'{json.dumps(a["prices"])}\'>+{_fmt_price(a["prices"])}</span>'
        f'</label>'
        for a in AIRPORTS
    )
    return f"""
    <div class="bk-x" data-addon="airport">
      <label class="bk-x-hd">
        <input type="checkbox" class="bk-x-chk" />
        <span class="bk-x-ttl">Airport transfer</span>
        <span class="bk-x-px" data-prices='{json.dumps(AIRPORTS[0]["prices"])}'><span class="bk-x-from">from</span> +{_fmt_price(AIRPORTS[0]["prices"])}</span>
        <i class="ti ti-chevron-down bk-x-caret" aria-hidden="true"></i>
      </label>
      <div class="bk-x-body">
        <span class="bk-sublbl">Which airport</span>
        <div class="bk-radio-grp" data-required="airport">
          {options}
        </div>
        <div class="bk-mini-grid">
          <div class="bk-mini-fld"><label>Arrival date</label><input type="date" /></div>
          <div class="bk-mini-fld"><label>Arrival time</label><input type="time" /></div>
          <div class="bk-mini-fld bk-full"><label>Flight number <span class="bk-hint">e.g. TK1944</span></label><input type="text" class="bk-flight-input" placeholder="TK1944" autocomplete="off" /></div>
          <div class="bk-mini-fld bk-full"><label>Airline <span class="bk-hint">auto-filled from flight number</span></label><input type="text" class="bk-airline-out" disabled placeholder="(auto)" /></div>
        </div>
      </div>
    </div>
    """


def _addon_otogar(root: str) -> str:
    options = "".join(
        f'<label class="bk-radio-opt" data-otogar="{o["key"]}">'
        f'<span class="bk-dot"></span>'
        f'<span class="bk-radio-lbl">{o["label"]}</span>'
        f'<span class="bk-radio-px" data-prices=\'{json.dumps(o["prices"])}\'>+{_fmt_price(o["prices"])}</span>'
        f'</label>'
        for o in OTOGARS
    )
    bus_options = "".join(f'<option value="{b}">{b}</option>' for b in BUS_OPERATORS)
    return f"""
    <div class="bk-x" data-addon="otogar">
      <label class="bk-x-hd">
        <input type="checkbox" class="bk-x-chk" />
        <span class="bk-x-ttl">Otogar (bus) transfer</span>
        <span class="bk-x-px" data-prices='{json.dumps(OTOGARS[1]["prices"])}'><span class="bk-x-from">from</span> +{_fmt_price(OTOGARS[1]["prices"])}</span>
        <i class="ti ti-chevron-down bk-x-caret" aria-hidden="true"></i>
      </label>
      <div class="bk-x-body">
        <span class="bk-sublbl">Which Otogar (bus station)</span>
        <div class="bk-radio-grp bk-radio-stacked" data-required="otogar">
          {options}
        </div>
        <div class="bk-mini-grid">
          <div class="bk-mini-fld bk-full">
            <label>Bus line / company</label>
            <input type="text" list="bus-operators" placeholder="Start typing — Kamil Koç, Metro…" autocomplete="off" />
            <datalist id="bus-operators">{bus_options}<option value="Other / not listed">Other / not listed</option></datalist>
          </div>
          <div class="bk-mini-fld"><label>Arrival date</label><input type="date" /></div>
          <div class="bk-mini-fld"><label>Arrival time</label><input type="time" /></div>
        </div>
      </div>
    </div>
    """


def _addon_late_checkout() -> str:
    slot_options = "".join(f'<option value="{s}">{s}</option>' for s in LATE_CHECKOUT["slots"])
    px = LATE_CHECKOUT["prices"]
    co_default = LATE_CHECKOUT["checkout_default"]
    return f"""
    <div class="bk-x" data-addon="late-checkout" data-available="true" data-prices='{json.dumps(px)}'>
      <label class="bk-x-hd">
        <input type="checkbox" class="bk-x-chk" />
        <span class="bk-x-ttl">Late checkout</span>
        <span class="bk-x-px" data-prices='{json.dumps(px)}'>+{_fmt_price(px)} flat</span>
        <i class="ti ti-chevron-down bk-x-caret" aria-hidden="true"></i>
      </label>
      <div class="bk-x-body">
        <p class="bk-blurb">{LATE_CHECKOUT['available_blurb']} Standard checkout is {co_default}.</p>
        <div class="bk-mini-grid">
          <div class="bk-mini-fld bk-full">
            <label>Stay until</label>
            <select>{slot_options}</select>
          </div>
        </div>
      </div>
      <div class="bk-x-unavail">
        <p class="bk-blurb-unavail">{LATE_CHECKOUT['unavailable_blurb']}</p>
      </div>
    </div>
    """


def _addon_spa() -> str:
    packages_html = "".join(
        f'<label class="bk-spa-opt" data-spa="{p["key"]}" data-prices=\'{json.dumps(p["prices"])}\'>'
        f'<span class="bk-spa-head">'
        f'<span class="bk-dot"></span>'
        f'<span class="bk-spa-px">+{_fmt_price(p["prices"])}</span>'
        f'<span class="bk-spa-name">{p["name"]}</span>'
        f'</span>'
        f'<ul class="bk-spa-bullets">' + "".join(f'<li>{b}</li>' for b in p["bullets"]) + '</ul>'
        f'</label>'
        for p in SPA_PACKAGES
    )
    return f"""
    <div class="bk-x" data-addon="spa">
      <label class="bk-x-hd">
        <input type="checkbox" class="bk-x-chk" />
        <span class="bk-x-ttl">Spa</span>
        <span class="bk-x-px" data-prices='{json.dumps(SPA_PACKAGES[0]["prices"])}'><span class="bk-x-from">from</span> +{_fmt_price(SPA_PACKAGES[0]["prices"])}</span>
        <i class="ti ti-chevron-down bk-x-caret" aria-hidden="true"></i>
      </label>
      <div class="bk-x-body">
        <span class="bk-sublbl">Choose a package</span>
        <div class="bk-spa-grp" data-required="spa">
          {packages_html}
        </div>
      </div>
    </div>
    """


def _addon_wine() -> str:
    return f"""
    <div class="bk-x" data-addon="wine" data-prices='{json.dumps(WINE["prices"])}'>
      <label class="bk-x-hd">
        <input type="checkbox" class="bk-x-chk" />
        <span class="bk-x-ttl">Sparkling wine on arrival</span>
        <span class="bk-x-px" data-prices='{json.dumps(WINE["prices"])}'>+{_fmt_price(WINE["prices"])}</span>
      </label>
    </div>
    """


# --- Main page render ------------------------------------------------------

def _data_json(root: str) -> str:
    """Emit all the data the front-end JS needs as a single window.BOOK_DATA blob.
    On currency change, the JS reads from this to re-render every price on the page.
    In R010 this will be fetched from the admin backend instead."""
    blob = {
        "currency_symbols": CUR_SYM,
        "suites": {
            k: {
                "name": v["name"],
                "rooms_label": v["rooms_label"],
                "sub": v["sub"],
                "prices": v["prices"],
                "photos": [{"path": f"{root}{p}", "label": l} for p, l in v["photos"]],
                "basics": v["basics"],
                "capacity": v["capacity"],
                "amenities": v["amenities"],
            }
            for k, v in SUITES.items()
        },
        "airports": AIRPORTS,
        "otogars": OTOGARS,
        "spa_packages": SPA_PACKAGES,
        "wine": WINE,
        "late_checkout": LATE_CHECKOUT,
        "airline_lookup": AIRLINE_LOOKUP,
    }
    return json.dumps(blob, ensure_ascii=False)


def book(root: str) -> str:
    initial = "king"
    s = SUITES[initial]

    # Suite tabs
    tabs_html = "".join(_suite_tab(k, k == initial) for k in SUITE_ORDER)

    # Initial info cards (King is selected by default)
    basics_html = _info_card("Basic Details", s["basics"])
    capacity_html = _info_card("Capacity &amp; Beds", s["capacity"])
    amenities_html = _amen_card(s["amenities"])

    # Initial hero + tiles
    first_photo = s["photos"][0]
    hero_url = f"{root}{first_photo[0]}"
    hero_label = first_photo[1]
    tiles_html = _photo_tiles(s["photos"], root)

    # Add-ons
    addons_html = "\n".join([
        _addon_airport(root),
        _addon_otogar(root),
        _addon_late_checkout(),
        _addon_spa(),
        _addon_wine(),
    ])

    data_blob = _data_json(root)

    return f"""
    <div class="bk-page">

      <!-- Title bar -->
      <div class="bk-title">
        <h1>Send an enquiry</h1>
        <p class="bk-title-note">No payment, no commitment · rates shown are indicative — we confirm the final rate for your dates within the hour, usually faster</p>
      </div>

      <!-- Suite tabs (full width) -->
      <div class="bk-tabs" id="bk-tabs" role="tablist" aria-label="Suite type">
        {tabs_html}
      </div>

      <!-- Two-column layout -->
      <div class="bk-cols">

        <!-- LEFT: form -->
        <!-- R016: form posts intercepted by site.js submitEnquiry() handler.
             Action URL becomes real Cloudflare Worker once user confirms wiring;
             during stub phase the handler just shows the email preview panel. -->
        <form class="bk-form" id="bk-form" novalidate
              data-enquiry-kind="room"
              action="https://mira-palace-enquiry.apps-224.workers.dev"
              method="POST">

          <!-- R016: honeypot — hidden field bots fill in but humans don't.
               R023: label text made blank so it never appears in a screen
               scrape / SR read-out. Submit handler rejects the form silently
               if this field is non-empty. -->
          <div class="bk-honeypot" aria-hidden="true">
            <label aria-hidden="true"><input type="text" name="website" tabindex="-1" autocomplete="off" /></label>
          </div>

          <div class="bk-form-head">
            <div>
              <div class="bk-form-nm" id="bk-form-nm">{s['name']}</div>
              <div class="bk-form-sub" id="bk-form-sub">{s['rooms_label']}</div>
            </div>
            <div class="bk-form-pr">
              <span id="bk-form-price" data-prices='{json.dumps(s["prices"])}'>{_fmt_price(s["prices"])}</span>
              <small>/ night</small>
            </div>
          </div>

          <div class="bk-grp">Dates</div>
          <div class="bk-rw2">
            <div class="bk-fld"><label for="bk-arrival">Arrival</label><input type="date" id="bk-arrival" name="arrival" required /></div>
            <div class="bk-fld"><label for="bk-departure">Departure</label><input type="date" id="bk-departure" name="departure" required /></div>
          </div>

          <div class="bk-grp">Guests</div>
          <div class="bk-rw2">
            <div class="bk-fld">
              <label for="bk-adults">Adults</label>
              <select id="bk-adults" name="adults">
                <option value="1">1</option>
                <option value="2" selected>2</option>
                <option value="3">3</option>
                <option value="4">4</option>
              </select>
            </div>
            <div class="bk-fld">
              <label for="bk-children">Children</label>
              <select id="bk-children" name="children">
                <option value="0" selected>0</option>
                <option value="1">1</option>
                <option value="2">2</option>
              </select>
            </div>
          </div>

          <div class="bk-grp">Your stay</div>
          <div class="bk-rw2">
            <div class="bk-fld">
              <label for="bk-arrival-time">Estimated arrival</label>
              <select id="bk-arrival-time" name="arrival_time">
                <option value="">Not sure yet</option>
                <option value="morning">Morning (before 12:00)</option>
                <option value="afternoon">Afternoon (12:00–18:00)</option>
                <option value="evening">Evening (18:00–22:00)</option>
                <option value="late">Late (after 22:00)</option>
              </select>
            </div>
            <div class="bk-fld">
              <label for="bk-occasion">Occasion (optional)</label>
              <select id="bk-occasion" name="occasion">
                <option value="">Just a stay</option>
                <option value="honeymoon">Honeymoon</option>
                <option value="anniversary">Anniversary</option>
                <option value="birthday">Birthday</option>
                <option value="wellness">Wellness retreat</option>
                <option value="family">Family holiday</option>
                <option value="business">Business trip</option>
              </select>
            </div>
          </div>

          <div class="bk-grp">Your details</div>
          <div class="bk-fld"><label for="bk-name">Full name</label><input type="text" id="bk-name" name="name" placeholder="Jane Roberts" required /></div>
          <div class="bk-fld"><label for="bk-email">Email</label><input type="email" id="bk-email" name="email" placeholder="jane@example.com" required /></div>
          <div class="bk-fld"><label for="bk-phone">Phone</label><input type="tel" id="bk-phone" name="phone" placeholder="+44 7700 900 123" /></div>
          <div class="bk-fld"><label for="bk-notes">Anything else? (optional)</label><input type="text" id="bk-notes" name="notes" placeholder="Dietary, accessibility, a specific request..." /></div>

          <div class="bk-grp">Add-ons</div>
          <div class="bk-xs" id="bk-xs">
            {addons_html}
          </div>

          <!-- R016: Cloudflare Turnstile bot-check. Test sitekey "always pass"
               during stub phase — swaps to real sitekey once user creates the
               Turnstile widget in Cloudflare. -->
          <div class="bk-turnstile-wrap">
            <div class="cf-turnstile" data-sitekey="1x00000000000000000000AA" data-callback="bkTurnstileOK" data-theme="light"></div>
          </div>

          <button type="submit" class="bk-go">Send enquiry →</button>
          <p class="bk-foot">This is an enquiry, not a confirmed booking. No payment now. We reply with availability and a direct rate within the hour — usually faster.</p>

        </form>

        <!-- R016: email preview panel — shows the exact staff inbox format.
             R023: now gated behind ?demo=1 query param via site.js, so the
             DEMO PREVIEW banner never surfaces in front of a real guest at
             production. Local previews still pop it up with ?demo=1. -->
        <div id="bk-email-preview" class="bk-hidden bk-email-preview" data-demo-only="true">
          <div class="bk-email-preview-head">
            <span class="bk-email-preview-tag">DEMO PREVIEW</span>
            <h3>What the hotel staff inbox will receive</h3>
            <p class="bk-email-preview-note">This is the formatted email that Resend will deliver to the hotel once the email wiring is connected. During the stub phase, the form does not actually send — it shows you this preview so you can verify the format.</p>
          </div>
          <pre id="bk-email-preview-body" class="bk-email-preview-body"></pre>
        </div>

        <!-- Confirmation panel (hidden until submit) -->
        <div id="bk-thanks" class="bk-hidden bk-thanks">
          <div class="bk-thanks-tick">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
          </div>
          <h3>Enquiry sent.</h3>
          <p>We'll be back to you within the hour with availability and a direct rate. Thank you for choosing to write to us directly.</p>
        </div>

        <!-- RIGHT: visuals -->
        <div class="bk-vis">
          <div class="bk-hero" id="bk-hero" style="background-image:url('{hero_url}');">
            <span class="bk-hero-tag" id="bk-hero-tag">{hero_label} · {s['name']}</span>
            <button type="button" class="bk-hero-full" aria-label="View fullscreen"><i class="ti ti-maximize" aria-hidden="true"></i><span>Fullscreen</span></button>
          </div>

          <div class="bk-info" id="bk-info">
            {basics_html}
            {capacity_html}
            {amenities_html}
          </div>

          <div class="bk-tiles-hd">
            <h3>More photos (<span id="bk-photo-count">{len(s['photos'])}</span>)</h3>
            <button type="button" class="bk-viewall" aria-label="View all"><i class="ti ti-maximize" aria-hidden="true"></i>View all</button>
          </div>
          <div id="bk-tiles-host">
            {tiles_html}
          </div>
        </div>

      </div>

    </div>

    <!-- Data blob the front-end JS reads from. R010 swaps this for a fetch() call to the admin API. -->
    <script type="application/json" id="bk-data">{data_blob}</script>
    """


PAGES = [
    {"path": "book.html", "active": "",
     "title": "Book a stay · Mira Palace",
     "description": "Direct-booking enquiry form for Mira Palace — confirm your dates, suite preference, and any specific requirements.",
     "body": book},
]
