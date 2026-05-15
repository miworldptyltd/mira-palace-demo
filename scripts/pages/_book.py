"""Dedicated booking page — distinct from Contact, focused only on the room booking flow."""
from common import hero_slideshow, section, eyebrow, heading, lead, SITE_META

# Real King Suite + Deluxe + garden photos drive the booking hero
BOOK_HERO_IMGS = [
    "assets/img/king/king-01.jpg",
    "assets/img/deluxe/deluxe-01.jpg",
    "assets/img/garden/garden-01.jpg",
    "assets/img/king/king-05.jpg",
]


def book(root: str) -> str:
    m = SITE_META
    hero_urls = [f"{root}{u}" for u in BOOK_HERO_IMGS]
    h = hero_slideshow(hero_urls, "Book a stay",
             "Reserve your suite.",
             "Tell us your dates below and our reservations team will confirm availability and a quote as soon as possible.",
             height="58vh")

    body = section(f"""
      <div class="max-w-3xl mx-auto">

        <!-- Payment-coming-soon notice (Variation A) -->
        <div role="status" class="mb-10 rounded-lg border border-sand-300 bg-sand-100/60 p-6 shadow-sm">
          <div class="flex items-start gap-4">
            <span aria-hidden="true" class="shrink-0 w-9 h-9 grid place-items-center rounded-full bg-sand-300 text-mira-900 font-display text-lg">i</span>
            <div>
              <h3 class="font-display text-xl text-mira-900">Online payment — coming soon</h3>
              <p class="mt-2 text-sm text-mira-800 leading-relaxed">
                Secure card payment is on its way to Mira Palace. While we finalise our payment gateway, please send us your booking request below. Our reservations team will reach out as soon as possible to confirm availability and arrange your deposit by bank transfer or card. Thank you for your patience — we look forward to welcoming you.
              </p>
            </div>
          </div>
        </div>

        {eyebrow('Direct-booking enquiry')}
        {heading('Tell us when and how many.', 3)}
        {lead("Direct guests get our best available rate, plus small extras: a bottle of local wine on arrival and complimentary late check-out when the suite can stay open.")}

        <form action="mailto:{m['email']}?subject=Booking%20enquiry%20-%20Mira%20Palace" method="post" enctype="text/plain"
              class="mt-10 bg-white rounded-lg shadow-lux p-8 space-y-6"
              onsubmit="event.preventDefault(); document.getElementById('book-thanks').classList.remove('hidden'); this.style.display='none';">

          <div class="grid sm:grid-cols-2 gap-5">
            <label class="block">
              <span class="text-sm font-medium text-mira-800">Arrival</span>
              <input required type="date" name="arrival" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2.5 text-sm focus:border-mira-700 focus:ring-0" />
            </label>
            <label class="block">
              <span class="text-sm font-medium text-mira-800">Departure</span>
              <input required type="date" name="departure" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2.5 text-sm focus:border-mira-700 focus:ring-0" />
            </label>
            <label class="block">
              <span class="text-sm font-medium text-mira-800">Adults</span>
              <input required type="number" min="1" max="6" value="2" name="adults" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2.5 text-sm" />
            </label>
            <label class="block">
              <span class="text-sm font-medium text-mira-800">Children</span>
              <input type="number" min="0" max="4" value="0" name="children" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2.5 text-sm" />
            </label>
            <label class="block sm:col-span-2">
              <span class="text-sm font-medium text-mira-800">Suite preference</span>
              <select name="suite" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2.5 text-sm">
                <option value="">Recommend the best fit for my dates</option>
                <option>Standard Suite (22 m², garden view)</option>
                <option>Deluxe Suite (28 m², sea view)</option>
                <option>Family Suite (34 m², garden view)</option>
                <option>King Suite (42 m², sea view)</option>
              </select>
            </label>
          </div>

          <hr class="border-mira-200" />

          <div class="grid sm:grid-cols-2 gap-5">
            <label class="block">
              <span class="text-sm font-medium text-mira-800">Your name</span>
              <input required name="name" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2.5 text-sm" />
            </label>
            <label class="block">
              <span class="text-sm font-medium text-mira-800">Email</span>
              <input required type="email" name="email" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2.5 text-sm" />
            </label>
            <label class="block sm:col-span-2">
              <span class="text-sm font-medium text-mira-800">Phone (optional, helps us reply quickly)</span>
              <input type="tel" name="phone" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2.5 text-sm" />
            </label>
            <label class="block sm:col-span-2">
              <span class="text-sm font-medium text-mira-800">Anything we should know?</span>
              <textarea name="message" rows="3" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2.5 text-sm" placeholder="Anniversary, dietary needs, accessibility, late arrival, transfer required…"></textarea>
            </label>
          </div>

          <label class="flex items-start gap-3 text-xs text-mira-700">
            <input type="checkbox" required class="mt-1" />
            <span>I consent to Mira Palace using these details to process my booking enquiry, in line with the <a href="{root}legal/privacy.html" class="underline">Privacy Notice</a>.</span>
          </label>

          <button class="w-full inline-flex items-center justify-center px-7 py-3.5 bg-mira-700 text-white rounded-full font-medium tracking-wide hover:bg-mira-800 transition">
            Send booking enquiry
          </button>
          <p class="text-center text-xs text-mira-600">We reply within the hour during the working day. Phones are answered 24/7 — call <a href="tel:{m['phone_tel']}" class="underline">{m['phone_display']}</a> or WhatsApp anytime.</p>
        </form>

        <div id="book-thanks" class="hidden mt-10 bg-white rounded-lg shadow-lux p-10 text-center">
          <div class="w-14 h-14 mx-auto rounded-full bg-sand-300 grid place-items-center">
            <svg class="w-7 h-7 text-mira-900" viewBox="0 0 24 24" fill="none"><path stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
          </div>
          <h3 class="mt-5 font-display text-3xl text-mira-900">Enquiry sent.</h3>
          <p class="mt-3 text-mira-700">We'll be back to you within the hour with availability and a direct rate. Thank you for choosing to write to us directly.</p>
        </div>

        <div class="mt-10 grid sm:grid-cols-3 gap-4 text-center text-sm">
          <a href="tel:{m['phone_tel']}" class="p-5 bg-mira-50 rounded-lg hover:bg-mira-200 transition">
            <div class="text-xs uppercase tracking-widest text-mira-600">Call</div>
            <div class="mt-1 font-medium text-mira-900">{m['phone_display']}</div>
          </a>
          <a href="{m['whatsapp']}" rel="noopener" class="p-5 bg-mira-50 rounded-lg hover:bg-mira-200 transition">
            <div class="text-xs uppercase tracking-widest text-mira-600">WhatsApp</div>
            <div class="mt-1 font-medium text-mira-900">Same number, faster</div>
          </a>
          <a href="mailto:{m['email']}" class="p-5 bg-mira-50 rounded-lg hover:bg-mira-200 transition">
            <div class="text-xs uppercase tracking-widest text-mira-600">Email</div>
            <div class="mt-1 font-medium text-mira-900">{m['email']}</div>
          </a>
        </div>
      </div>
    """, bg="bg-sand-50")

    return h + body


PAGES = [
    {"path": "book.html", "active": "",
     "title": "Book a stay · Mira Palace",
     "description": "Direct-booking enquiry form for Mira Palace — confirm your dates, room preference, and any specific requirements.",
     "body": book},
]
