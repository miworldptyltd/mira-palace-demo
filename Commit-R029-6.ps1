#requires -Version 7.4
# R029.6 — amenity pills as a green-tick confirmed-features checklist.

$ErrorActionPreference = 'Stop'
$RepoRoot = $PSScriptRoot
$Tag = 'R029.6'
$Msg = @'
R029.6: amenity pills — green checkmarks, not empty squares

Owner reported the Features & Amenities pills on book.html read like
empty selectable checkboxes. Root cause: per-amenity Tabler glyphs
(ti-wifi, ti-snowflake, ti-hanger, ti-baby-carriage, ti-iron, etc.)
which either dont exist under those names or fell outside the inlined
icon subset from R024.

Replaced the icon column with a single inline green tick SVG. Reads
as a checklist of confirmed amenities — no ambiguity that these are
what the room has, not filters to toggle.

CSS: new .bk-chip-tick (12x12, #1A8F5B green, no shrink). Pills
padded a touch more (4/10/4/8) and gap bumped 4->6 so the tick
breathes.

Per-suite amenity lists already differ (Deluxe carries "Kitchenette",
Standard/Family/King do not). Owner mentioned per-actual-room refinement
(A-floor -> garden/pool access) — that lands separately once room-by-
room inventory is confirmed.
'@

$booktxt = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'scripts/pages/_book.py')
if ($booktxt -notmatch 'bk-chip-tick') { throw '_book.py missing tick svg' }
$css = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'scripts/tailwind/custom.css')
if ($css -notmatch '\.bk-chip-tick')   { throw 'custom.css missing .bk-chip-tick' }

$py = $null
foreach ($c in @('python','python3','py')) { $f = Get-Command $c -ErrorAction SilentlyContinue; if ($f) { $py = $f.Source; break } }
Push-Location $RepoRoot
try {
  & $py 'scripts/build.py' 2>&1 | Out-Null
  if ($LASTEXITCODE -ne 0) { throw 'build.py failed' }
  $tw = Join-Path $RepoRoot 'tools/tailwindcss.exe'
  if (Test-Path $tw) { & $tw -i scripts/tailwind/input.css -o site/assets/css/site.css --minify 2>&1 | Out-Null }

  git add scripts/pages/_book.py scripts/tailwind/custom.css site/
  git add Commit-R029-6.ps1
  git commit -m $Msg
  git tag -f -a $Tag -m 'R029.6 — green tick amenities'
  git push origin main
  git push --force origin "refs/tags/$Tag"
} finally { Pop-Location }

Write-Host '[R029.6] Shipped.' -ForegroundColor Green
