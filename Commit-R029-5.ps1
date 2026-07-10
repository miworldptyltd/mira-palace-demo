#requires -Version 7.4
<#
.SYNOPSIS
  R029.5 — unify logo: single SVG monogram used in header + footer +
  favicon + JSON-LD. Delete orphan PNG variants.
#>

$ErrorActionPreference = 'Stop'
$InformationPreference = 'Continue'

$RepoRoot    = $PSScriptRoot
$BuildScript = Join-Path $RepoRoot 'scripts/build.py'
$Tag         = 'R029.5'
$Msg         = @'
R029.5: unify brand mark — one SVG monogram everywhere

Three visual variants of the brand mark were shipping side-by-side:
* header: mp-monogram-gold.png (bitmap M, 234x229 rendered in 36x36)
* footer: CSS-drawn <span> rounded-full with M text in Cormorant
* favicon: SVG rendering as dark navy square with gold M

Result: browser tab, page header, and page footer all showed a
different logo — worst offender was the favicon which looked like a
different brand entirely.

Consolidated to one canonical asset:
* site/assets/img/mp-monogram.svg — gold circle, dark navy M path.
  Same viewBox as favicon so both are pixel-identical.
* header <img> now points at mp-monogram.svg
* footer <span>M</span> replaced with <img src="mp-monogram.svg">
* favicon.svg redrawn to match (circle instead of rect, colors swapped)
* JSON-LD "logo" field now points at the SVG

Orphan files removed:
* mp-monogram-gold.png    (superseded)
* mp-monogram-dark.png    (unreferenced; never appeared in code)
* Mira_Palace_Logo.png    (unreferenced; likely an owner supply)
'@

# Delete orphans (repo files, not our sandbox)
$orphans = @(
  (Join-Path $RepoRoot 'site/assets/img/mp-monogram-gold.png'),
  (Join-Path $RepoRoot 'site/assets/img/mp-monogram-dark.png'),
  (Join-Path $RepoRoot 'site/assets/img/Mira_Palace_Logo.png')
)
foreach ($o in $orphans) {
  if (Test-Path -LiteralPath $o) {
    Remove-Item -LiteralPath $o -Force
    Write-Information "  [rm] $(Split-Path $o -Leaf)"
  }
}

# Preflight
if (-not (Test-Path (Join-Path $RepoRoot 'site/assets/img/mp-monogram.svg'))) {
  throw 'mp-monogram.svg missing.'
}

$cm = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'scripts/common.py')
if ($cm -match 'mp-monogram-gold.png') { throw 'common.py still references mp-monogram-gold.png' }
if ($cm -notmatch 'mp-monogram\.svg')  { throw 'common.py missing mp-monogram.svg' }

# Build
Write-Information '[R029.5] Build...'
$py = $null
foreach ($c in @('python','python3','py')) { $f = Get-Command $c -ErrorAction SilentlyContinue; if ($f) { $py = $f.Source; break } }
if (-not $py) { throw 'No python on PATH.' }
Push-Location $RepoRoot
try {
  $out = & $py $BuildScript 2>&1
  if ($LASTEXITCODE -ne 0) { $out | ForEach-Object { Write-Host $_ }; throw 'build.py failed' }
} finally { Pop-Location }

# Ship
Push-Location $RepoRoot
try {
  git add scripts/common.py
  git add site/assets/img/mp-monogram.svg site/assets/img/favicon.svg
  git rm -f --ignore-unmatch site/assets/img/mp-monogram-gold.png site/assets/img/mp-monogram-dark.png site/assets/img/Mira_Palace_Logo.png 2>&1 | Out-Null
  git add site/
  git add Commit-R029-5.ps1
  git commit -m $Msg
  git tag -f -a $Tag -m 'R029.5 — unified brand mark SVG'
  git push origin main
  git push --force origin "refs/tags/$Tag"
} finally { Pop-Location }

Write-Host ''
Write-Host '[R029.5] Shipped.' -ForegroundColor Green
Write-Host '  Retry:  https://miworldptyltd.github.io/mira-palace-demo/  (hard-refresh browser tab too — favicon caches aggressively)'
