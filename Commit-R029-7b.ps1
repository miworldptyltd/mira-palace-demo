#requires -Version 7.4
# R029.7b — P2 body-copy tightening on existing i18n keys.

$ErrorActionPreference = 'Stop'
$RepoRoot = $PSScriptRoot
$Tag = 'R029.7b'
$Msg = @'
R029.7b: EN P2 body-copy tightening (BrE)

16 additional rewrites to existing i18n keys, applied on top of R029.7's
P1 pass. Highlights:

VOICE
* home.intro.kicker: "A quieter kind of resort" -> "A quieter kind of
  all-inclusive" (honest positioning against loud AI resorts).
* about.values.h2: "Three promises, kept quietly." -> "Three things we
  promise." (drops decoration.)
* about.values.3.title: "Of the place" -> "Made where we live."
* contact.hero.sub: "prefer the detail on paper" -> "rather have it in
  writing"; "24/7" -> "around the clock".

BOOKING + SPA FORMS
* bk.payment_note, sp.payment_note: "No payment now" -> "No payment
  taken"; garden-path phrasing untangled.
* bk.notes.placeholder / sp.notes.placeholder: keyword lists rewritten
  as prompts.
* sp.room_number.hint: "(if a hotel guest)" -> "(if you're staying with
  us)".
* bk.airline_hint: "auto-filled from flight number" -> "filled in from
  your flight number".

ROOMS + SPA
* rooms.index.h1: "Four ways to sleep" -> "Four kinds of room" (was
  slightly cute for a room-inventory H1).
* room.short.family: en-suite claim was inaccurate — bathroom is
  shared, not attached; new copy names it plainly.
* spa.pkgs.h2: "an afternoon" -> "a couple of hours" (two of three
  packages are under 90 min).
* spa.etq.6.d: "text the WhatsApp" -> "WhatsApp us using the button".
* spa.pkgs.foot: grammar tidied.

DEMO BANNER
* demo.banner: dropped the ALL-CAPS "DEMONSTRATION SITE"; sentence
  case matches the rest of the site.

DEFERRED to R029.7c
* Untagged strings in _book.py, _spa_book.py, _faq_contact_career.py,
  _home.py intro paragraphs, _pools_spa.py, _concept.py, _gallery_offers.py,
  _activities_location.py, _legal_404.py — approximately 200 EN strings
  that need data-i18n tagging before translators can pick them up.

Untouched. Only English strings changed; TR/DE/RU blocks preserved for
the wholesale replacement in R029.8.
'@

$en = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'site/assets/js/i18n.js')
if ($en -notmatch 'A quieter kind of all-inclusive') { throw 'P2 not applied' }
if ($en -notmatch 'Four kinds of room')              { throw 'rooms.index.h1 not updated' }
if ($en -cmatch 'DEMONSTRATION SITE')                { throw 'demo banner still all caps' }

$py = $null
foreach ($c in @('python','python3','py')) { $f = Get-Command $c -ErrorAction SilentlyContinue; if ($f) { $py = $f.Source; break } }
Push-Location $RepoRoot
try {
  & $py 'scripts/build.py' 2>&1 | Out-Null
  if ($LASTEXITCODE -ne 0) { throw 'build.py failed' }
  git add site/assets/js/i18n.js site/ Commit-R029-7b.ps1
  git commit -m $Msg
  git tag -f -a $Tag -m 'R029.7b — EN P2 tightening'
  git push origin main
  git push --force origin "refs/tags/$Tag"
} finally { Pop-Location }

Write-Host '[R029.7b] Shipped.' -ForegroundColor Green
