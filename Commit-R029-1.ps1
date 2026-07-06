#requires -Version 7.4
<#
.SYNOPSIS
  R029.1 — date-picker fixes + arrival-time input + check-out blurb.
#>

$ErrorActionPreference = 'Stop'
$InformationPreference = 'Continue'

$RepoRoot    = $PSScriptRoot
$BuildScript = Join-Path $RepoRoot 'scripts/build.py'
$SitePath    = Join-Path $RepoRoot 'site'
$Tag         = 'R029.1'
$Msg         = @'
R029.1: date guards + arrival time + checkout blurb

Smoke test caught two UX gaps:
* date pickers happily accepted past dates
* no clarity on same-day arrivals / 12:00 checkout

Changes:
* _book.py: arrival input carries data-min=today, departure carries
  data-min=arrival. New inline blurb: "Check-in from 14:00, check-out
  by 12:00 — regardless of arrival time. Same-day arrivals welcome."
* _book.py: "Estimated arrival" bucket-select replaced with a proper
  24-hour <input type="time"> (step 900s = 15 min).
* _spa_book.py: date input min = today.
* site.js: initDateGuards() reads data-min, sets .min live, syncs
  departure whenever arrival changes.
* custom.css: styles for .bk-note-inline and .bk-lbl-hint.

Also carries the R029 Update-WorkerToEmail.ps1 redaction and any other
tree cleanup.
'@

# Preflight
foreach ($p in @($BuildScript)) { if (-not (Test-Path -LiteralPath $p)) { throw "Missing: $p" } }

# Verify edits landed
$booktxt = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'scripts/pages/_book.py')
if ($booktxt -notmatch 'data-min="today"') { throw '_book.py missing data-min=today' }
if ($booktxt -notmatch 'bk-note-inline')   { throw '_book.py missing checkout blurb' }
if ($booktxt -notmatch 'input type="time" id="bk-arrival-time"') { throw '_book.py missing time input' }

$sitejs = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'site/assets/js/site.js')
if ($sitejs -notmatch 'initDateGuards') { throw 'site.js missing initDateGuards' }

# Local build
Write-Information '[R029.1] Local build...'
$pythonCmd = $null
foreach ($c in @('python','python3','py')) { $f = Get-Command $c -ErrorAction SilentlyContinue; if ($f) { $pythonCmd = $f.Source; break } }
if (-not $pythonCmd) { throw 'No python on PATH.' }
Push-Location $RepoRoot
try {
  $out = & $pythonCmd $BuildScript 2>&1
  if ($LASTEXITCODE -ne 0) { $out | ForEach-Object { Write-Host $_ }; throw 'build.py failed' }
  Write-Information '  [ok]'
} finally { Pop-Location }

# Tailwind
Write-Information '[R029.1] Tailwind rebuild...'
Push-Location $RepoRoot
try {
  $tw = Join-Path $RepoRoot 'tools/tailwindcss.exe'
  if (Test-Path $tw) {
    & $tw -i scripts/tailwind/input.css -o site/assets/css/site.css --minify 2>&1 | Out-Null
    Write-Information '  [ok] tailwind rebuilt'
  } else {
    Write-Warning '  tools/tailwindcss.exe not found — CSS may be stale. GH Actions will still rebuild.'
  }
} finally { Pop-Location }

# Ship
Push-Location $RepoRoot
try {
  git add scripts/pages/_book.py scripts/pages/_spa_book.py
  git add site/assets/js/site.js scripts/tailwind/custom.css
  git add site/
  git add Update-WorkerToEmail.ps1 Commit-R029-1.ps1
  git commit -m $Msg
  git tag -f -a $Tag -m 'R029.1 — date guards + arrival time + checkout blurb'
  git push origin main
  git push --force origin "refs/tags/$Tag"
} finally { Pop-Location }

Write-Host ''
Write-Host '[R029.1] Shipped.' -ForegroundColor Green
Write-Host '  Actions:  https://github.com/miworldptyltd/mira-palace-demo/actions'
Write-Host '  Retry:    https://miworldptyltd.github.io/mira-palace-demo/book.html'
