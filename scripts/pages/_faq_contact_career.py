from common import hero, section, eyebrow, heading, SITE_META

IMG_CONTACT = "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1920&q=80"
IMG_FAQ = "https://images.unsplash.com/photo-1590073242678-70ee3fc28e8e?auto=format&fit=crop&w=1920&q=80"
IMG_CAREER = "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?auto=format&fit=crop&w=1920&q=80"


def faq(root: str) -> str:
    qs = [
        ("What time is check-in and check-out?",
         "Check-in from 15:00 and check-out by 12:00. Early check-in and late check-out are offered subject to availability — ask on arrival, or arrange in advance via the enquiry form."),
        ("Is breakfast / All-Inclusive included in my room rate?",
         "Yes. Every rate at Mira Palace is All-Inclusive and covers breakfast, lunch, dinner, afternoon tea, a late-night snack bar, and all soft drinks, local beers, wines, spirits and coffees. See the All-Inclusive page for the honest extras list."),
        ("What airport do you recommend?",
         "Antalya International (AYT), 60 km from the hotel. We can arrange a private or shared transfer — see the Location page for options and prices."),
        ("Is the hotel suitable for children?",
         "Yes — we have a dedicated Family Connecting room type, a children’s pool with a small slide, a kids’ club (4–12) and a teen lounge (13–17). Children under 6 stay free when sharing with two adults; 6–12 at a reduced rate."),
        ("Do you allow pets?",
         "Service dogs are welcome; other pets are not, in line with Turkish food-safety rules for the restaurant and pool areas."),
        ("Is smoking allowed?",
         "Rooms and indoor public spaces are non-smoking. Smoking is permitted on balconies and in designated outdoor areas away from dining."),
        ("What is your cancellation policy?",
         "Flexible: free cancellation up to 14 days before arrival. Within 14 days, the first night is charged. Non-refundable rates are discounted by 10 per cent and are — as the name implies — not refundable. Seasonal and package rates may vary."),
        ("Do you have facilities for guests with reduced mobility?",
         "Yes. The ground floor is step-free, one of our Deluxe rooms is fully accessible with a roll-in shower, and the spa, restaurants and pools are reachable without stairs. Please let us know at booking so we can allocate the right room."),
        ("Can I arrange a wedding, proposal or honeymoon?",
         "Yes to all three. The honeymoon package covers couples within six months of their wedding — write to info@sidemirapalace.com with your dates."),
        ("Do you have a spa and what does it cost?",
         "Yes. The hammam, saunas, steam room, cold plunge and relaxation room are included in your stay. Treatments — massage, facial, rituals — are priced à la carte on the treatment menu."),
        ("Is the electricity Turkish standard?",
         "Yes, 230 V, type F (European two-pin). Our rooms also have USB-C sockets on the bedside and desk."),
        ("Is there Wi-Fi? Is it fast?",
         "Yes, complimentary fibre (approximately 500 Mbps) throughout the hotel. Good enough for video calls and streaming. If yours misbehaves, the front desk will move you to a closer access point."),
    ]
    items = "".join(
        f'<details class="group border-b border-mira-200 py-5"><summary class="flex items-center justify-between cursor-pointer list-none"><span class="font-display text-xl text-mira-900">{q}</span><span class="text-sand-500 transition group-open:rotate-45 text-2xl leading-none">+</span></summary><p class="mt-4 text-mira-700 leading-relaxed">{a}</p></details>'
        for q, a in qs
    )
    h = hero(IMG_FAQ, "FAQ", "Before you ask.",
             "Twelve of the questions we hear most often, answered. Don’t see yours? Drop us a line on info@sidemirapalace.com and we will reply the same day, usually within an hour.", height="55vh")
    body = section(f"""
      <div class="max-w-3xl">{items}</div>
    """, bg="bg-white")
    return h + body


