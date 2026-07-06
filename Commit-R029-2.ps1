#requires -Version 7.4
<#
.SYNOPSIS
  R029.2 — ship arrival-time select + info popover + 12h blurb format.
#>

$ErrorActionPreference = 'Stop'
$InformationPreference = 'Continue'

$RepoRoot    = $PSScriptRoot
$BuildScript = Join-Path $RepoRoot 'scripts/build.py'
$Tag         = 'R029.2'
$Msg         = @'
R029.2: arrival-time select + info popover + 12h checkout blurb

Killed the native <input type="time"> browser-wheel picker. Guests were
seeing a minute-granularity vertical scroll (03/04/05...) with no snap
to 15-min steps, inconsistent across Brave/Chrome/Safari.

Replaced with a styled <select> — "Not sure yet" default, 30-min slots
06:00 through midnight, plus "After midnight (late arrival)". 14:00
labelled with "check-in opens" hint so guests know when the room is
first available.

Also lands:
* Booking blurb reformatted to two-line 12h — "Check-in: From 2:00 PM"
  and "Check-out: By 12:00 noon" with a small info icon next to
  Check-out. Click reveals a small popover about late-night arrivals
  not extending checkout time.
* initInfoPops() — reusable click-toggle popover pattern for future
  info icons. Outside-click and ESC close.
* CSS for .bk-info-btn + .bk-info-pop + .bk-note-line.
'@

foreach ($p in @($BuildScript)) { if (-not (Test-Path $p)) { throw "Missing: $p" } }

# Verify edits landed
$booktxt = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'scripts/pages/_book.py')
if ($booktxt -notmatch 'bk-info-btn')            { throw '_book.py missing info button' }
if ($booktxt -notmatch 'Not sure yet')           { throw '_book.py missing arrival-time select' }
if ($booktxt -match 'input type="time" id="bk-arrival-time"') { throw '_book.py still has native time input' }

$sitejs = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'site/assets/js/site.js')
if ($sitejs -notmatch 'initInfoPops') { throw 'site.js missing initInfoPops' }

$css = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'scripts/tailwind/custom.css')
if ($css -notmatch '\.bk-info-btn') { throw 'custom.css missing .bk-info-btn' }

# Local build
Write-Information '[R029.2] Build...'
$py = $null
foreach ($c in @('python','python3','py')) { $f = Get-Command $c -ErrorAction SilentlyContinue; if ($f) { $py = $f.Source; break } }
if (-not $py) { throw 'No python on PATH.' }
Push-Location $RepoRoot
try {
  $out = & $py $BuildScript 2>&1
  if ($LASTEXITCODE -ne 0) { $out | ForEach-Object { Write-Host $_ }; throw 'build.py failed' }
  Write-Information '  [ok]'
} finally { Pop-Location }

# Tailwind rebuild
Push-Location $RepoRoot
try {
  $tw = Join-Path $RepoRoot 'tools/tailwindcss.exe'
  if (Test-Path $tw) {
    & $tw -i scripts/tailwind/input.css -o site/assets/css/site.css --minify 2>&1 | Out-Null
    Write-Information '[R029.2] Tailwind rebuilt'
  }
} finally { Pop-Location }

# Ship
Push-Location $RepoRoot
try {
  git add scripts/pages/_book.py site/assets/js/site.js scripts/tailwind/custom.css
  git add site/
  git add Commit-R029-2.ps1
  git commit -m $Msg
  git tag -f -a $Tag -m 'R029.2 — arrival-time select + info popover'
  git push origin main
  git push --force origin "refs/tags/$Tag"
} finally { Pop-Location }

Write-Host ''
Write-Host '[R029.2] Shipped.' -ForegroundColor Green
Write-Host '  Retry:  https://miworldptyltd.github.io/mira-palace-demo/book.html'
