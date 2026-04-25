# Publish-Site.ps1 — rebuild the site, commit, and push to GitHub.
# Use this for ALL updates after the first Init-Repo.ps1 run.
# Self-contained per Agent Working Agreement §10.

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $root

Write-Host ""
Write-Host "Mira Palace - Publish to GitHub" -ForegroundColor Cyan
Write-Host "===============================" -ForegroundColor Cyan

# Sanity: must already be a git repo (Init-Repo.ps1 should have run once).
if (-not (Test-Path ".git")) {
  Write-Host "  No .git folder yet. Run Init-Repo.ps1 first." -ForegroundColor Red
  exit 1
}

# 1. Rebuild static site so the latest content goes up.
Write-Host ""
Write-Host "[1/4] Rebuilding site..." -ForegroundColor Cyan
$python = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $python) { $python = (Get-Command python3 -ErrorAction SilentlyContinue).Source }
if (-not $python) { Write-Host "ERROR: no python on PATH" -ForegroundColor Red; exit 1 }
& $python (Join-Path $root "scripts\build.py")
if ($LASTEXITCODE -ne 0) { Write-Host "Build failed." -ForegroundColor Red; exit $LASTEXITCODE }

# 2. Show what changed.
Write-Host ""
Write-Host "[2/4] Changes since last push:" -ForegroundColor Cyan
$changes = git status --short
if (-not $changes) {
  Write-Host "  Nothing changed since last push. Nothing to do." -ForegroundColor Yellow
  exit 0
}
$changes | ForEach-Object { Write-Host "  $_" }

# 3. Commit.
$msg = "chore(site): rebuild and publish"
$argMsg = $args -join " "
if ($argMsg) { $msg = $argMsg }
Write-Host ""
Write-Host "[3/4] Committing..." -ForegroundColor Cyan
Write-Host "  Message: $msg"
git add -A
git commit -m "$msg" | Out-Null
Write-Host "  Commit: $(git rev-parse --short HEAD)"

# 4. Push.
Write-Host ""
Write-Host "[4/4] Pushing to GitHub..." -ForegroundColor Cyan
git push origin main
if ($LASTEXITCODE -ne 0) { Write-Host "Push failed." -ForegroundColor Red; exit $LASTEXITCODE }

# Report deployed URL.
$remote = git remote get-url origin
$urlMatch = [regex]::Match($remote, 'github\.com[:/](?<owner>[^/]+)/(?<repo>[^/.]+)')
if ($urlMatch.Success) {
  $owner = $urlMatch.Groups['owner'].Value
  $repo  = $urlMatch.Groups['repo'].Value
  Write-Host ""
  Write-Host "  Done. Deployment runs in:" -ForegroundColor Green
  Write-Host "    https://github.com/$owner/$repo/actions"
  Write-Host ""
  Write-Host "  Live URL (~60 sec after push completes):" -ForegroundColor Green
  Write-Host "    https://$owner.github.io/$repo/"
}