def contact(root: str) -> str:
    m = SITE_META
    h = hero(IMG_CONTACT, "Contact & enquiries", "We’ll reply within the hour.",
             "WhatsApp is the fastest way to reach us; email if you’d prefer the detail on paper. Phones are answered 24/7 — we are a small team and one of us is always on.", height="58vh")
    body = section(f"""
      <div class="grid lg:grid-cols-12 gap-12">
        <div class="lg:col-span-5">{eyebrow('Reach us')}
          {heading('Four ways to write.', 3)}
          <ul class="mt-6 space-y-4 text-mira-800">
            <li><div class="text-xs uppercase tracking-widest text-mira-500">Phone</div><a href="tel:{m['phone_tel']}" class="font-display text-2xl hover:text-sand-600">{m['phone_display']}</a></li>
            <li><div class="text-xs uppercase tracking-widest text-mira-500">Email</div><a href="mailto:{m['email']}" class="font-display text-2xl hover:text-sand-600">{m['email']}</a></li>
            <li><div class="text-xs uppercase tracking-widest text-mira-500">WhatsApp</div><a href="{m['whatsapp']}" class="font-display text-2xl hover:text-sand-600">+90 534 898 84 05</a></li>
            <li><div class="text-xs uppercase tracking-widest text-mira-500">Address</div><address class="not-italic">{m['address_line1']}<br/>{m['address_line2']}</address></li>
          </ul>
          <div class="mt-6">
            <div class="text-xs uppercase tracking-widest text-mira-500 mb-2">Find us on the map</div>
            <iframe src="https://www.google.com/maps?q=36.7748,31.3888&amp;hl=en&amp;z=14&amp;output=embed" class="w-full aspect-[4/3] rounded-lg shadow-lux border-0" loading="lazy" title="Map of Mira Palace"></iframe>
            <a href="{m['google_maps']}" rel="noopener" class="mt-3 inline-flex items-center gap-2 text-sm text-mira-700 hover:text-sand-600 font-medium">Open in Google Maps for directions <span>→</span></a>
          </div>
        </div>
        <div class="lg:col-span-7">
          <form id="enquiry" action="mailto:{m['email']}" method="post" enctype="text/plain" class="bg-white rounded-lg shadow-lux p-7 space-y-5">
            <h3 class="font-display text-2xl text-mira-900">Send an enquiry</h3>

            <label class="block">
              <span class="text-sm font-medium text-mira-800">Reason for getting in touch</span>
              <select id="enq-reason" name="reason" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2.5 text-sm focus:border-mira-500 focus:ring-0">
                <option value="reservation">Room reservation enquiry</option>
                <option value="group">Group booking (10+ rooms)</option>
                <option value="wedding">Wedding or private event</option>
                <option value="career">Career / job opportunity</option>
                <option value="press">Press, partnership or media</option>
                <option value="lost">Lost &amp; found / past stay</option>
                <option value="other">Something else</option>
              </select>
            </label>

            <div class="grid sm:grid-cols-2 gap-5">
              <label class="block"><span class="text-sm text-mira-700">Your name</span><input required name="name" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2 text-sm focus:border-mira-500 focus:ring-0" /></label>
              <label class="block"><span class="text-sm text-mira-700">Email</span><input required type="email" name="email" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2 text-sm focus:border-mira-500 focus:ring-0" /></label>
            </div>

            <div id="enq-reservation-fields" class="grid sm:grid-cols-2 gap-5">
              <label class="block"><span class="text-sm text-mira-700">Arrival date</span><input type="date" name="arrival" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2 text-sm" /></label>
              <label class="block"><span class="text-sm text-mira-700">Departure date</span><input type="date" name="departure" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2 text-sm" /></label>
              <label class="block"><span class="text-sm text-mira-700">Adults</span><input type="number" min="1" value="2" name="adults" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2 text-sm" /></label>
              <label class="block"><span class="text-sm text-mira-700">Children</span><input type="number" min="0" value="0" name="children" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2 text-sm" /></label>
              <label class="block sm:col-span-2"><span class="text-sm text-mira-700">Room preference</span>
                <select name="room" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2 text-sm">
                  <option>Not sure — recommend for my dates</option>
                  <option>Standard Room</option>
                  <option>Deluxe Room</option>
                  <option>Family Connecting</option>
                  <option>Junior Suite</option>
                </select>
              </label>
            </div>

            <script>
              (function() {{
                const sel = document.getElementById('enq-reason');
                const fields = document.getElementById('enq-reservation-fields');
                if (!sel || !fields) return;
                const sync = () => {{ fields.style.display = (sel.value === 'reservation') ? '' : 'none'; }};
                sel.addEventListener('change', sync); sync();
              }})();
            </script>

            <div class="grid sm:grid-cols-2 gap-5">
              <label class="block sm:col-span-2"><span class="text-sm text-mira-700">Message</span><textarea name="message" rows="4" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2 text-sm focus:border-mira-500 focus:ring-0" placeholder="Anniversaries, dietary needs, accessibility, anything else worth us knowing."></textarea></label>
            </div>
            <label class="flex items-start gap-3 text-xs text-mira-700"><input type="checkbox" required class="mt-1" /><span>I consent to Mira Palace using my details to reply to this enquiry, in line with the <a href="{root}legal/privacy.html" class="underline">Privacy Notice</a>. (This is the required consent — it is kept separate from marketing, per data-protection rules.)</span></label>
            <label class="flex items-start gap-3 text-xs text-mira-700"><input type="checkbox" class="mt-1" /><span>Also sign me up for occasional seasonal offers and news from the hotel (optional, separate consent).</span></label>
            <button class="inline-flex items-center justify-center px-6 py-3 bg-mira-700 text-white rounded-full font-medium hover:bg-mira-800">Send enquiry</button>
            <p class="text-xs text-mira-500">This demonstration form opens your email client. In the production site, submissions go directly to the hotel’s reservations inbox.</p>
          </form>
        </div>
      </div>
    """, bg="bg-sand-50")
    return h + body


