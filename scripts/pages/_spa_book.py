"""Spa booking page — R007.

Mirrors the R006 room booking layout (form left, photos right) but adapted
for spa packages. Three package tabs (Classic / Relax / Aromatherapy);
form is simpler than room booking because:

- single date + time slot (not date range)
- party size 1 or 2 (couples version of any package available)
- no add-ons (everything is part of the package itself)
- no late-checkout / airport / otogar etc.

Uses the same .bk-* CSS classes as the room booking for layout consistency;
site.js has a dedicated branch for spa booking that handles tab swap +
currency switch + total recalculation.
"""
from __future__ import annotations
import json
from common import SITE_META

CUR_SYM = {"try": "₺", "eur": "€", "usd": "$"}

PACKAGES = [
    {
        "key": "classic",
        "name": "Classic Package",
        "tagline": "The signature introduction",
        "prices": {"try": 1120, "eur": 32, "usd": 35},
        "duration_min": 60,
        "bullets": [
            "20 min Turkish scrub & foam",
            "40 min classic massage",
            "Sauna and steam room access",
            "Face mask after each massage",
            "Herbal tea or coffee service",
            "Free shuttle service — round trip",
        ],
        "photos": [
            ("assets/img/spa/spa-01.jpg", "Hammam chamber"),
            ("assets/img/spa/spa-03.jpg", "Marble göbek taşı"),
            ("assets/img/spa/spa-06.jpg", "Treatment room"),
            ("assets/img/spa/spa-08.jpg", "Relaxation lounge"),
            ("assets/img/spa/spa-11.jpg", "Spa entrance"),
            ("assets/img/spa/spa-02.jpg", "Steam room"),
        ],
    },
    {
        "key": "relax",
        "name": "Relax Package",
        "tagline": "Longer, deeper, more therapeutic",
        "prices": {"try": 1505, "eur": 43, "usd": 47},
        "duration_min": 80,
        "bullets": [
            "20 min Turkish scrub & foam",
            "60 min mix therapy",
            "Sauna and steam room access",
            "Face mask after each massage",
            "Herbal tea or coffee service",
            "Free shuttle service — round trip",
        ],
        "photos": [
            ("assets/img/spa/spa-06.jpg", "Treatment room"),
            ("assets/img/spa/spa-08.jpg", "Relaxation lounge"),
            ("assets/img/spa/spa-03.jpg", "Marble göbek taşı"),
            ("assets/img/spa/spa-01.jpg", "Hammam chamber"),
            ("assets/img/spa/spa-11.jpg", "Spa entrance"),
            ("assets/img/spa/spa-04.jpg", "Massage suite"),
        ],
    },
    {
        "key": "aroma",
        "name": "Aromatherapy Package",
        "tagline": "Our most indulgent ritual",
        "prices": {"try": 2065, "eur": 59, "usd": 64},
        "duration_min": 110,
        "bullets": [
            "20 min Turkish scrub & foam",
            "90 min aromatherapy",
            "Sauna and steam room access",
            "Face mask after each massage",
            "Freshly squeezed orange juice",
            "Free shuttle service — round trip",
        ],
        "photos": [
            ("assets/img/spa/spa-08.jpg", "Relaxation lounge"),
            ("assets/img/spa/spa-06.jpg", "Treatment room"),
            ("assets/img/spa/spa-01.jpg", "Hammam chamber"),
            ("assets/img/spa/spa-03.jpg", "Marble göbek taşı"),
            ("assets/img/spa/spa-11.jpg", "Spa entrance"),
            ("assets/img/spa/spa-09.jpg", "Aromatherapy room"),
        ],
    },
]

PACKAGE_ORDER = ["classic", "relax", "aroma"]

# Spa facilities — same for every package (info card 3)
SPA_FACILITIES = [
    ("flame", "Turkish hammam"),
    ("temperature-sun", "Two saunas"),
    ("droplet", "Steam room"),
    ("snowflake", "Cold plunge"),
    ("yoga", "Relaxation lounge"),
    ("activity", "Fitness studio"),
    ("flower", "Herbal tea bar"),
    ("shirt", "Robe + slippers"),
]

# What to bring — info card 2 chips
BRING_ITEMS = [
    ("check", "Just yourself"),
    ("hanger", "Swimsuit (for sauna)"),
    ("user", "Towel provided"),
    ("droplet", "Slippers provided"),
]

