#requires -Version 7.4
# R029.2b — remove native time pickers from airport + otogar add-ons.

$ErrorActionPreference = 'Stop'
$InformationPreference = 'Continue'

$RepoRoot    = $PSScriptRoot
$BuildScript = Join-Path $RepoRoot 'scripts/build.py'
$Tag         = 'R029.2b'
$Msg         = @'
R029.2b: transfer add-ons — same styled arrival-time select

The airport + otogar add-ons still shipped native <input type="time">
which shows the browser wheel-picker (03/04/05…) that we killed on the
main form in R029.2. This carries the same fix to both add-ons:

* New _arrival_time_select() helper in _book.py — one source of truth
  for the 30-min slot dropdown. Emits 06:00 through 23:30 plus midnight,
  plus "Not sure yet" default and "After midnight (late arrival)".
* Airport transfer arrival-time -> _arrival_time_select("airport_arrival_time")
* Otogar transfer arrival-time  -> _arrival_time_select("otogar_arrival_time")
* Both add-on arrival-date inputs now carry data-min="today" so past
  dates are refused (same as the main dates block).

Grep confirmed zero <input type="time"> left in scripts/.
'@

foreach ($p in @($BuildScript)) { if (-not (Test-Path $p)) { throw "Missing: $p" } }

$booktxt = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'scripts/pages/_book.py')
if ($booktxt -match 'input type="time"') { throw '_book.py still has native time input' }
if ($booktxt -notmatch '_arrival_time_select') { throw '_book.py missing shared helper' }
if ($booktxt -notmatch 'airport_arrival_time') { throw '_book.py airport not wired' }
if ($booktxt -notmatch 'otogar_arrival_time')  { throw '_book.py otogar not wired' }

Write-Information '[R029.2b] Build...'
$py = $null
foreach ($c in @('python','python3','py')) { $f = Get-Command $c -ErrorAction SilentlyContinue; if ($f) { $py = $f.Source; break } }
if (-not $py) { throw 'No python on PATH.' }
Push-Location $RepoRoot
try {
  $out = & $py $BuildScript 2>&1
  if ($LASTEXITCODE -ne 0) { $out | ForEach-Object { Write-Host $_ }; throw 'build.py failed' }
} finally { Pop-Location }

# Tailwind
Push-Location $RepoRoot
try {
  $tw = Join-Path $RepoRoot 'tools/tailwindcss.exe'
  if (Test-Path $tw) {
    & $tw -i scripts/tailwind/input.css -o site/assets/css/site.css --minify 2>&1 | Out-Null
  }
} finally { Pop-Location }

# Ship
Push-Location $RepoRoot
try {
  git add scripts/pages/_book.py
  git add site/
  git add Commit-R029-2b.ps1
  git commit -m $Msg
  git tag -f -a $Tag -m 'R029.2b — transfer add-ons arrival-time select'
  git push origin main
  git push --force origin "refs/tags/$Tag"
} finally { Pop-Location }

Write-Host ''
Write-Host '[R029.2b] Shipped.' -ForegroundColor Green
Write-Host '  Retry:  https://miworldptyltd.github.io/mira-palace-demo/book.html'
