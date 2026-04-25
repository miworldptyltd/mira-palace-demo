"""Dedicated booking page — distinct from Contact, focused only on the room booking flow."""
from common import hero, section, eyebrow, heading, lead, SITE_META

IMG_BOOK = "https://images.unsplash.com/photo-1611892440504-42a792e24d32?auto=format&fit=crop&w=1920&q=80"


def book(root: str) -> str:
    m = SITE_META
    h = hero(IMG_BOOK, "Book a stay",
             "Reserve your room.",
             "A real-time booking engine will sit here in the production site (Caglatur, HotelRunner, or your preferred provider). For now, fill in your dates and we'll confirm availability and a quote within an hour.",
             height="58vh")

    body = section(f"""
      <div class="max-w-3xl mx-auto">
        {eyebrow('Direct-booking enquiry')}
        {heading('Tell us when and how many.', 3)}
        {lead("Direct guests get our best available rate, plus small extras: a bottle of local wine on arrival and complimentary late check-out when the room can stay open.")}

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
              <span class="text-sm font-medium text-mira-800">Room preference</span>
              <select name="room" class="mt-1 block w-full rounded border border-mira-200 px-3 py-2.5 text-sm">
                <option value="">Recommend the best fit for my dates</option>
                <option>Standard Room (22 m², garden view)</option>
                <option>Deluxe Room (28 m², sea view)</option>
                <option>Family Connecting (34 m²)</option>
                <option>Junior Suite (42 m², sea view)</option>
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