# Time slots the spa accepts bookings for
TIME_SLOTS = ["10:00", "11:00", "12:00", "14:00", "15:00", "16:00", "17:00", "18:00"]


def _fmt(prices, cur="eur"):
    return f"{CUR_SYM[cur]}{prices[cur]:,}"


def _tab(p, selected: bool) -> str:
    sel = ' data-sel="true"' if selected else ""
    return (
        f'<button type="button" class="bk-tab" data-pkg="{p["key"]}"{sel}>'
        f'  <span class="bk-tab-nm">{p["name"].replace(" Package","")}</span>'
        f'  <span class="bk-tab-pr" data-prices=\'{json.dumps(p["prices"])}\'>{p["duration_min"]} min · from {_fmt(p["prices"])}</span>'
        f'</button>'
    )


def _bullets_card(bullets) -> str:
    items = "".join(f'<li>{b}</li>' for b in bullets)
    return (
        f'<div class="bk-card">'
        f'<h3>Included in this package</h3>'
        f'<ul class="bk-bullets-list">{items}</ul>'
        f'</div>'
    )


def _bring_card() -> str:
    chips = "".join(
        f'<span class="bk-chip"><i class="ti ti-{i}" aria-hidden="true"></i>{l}</span>'
        for i, l in BRING_ITEMS
    )
    return (
        f'<div class="bk-card">'
        f'<h3>What to bring</h3>'
        f'<div class="bk-chips">{chips}</div>'
        f'</div>'
    )


def _facilities_card() -> str:
    chips = "".join(
        f'<span class="bk-chip"><i class="ti ti-{i}" aria-hidden="true"></i>{l}</span>'
        for i, l in SPA_FACILITIES
    )
    return (
        f'<div class="bk-card bk-card-full">'
        f'<h3>Spa facilities (all packages)</h3>'
        f'<div class="bk-chips">{chips}</div>'
        f'</div>'
    )


def _photo_tiles(photos, root: str) -> str:
    tiles = "".join(
        f'<button type="button" class="bk-tile" data-photo="{root}{p}" data-label="{l}" aria-label="{l}">'
        f'<span class="bk-tile-img" style="background-image:url(\'{root}{p}\')"></span>'
        f'<span class="bk-tile-tag">{l}</span></button>'
        for p, l in photos
    )
    return f'<div class="bk-tiles">{tiles}</div>'


def _data_json(root: str) -> str:
    blob = {
        "kind": "spa",
        "currency_symbols": CUR_SYM,
        "packages": {
            p["key"]: {
                "name": p["name"],
                "tagline": p["tagline"],
                "duration_min": p["duration_min"],
                "prices": p["prices"],
                "bullets": p["bullets"],
                "photos": [{"path": f"{root}{path}", "label": l} for path, l in p["photos"]],
            }
            for p in PACKAGES
        },
    }
    return json.dumps(blob, ensure_ascii=False)


