#requires -Version 7.4
# R029.9 — no suite pre-selected + mandatory field validation.

$ErrorActionPreference = 'Stop'
$RepoRoot = $PSScriptRoot
$Tag = 'R029.9'
$Msg = @'
R029.9: no suite pre-selected + mandatory field validation

Book page previously auto-selected King Suite on load — populating the
right column with A6 photos, basics, capacity and amenities before the
guest had picked anything. Confusing UX: it looked like the King was
already reserved / already selected.

Changes:
* _book.py: initial=None. Suite tabs render with no data-sel="true".
  Right column shows a placeholder card ("Please choose your suite")
  layered over a friendly Mira Palace garden shot (same photo used as
  the home-page hero poster). Form head displays the same placeholder
  instead of King Suite metadata. Photo count header hidden until a
  suite is picked.
* site.js selectSuite(): reveals the tiles-hd on first click,
  otherwise unchanged — the existing rebuildInfoCards() and
  rebuildTiles() already swap the placeholder out cleanly.
* site.js handleEnquirySubmit(): new pre-Turnstile validation block
  runs BEFORE the token check. Requires suite selected + arrival +
  departure + full name + email + phone. Invalid fields get
  .bk-fld-invalid styling and the first offender scrolls into view.
* custom.css: .bk-placeholder card (dashed champagne border on sand
  background) + .bk-fld-invalid input outline (red).
* i18n.js: 5 new keys x 4 languages = 20 new lines
  - bk.placeholder.h3 / .body / .hero_tag
  - bk.form_head.name_placeholder / .sub_placeholder

Enforces the enquiry-form contract: this IS a booking enquiry and every
piece of contact detail is mandatory before we take it to the hotel.
'@

$booktxt = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'scripts/pages/_book.py')
if ($booktxt -notmatch 'initial = None') { throw '_book.py still pre-selects' }
if ($booktxt -notmatch 'bk-placeholder') { throw '_book.py missing placeholder card' }

$sitejs = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'site/assets/js/site.js')
if ($sitejs -notmatch 'Please fill in:') { throw 'site.js missing mandatory-field validation' }

$en = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'site/assets/js/i18n.js')
if ($en -notmatch 'bk\.placeholder\.h3') { throw 'i18n missing placeholder keys' }

$py = $null
foreach ($c in @('python','python3','py')) { $f = Get-Command $c -ErrorAction SilentlyContinue; if ($f) { $py = $f.Source; break } }
Push-Location $RepoRoot
try {
  & $py 'scripts/build.py' 2>&1 | Out-Null
  if ($LASTEXITCODE -ne 0) { throw 'build.py failed' }
  $tw = Join-Path $RepoRoot 'tools/tailwindcss.exe'
  if (Test-Path $tw) { & $tw -i scripts/tailwind/input.css -o site/assets/css/site.css --minify 2>&1 | Out-Null }
  git add scripts/pages/_book.py site/assets/js/site.js site/assets/js/i18n.js scripts/tailwind/custom.css site/
  git add Commit-R029-9.ps1
  git commit -m $Msg
  git tag -f -a $Tag -m 'R029.9 — no suite preselect + validation'
  git push origin main
  git push --force origin "refs/tags/$Tag"
} finally { Pop-Location }

Write-Host '[R029.9] Shipped.' -ForegroundColor Green