def career(root: str) -> str:
    roles = [
        ("Front-desk Receptionist", "Full-time · Year-round", "Excellent English; a second language (German, Russian, Arabic) a strong plus. Prior hospitality experience preferred."),
        ("Commis Chef", "Full-time · Year-round", "Training under our head chef. Willing to learn both Turkish and Mediterranean cuisines."),
        ("Spa Therapist", "Full-time · Seasonal", "Certified massage therapist. Knowledge of Turkish hammam techniques preferred."),
        ("Housekeeping Assistant", "Full-time · Seasonal", "Careful, thorough, reliable. Staff accommodation available for applicants from outside Manavgat."),
        ("Kids’ Club Leader", "Full-time · April–November", "Experience working with children 4–12. First-aid qualification required (we will support a recert if needed)."),
    ]
    rows = "".join(
        f'<div class="p-7 bg-white rounded-lg shadow-lux flex flex-col md:flex-row md:items-center md:justify-between gap-4"><div><h3 class="font-display text-2xl text-mira-900">{t}</h3><p class="text-sm text-mira-600">{sub}</p><p class="mt-2 text-sm text-mira-700">{d}</p></div><a href="#apply" class="shrink-0 inline-flex items-center px-5 py-2 bg-mira-700 text-white rounded-full text-sm font-medium hover:bg-mira-800">Apply</a></div>'
        for t, sub, d in roles
    )
    h = hero(IMG_CAREER, "Careers", "Come and work with us.",
             "A small team — thirty-four rooms asks about fifty staff — which means every job matters and every person is visible. We pay on time, we train, and most of our seasonal staff come back the following year.",
             height="60vh")
    listings = section(f"""
      {eyebrow('Open positions')}
      {heading('Who we’re hiring this season.', 3)}
      <div class="grid gap-5 mt-10">{rows}</div>
    """, bg="bg-sand-50")
    form = section(f"""
      <div id="apply" class="max-w-2xl mx-auto">{eyebrow('Apply')}
        {heading('Application form.', 3)}
        <form class="mt-8 bg-white rounded-lg shadow-lux p-7 space-y-5" onsubmit="event.preventDefault(); alert('Demo form — in the production site, this submits to HR.');">
          <div class="grid sm:grid-cols-2 gap-5">
            <label class="block"><span class="text-sm text-mira-700">Full name</span><input required class="mt-1 block w-full rounded border border-mira-200 px-3 py-2 text-sm" /></label>
            <label class="block"><span class="text-sm text-mira-700">Email</span><input required type="email" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2 text-sm" /></label>
            <label class="block"><span class="text-sm text-mira-700">Phone</span><input type="tel" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2 text-sm" /></label>
            <label class="block"><span class="text-sm text-mira-700">Position applied for</span>
              <select class="mt-1 block w-full rounded border border-mira-200 px-3 py-2 text-sm">
                {"".join(f"<option>{t}</option>" for t, *_ in roles)}
              </select>
            </label>
            <label class="block sm:col-span-2"><span class="text-sm text-mira-700">CV (PDF, up to 5 MB)</span><input type="file" accept="application/pdf" class="mt-1 block w-full text-sm text-mira-700" /></label>
            <label class="block sm:col-span-2"><span class="text-sm text-mira-700">Cover note</span><textarea rows="4" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2 text-sm" placeholder="A short note about your experience and availability."></textarea></label>
          </div>
          <label class="flex items-start gap-3 text-xs text-mira-700"><input type="checkbox" required class="mt-1" /><span>I consent to Mira Palace storing my application details for up to 12 months for recruitment purposes, in line with the <a href="{root}legal/privacy.html" class="underline">Privacy Notice</a>.</span></label>
          <button class="inline-flex items-center justify-center px-6 py-3 bg-mira-700 text-white rounded-full font-medium hover:bg-mira-800">Submit application</button>
        </form>
      </div>
    """, bg="bg-white")
    return h + listings + form


PAGES = [
    {"path": "faq.html", "active": "faq",
     "title": "FAQ · Mira Palace",
     "description": "Twelve frequently asked questions about staying at Mira Palace — check-in, all-inclusive, children, pets, accessibility.",
     "body": faq},
    {"path": "contact.html", "active": "contact",
     "title": "Contact · Mira Palace",
     "description": "Reach Mira Palace by phone, email, WhatsApp, or enquiry form. Address, directions, and map.",
     "body": contact},
    {"path": "career.html", "active": "",
     "title": "Careers · Mira Palace",
     "description": "Open positions at Mira Palace — front desk, kitchen, spa, housekeeping, kids’ club.",
     "body": career},
]