def spa_book(root: str) -> str:
    initial = "classic"
    p = next(x for x in PACKAGES if x["key"] == initial)

    tabs_html = "".join(_tab(x, x["key"] == initial) for x in PACKAGES)
    first_photo = p["photos"][0]
    hero_url = f"{root}{first_photo[0]}"
    hero_label = first_photo[1]
    tiles_html = _photo_tiles(p["photos"], root)
    bullets_html = _bullets_card(p["bullets"])
    bring_html = _bring_card()
    facilities_html = _facilities_card()
    slot_options = "".join(f'<option value="{s}">{s}</option>' for s in TIME_SLOTS)

    data_blob = _data_json(root)

    return f"""
    <div class="bk-page sp-page">

      <div class="bk-title">
        <h1>Book a spa session</h1>
        <p class="bk-title-note">Open daily 10:00–19:00 · free shuttle from the hotel · packages designed for solo or couples</p>
      </div>

      <div class="bk-tabs" id="sp-tabs" role="tablist" aria-label="Spa package">
        {tabs_html}
      </div>

      <div class="bk-cols">

        <form class="bk-form" id="sp-form" novalidate
              onsubmit="event.preventDefault(); document.getElementById('sp-thanks').classList.remove('bk-hidden'); this.style.display='none';">

          <div class="bk-form-head">
            <div>
              <div class="bk-form-nm" id="sp-form-nm">{p['name']}</div>
              <div class="bk-form-sub" id="sp-form-sub">{p['duration_min']} min · {p['tagline'].lower()}</div>
            </div>
            <div class="bk-form-pr">
              <span id="sp-form-price" data-prices='{json.dumps(p["prices"])}'>{_fmt(p["prices"])}</span>
              <small>per person</small>
            </div>
          </div>

          <div class="bk-grp">When</div>
          <div class="bk-rw2">
            <div class="bk-fld"><label for="sp-date">Date</label><input type="date" id="sp-date" name="date" required /></div>
            <div class="bk-fld"><label for="sp-time">Time slot</label><select id="sp-time" name="time" required>{slot_options}</select></div>
          </div>

          <div class="bk-grp">Who</div>
          <div class="bk-rw2">
            <div class="bk-fld">
              <label for="sp-people">People</label>
              <select id="sp-people" name="people">
                <option value="1" selected>1 person</option>
                <option value="2">2 people (couples)</option>
              </select>
            </div>
            <div class="bk-fld">
              <label for="sp-guest">Hotel guest?</label>
              <select id="sp-guest" name="guest">
                <option value="yes" selected>Staying at Mira Palace</option>
                <option value="no">Visiting from elsewhere</option>
              </select>
            </div>
          </div>

          <div class="bk-grp">Your details</div>
          <div class="bk-fld"><label for="sp-name">Full name</label><input type="text" id="sp-name" name="name" placeholder="Jane Roberts" required /></div>
          <div class="bk-fld"><label for="sp-email">Email</label><input type="email" id="sp-email" name="email" placeholder="jane@example.com" required /></div>
          <div class="bk-fld"><label for="sp-phone">Phone</label><input type="tel" id="sp-phone" name="phone" placeholder="+44 7700 900 123" /></div>
          <div class="bk-fld"><label for="sp-room">Room number <span class="bk-hint">(if a hotel guest)</span></label><input type="text" id="sp-room" name="room" placeholder="A6 / B7 / C12..." /></div>
          <div class="bk-fld"><label for="sp-notes">Notes (optional)</label><input type="text" id="sp-notes" name="notes" placeholder="Pregnancy, injuries, allergies, preferred therapist gender..." /></div>

          <div class="bk-tot">
            <div class="bk-tot-rows">
              <span class="bk-tot-lbl">Estimated total</span>
              <span class="bk-tot-num" id="sp-total" data-prices='{json.dumps(p["prices"])}'>{_fmt(p["prices"])}</span>
            </div>
            <span class="bk-tot-sub" id="sp-tot-sub">{p['name']} · 1 person · {p['duration_min']} min</span>
          </div>

          <button type="submit" class="bk-go">Request session →</button>
          <p class="bk-foot">We confirm within the hour during spa hours · free shuttle from the hotel · all prices admin-managed</p>

        </form>

        <div id="sp-thanks" class="bk-hidden bk-thanks">
          <div class="bk-thanks-tick">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
          </div>
          <h3>Request sent.</h3>
          <p>We'll be back to you within the hour with availability confirmed for your chosen slot. Thank you for booking direct.</p>
        </div>

        <div class="bk-vis">
          <div class="bk-hero" id="sp-hero" style="background-image:url('{hero_url}');">
            <span class="bk-hero-tag" id="sp-hero-tag">{hero_label} · {p['name']}</span>
            <button type="button" class="bk-hero-full" aria-label="View fullscreen"><i class="ti ti-maximize" aria-hidden="true"></i><span>Fullscreen</span></button>
          </div>

          <div class="bk-info" id="sp-info">
            {bullets_html}
            {bring_html}
            {facilities_html}
          </div>

          <div class="bk-tiles-hd">
            <h3>Spa photos (<span id="sp-photo-count">{len(p['photos'])}</span>)</h3>
            <button type="button" class="bk-viewall" aria-label="View all"><i class="ti ti-maximize" aria-hidden="true"></i>View all</button>
          </div>
          <div id="sp-tiles-host">
            {tiles_html}
          </div>
        </div>

      </div>

    </div>

    <script type="application/json" id="sp-data">{data_blob}</script>
    """


PAGES = [
    {"path": "spa-book.html", "active": "spa",
     "title": "Book a spa session · Mira Palace",
     "description": "Book a spa session at Mira Palace — Classic, Relax or Aromatherapy package. Hammam, sauna, steam room and treatment included. Open to hotel guests and visitors.",
     "body": spa_book},
]
