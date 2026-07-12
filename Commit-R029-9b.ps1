#requires -Version 7.4
# R029.9b — Fullscreen + View all buttons now open a real lightbox.

$ErrorActionPreference = 'Stop'
$RepoRoot = $PSScriptRoot
$Tag = 'R029.9b'
$Msg = @'
R029.9b: photo lightbox — Fullscreen + View all now work

The Fullscreen button on the booking hero and the View all button next
to "More photos" were rendered but had no JS handlers. Owner reported
they did nothing.

Built a proper lightbox modal from scratch:
* Hidden overlay markup in _book.py (dark backdrop, centred image,
  prev / next arrows, close X, caption, counter).
* CSS in custom.css — fixed positioning, mobile-friendly sizes at
  <=640px, semi-transparent controls.
* JS in site.js — openLightbox() reveals the modal + shows the photo;
  ESC / backdrop click / close button all close; arrow keys navigate;
  body scroll locked while open.

Wiring:
* Fullscreen button on hero opens lightbox at the current hero photo.
  If a suite is picked, the full suite gallery is available for nav.
  In placeholder mode (before a suite is picked), shows the garden
  hero alone with no arrows.
* View all button opens the full gallery at photo 1.
* Tile clicks unchanged — they still swap the hero preview (existing
  behaviour, not affected).

No new i18n keys — button labels already have data-i18n on them.
'@

$booktxt = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'scripts/pages/_book.py')
if ($booktxt -notmatch 'bk-lightbox') { throw '_book.py missing lightbox markup' }

$sitejs = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'site/assets/js/site.js')
if ($sitejs -notmatch 'openLightbox') { throw 'site.js missing openLightbox' }

$css = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'scripts/tailwind/custom.css')
if ($css -notmatch '\.bk-lightbox') { throw 'custom.css missing .bk-lightbox' }

$py = $null
foreach ($c in @('python','python3','py')) { $f = Get-Command $c -ErrorAction SilentlyContinue; if ($f) { $py = $f.Source; break } }
Push-Location $RepoRoot
try {
  & $py 'scripts/build.py' 2>&1 | Out-Null
  if ($LASTEXITCODE -ne 0) { throw 'build.py failed' }
  $tw = Join-Path $RepoRoot 'tools/tailwindcss.exe'
  if (Test-Path $tw) { & $tw -i scripts/tailwind/input.css -o site/assets/css/site.css --minify 2>&1 | Out-Null }
  git add scripts/pages/_book.py site/assets/js/site.js scripts/tailwind/custom.css site/
  git add Commit-R029-9b.ps1
  git commit -m $Msg
  git tag -f -a $Tag -m 'R029.9b — photo lightbox'
  git push origin main
  git push --force origin "refs/tags/$Tag"
} finally { Pop-Location }

Write-Host '[R029.9b] Shipped.' -ForegroundColor Green
