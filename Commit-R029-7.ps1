#requires -Version 7.4
# R029.7 — English P1 sweep. Facts + hero H1s + form CTAs + rate alignment.

$ErrorActionPreference = 'Stop'
$RepoRoot = $PSScriptRoot
$Tag = 'R029.7'
$Msg = @'
R029.7: English P1 sweep — vetted BrE source ready for translation

Full site copy audit (SME, 25-min brief) flagged ~40 P1 rewrites plus 13
factual errors. This ship carries the highest-impact fixes:

FACTUAL
* Home meta description: was "Four pools, private beach 600 m." Now
  correctly says two pools, Blue-Flag public beach seven minutes down
  the lane.
* JSON-LD Hotel description + footer tagline: same fix — Google was
  being told the wrong beach + distance every crawl.
* Room rate tags (i18n) aligned with the central PRICES registry in
  common.py — 130/180/220/290 -> 180/240/290/420. One source of truth.

HERO H1s
* Home:  "The Turkish Riviera, reimagined in quiet luxury."
  ->      "Thirty-four suites on the Turkish Riviera."
* About: "Small hotel. Big intent."
  ->      "Thirty-four suites, opened in 2022 by one family."
* Spa:   "A hammam in the old way. A spa menu in the quiet way."
  ->      "A Turkish hammam, done the old way. Three treatments, kept
           short on purpose."
Reason: the site's best-performing headline pattern is factual H1 +
literary sub (see rooms.index.h1). Three flagship pages were doing the
opposite. Aman/Passalacqua pattern.

VOICE / FORM CTAs
* bk.page.h1  "Send an enquiry" -> "Enquire about a stay"
* sp.page.h1  "Spa enquiry"     -> "Enquire about a spa session"
* Same fix applied to the hardcoded H1 in _book.py + _spa_book.py (now
  tagged data-i18n so translators pick them up automatically).
* bk.request_booking / sp.request_session  "Send enquiry ->"
  ->  "Send my enquiry"  (drop decorative arrow, personal pronoun softens)
* bk.stay_until  "Stay until"  ->  "Late checkout until"
  Ambiguous form label -> concrete late-checkout picker.
* contact.form.h3  "Send an enquiry"  ->  "Write to us"
* bk.thanks.body / sp.thanks.body — "We'll be back to you" replaced
  with "You'll hear from us" (rest of the site addresses "you").

HOME BODY
* home.hero.sub — em-dash pile-up removed, cypress-lane reference
  dropped (used four times site-wide).
* home.intro.h2  "Big-hotel comfort, small-hotel soul."
  ->  "A resort's comforts, kept small enough to feel personal."

DEFERRED to R029.7b
* ~40 P2 body copy tightening rewrites
* Untagged hardcoded strings across _book.py, _spa_book.py,
  _faq_contact_career.py, _concept.py, _home.py, _pools_spa.py,
  _gallery_offers.py, _activities_location.py, _legal_404.py (about
  ~200 strings that will otherwise ship English-only after translation)
* Chef quote fact-check + demo-only content flags

British English throughout. All TR/DE/RU blocks untouched — those are
about to be replaced wholesale by three parallel SMEs against this
vetted EN source (R029.8).
'@

# Verify a couple of the changes landed
$en = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'site/assets/js/i18n.js')
if ($en -match 'Send enquiry .*→') { throw 'bk.request_booking arrow still present' }
if ($en -notmatch 'Thirty-four suites on the Turkish Riviera') { throw 'home.hero.h1 not updated' }
if ($en -notmatch 'From €180 / night') { throw 'standard rate not updated' }

$cm = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'scripts/common.py')
if ($cm -match '600 metres from the Mediterranean') { throw 'footer/JSON-LD still wrong' }

$py = $null
foreach ($c in @('python','python3','py')) { $f = Get-Command $c -ErrorAction SilentlyContinue; if ($f) { $py = $f.Source; break } }
Push-Location $RepoRoot
try {
  & $py 'scripts/build.py' 2>&1 | Out-Null
  if ($LASTEXITCODE -ne 0) { throw 'build.py failed' }

  git add scripts/common.py scripts/pages/_home.py scripts/pages/_book.py scripts/pages/_spa_book.py
  git add site/assets/js/i18n.js site/
  git add Commit-R029-7.ps1
  git commit -m $Msg
  git tag -f -a $Tag -m 'R029.7 — EN copy P1'
  git push origin main
  git push --force origin "refs/tags/$Tag"
} finally { Pop-Location }

Write-Host '[R029.7] Shipped.' -ForegroundColor Green
