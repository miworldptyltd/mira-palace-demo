#requires -Version 7.4
<#
.SYNOPSIS
  R029.5b — wire the real brand mark: dark PNG in header, gold PNG in footer,
  full wordmark PNG for social/SEO, favicon left alone.
#>

$ErrorActionPreference = 'Stop'

$RepoRoot    = $PSScriptRoot
$BuildScript = Join-Path $RepoRoot 'scripts/build.py'
$Tag         = 'R029.5b'
$Msg         = @'
R029.5b: wire real brand mark — right PNG for each context

Rolled back the invented "M in gold circle" and used the actual assets:

* Header: mp-monogram-dark.png (the dark green MP monogram), inside a
  small white circle so it reads cleanly against the mid-teal nav band.
* Footer: mp-monogram-gold.png (the gold MP variant of the same
  monogram), no wrapper — it lands directly on the dark navy footer.
* JSON-LD schema.org logo: Mira_Palace_Logo.png (has wordmark) — used
  for Google's rich results + social share previews.
* favicon.svg: kept as owner-restored (dark navy square, gold M).

All three PNG assets are the ones that already lived in the repo. No new
files, no invented monograms.
'@

# Verify edits
$cm = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'scripts/common.py')
if ($cm -notmatch 'mp-monogram-dark\.png') { throw 'common.py missing header dark PNG' }
if ($cm -notmatch 'mp-monogram-gold\.png') { throw 'common.py missing footer gold PNG' }
if ($cm -notmatch 'Mira_Palace_Logo\.png') { throw 'common.py missing JSON-LD wordmark' }

# All three PNGs must be present
foreach ($f in @('mp-monogram-dark.png','mp-monogram-gold.png','Mira_Palace_Logo.png')) {
  if (-not (Test-Path (Join-Path $RepoRoot "site/assets/img/$f"))) { throw "Missing asset: $f" }
}

Write-Host '[R029.5b] Build...' -ForegroundColor Cyan
$py = $null
foreach ($c in @('python','python3','py')) { $f = Get-Command $c -ErrorAction SilentlyContinue; if ($f) { $py = $f.Source; break } }
Push-Location $RepoRoot
try {
  $out = & $py $BuildScript 2>&1
  if ($LASTEXITCODE -ne 0) { $out | ForEach-Object { Write-Host $_ }; throw 'build.py failed' }
} finally { Pop-Location }

Push-Location $RepoRoot
try {
  git add scripts/common.py site/
  git add Commit-R029-5b.ps1
  git commit -m $Msg
  git tag -f -a $Tag -m 'R029.5b — real brand mark PNGs wired'
  git push origin main
  git push --force origin "refs/tags/$Tag"
} finally { Pop-Location }

Write-Host ''
Write-Host '[R029.5b] Shipped.' -ForegroundColor Green
Write-Host '  Retry:  https://miworldptyltd.github.io/mira-palace-demo/  (hard-refresh)'
