#requires -Version 7.4
<#
.SYNOPSIS
  R029 — ship the email pipeline: real Turnstile Site Key + real fetch() +
  Worker source under version control.

.DESCRIPTION
  Preflight paths + local build smoke test + git-state audit + stage + commit
  + tag + push. Mirrors Commit-R028.ps1 pattern.
#>

$ErrorActionPreference = 'Stop'
$InformationPreference = 'Continue'

$RepoRoot    = $PSScriptRoot
$WorkerJs    = Join-Path $RepoRoot 'worker/mira-palace-enquiry.js'
$WranglerTml = Join-Path $RepoRoot 'worker/wrangler.toml'
$BookPy      = Join-Path $RepoRoot 'scripts/pages/_book.py'
$SpaBookPy   = Join-Path $RepoRoot 'scripts/pages/_spa_book.py'
$SiteJs      = Join-Path $RepoRoot 'site/assets/js/site.js'
$BuildScript = Join-Path $RepoRoot 'scripts/build.py'
$SitePath    = Join-Path $RepoRoot 'site'
$Tag         = 'R029'
$Msg         = @'
R029: wire the enquiry pipeline — Worker + real Turnstile + real fetch

Previously the form was a stub: submit ran validation, showed the pretty
thank-you card, and console.info(payload). Nothing left the browser.

This ships:
* worker/mira-palace-enquiry.js  new Cloudflare Worker source under Git.
  CORS + origin allowlist + JSON guard + 16 KB body cap + per-IP rate limit
  (KV, optional) + server-side Turnstile verify + input sanitisation +
  Resend forward + HTML email template designed for hotel staff.
* worker/wrangler.toml + README.md for future CLI deploys.
* site/assets/js/site.js: real fetch() to the Worker (was commented out).
  Submit button disables during send; failure rolls back UI + resets
  Turnstile so guest can retry.
* scripts/pages/_book.py + _spa_book.py: real Turnstile Site Key
  (0x4AAAAAADw1GxGvpcClGqV8, widget "mira-palace-enquiry"). Stub-phase
  copy replaced.

Worker + all 5 secrets already deployed to Cloudflare via API. This ship
carries the site changes that make the client POST to it.
'@

# --- Preflight ---
Write-Information '[R029] Preflight...'
foreach ($p in @($WorkerJs, $WranglerTml, $BookPy, $SpaBookPy, $SiteJs, $BuildScript)) {
  if (-not (Test-Path -LiteralPath $p)) { throw "Missing: $p" }
}

# --- Verify edits landed ---
$booktxt = Get-Content -Raw -LiteralPath $BookPy
if ($booktxt -notmatch '0x4AAAAAADw1GxGvpcClGqV8') { throw '_book.py missing real Site Key' }
if ($booktxt -match '1x00000000000000000000AA') { throw '_book.py still has test key' }

$spatxt = Get-Content -Raw -LiteralPath $SpaBookPy
if ($spatxt -notmatch '0x4AAAAAADw1GxGvpcClGqV8') { throw '_spa_book.py missing real Site Key' }

$sitejs = Get-Content -Raw -LiteralPath $SiteJs
if ($sitejs -match 'payload \(stub . not sent\)') { throw 'site.js still logs stub payload' }
if ($sitejs -notmatch 'fetch\(form\.action') { throw 'site.js missing real fetch()' }
Write-Information '  [ok] source edits verified'

# --- Local build smoke test ---
Write-Information '[R029] Local build...'
$pythonCmd = $null
foreach ($c in @('python','python3','py')) {
  $f = Get-Command $c -ErrorAction SilentlyContinue
  if ($f) { $pythonCmd = $f.Source; break }
}
if (-not $pythonCmd) { throw 'No python on PATH.' }
Push-Location $RepoRoot
try {
  $out = & $pythonCmd $BuildScript 2>&1
  if ($LASTEXITCODE -ne 0) { $out | ForEach-Object { Write-Host $_ }; throw 'build.py failed' }
  if (-not (Test-Path (Join-Path $SitePath 'book.html'))) { throw 'site/book.html missing after build' }
  Write-Information '  [ok] built cleanly'
} finally { Pop-Location }

# --- Git state audit ---
Write-Information '[R029] Auditing git state...'
Push-Location $RepoRoot
try {
  $status = git status --porcelain=v1
  if (-not $status) { throw 'Working tree clean — edits lost?' }

  $allowed = @(
    'worker/mira-palace-enquiry.js', 'worker/wrangler.toml', 'worker/README.md',
    'scripts/pages/_book.py', 'scripts/pages/_spa_book.py',
    'site/assets/js/site.js',
    'RELEASE_NOTES.md', 'Commit-R029.ps1', 'Set-WorkerSecrets.ps1',
    'Commit-R028.ps1'
  )
  $offenders = $status | Where-Object {
    $path = ($_.Substring(3)).Trim('"')
    $ok = $false
    foreach ($a in $allowed) { if ($path -eq $a) { $ok = $true; break } }
    if (-not $ok -and ($path -like 'site/*' -or $path -like 'site\*')) { $ok = $true }
    if (-not $ok -and ($path -like 'worker/*' -or $path -like 'worker\*' -or $path -eq 'worker/' -or $path -eq 'worker')) { $ok = $true }
    -not $ok
  }
  if ($offenders) {
    Write-Host '[R029] Unexpected dirty files:' -ForegroundColor Yellow
    $offenders | ForEach-Object { Write-Host "    $_" }
    throw 'Fix tree first, then re-run.'
  }

  # Guard: never commit real secrets in the redacted script.
  $spsTxt = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'Set-WorkerSecrets.ps1')
  if ($spsTxt -match 're_[A-Za-z0-9_]{20,}' -or $spsTxt -match 'cfut_[A-Za-z0-9]{20,}') {
    throw 'Set-WorkerSecrets.ps1 still contains real secrets — redact before shipping.'
  }

  Write-Host ''
  Write-Host '===== files being shipped =====' -ForegroundColor Cyan
  git status --short
  Write-Host '===============================' -ForegroundColor Cyan
  Write-Host ''
} finally { Pop-Location }

# --- Stage / commit / tag / push ---
Write-Information '[R029] Staging...'
Push-Location $RepoRoot
try {
  git add worker/mira-palace-enquiry.js worker/wrangler.toml worker/README.md
  git add scripts/pages/_book.py scripts/pages/_spa_book.py
  git add site/assets/js/site.js
  git add RELEASE_NOTES.md Commit-R029.ps1 Set-WorkerSecrets.ps1

  git commit -m $Msg
  if ($LASTEXITCODE -ne 0) { throw 'git commit failed' }

  git tag -f -a $Tag -m 'R029 — enquiry pipeline live'
  git push origin main
  if ($LASTEXITCODE -ne 0) { throw 'git push main failed' }
  git push --force origin "refs/tags/$Tag"
  if ($LASTEXITCODE -ne 0) { throw 'git push tag failed' }
} finally { Pop-Location }

Write-Host ''
Write-Host '[R029] Shipped.' -ForegroundColor Green
Write-Host '  Actions:   https://github.com/miworldptyltd/mira-palace-demo/actions'
Write-Host '  Live URL:  https://miworldptyltd.github.io/mira-palace-demo/book.html'
