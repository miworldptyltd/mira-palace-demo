# Fix-Pages.ps1 — switch GitHub Pages source from "branch" to "GitHub Actions"
# and re-trigger the deploy workflow. Self-contained per AWA §10.
#
# Why this exists: Init-Repo.ps1 set Pages to deploy-from-branch by default,
# but our workflow uses the modern actions/deploy-pages model. This script
# reconciles the two. Safe to re-run.

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $root

Write-Host ""
Write-Host "Mira Palace - Fix GitHub Pages source" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan

# Sanity: must be in a git repo, gh must be installed and authenticated.
if (-not (Test-Path ".git")) {
  Write-Host "  No .git folder. Run Init-Repo.ps1 first." -ForegroundColor Red
  exit 1
}
try { gh auth status *>$null }
catch {
  Write-Host "  Not logged in. Run: gh auth login" -ForegroundColor Red
  exit 1
}

$owner = gh api user --jq .login
$remote = git remote get-url origin
$repoMatch = [regex]::Match($remote, 'github\.com[:/](?<owner>[^/]+)/(?<repo>[^/.]+)')
$repo = $repoMatch.Groups['repo'].Value
Write-Host "  Repo: $owner/$repo"

# 1. Update Pages config to use GitHub Actions as the build source.
Write-Host ""
Write-Host "[1/3] Setting Pages source to 'GitHub Actions'..." -ForegroundColor Cyan
try {
  # PUT updates an existing Pages site; -f sets a form field.
  gh api --method PUT -H "Accept: application/vnd.github+json" "repos/$owner/$repo/pages" -f "build_type=workflow" 2>&1 | Out-Null
  Write-Host "  Updated to build_type=workflow." -ForegroundColor Green
} catch {
  # If PUT fails (Pages not yet created), POST to create it.
  Write-Host "  PUT failed, trying POST to create Pages with workflow source..." -ForegroundColor Yellow
  gh api --method POST -H "Accept: application/vnd.github+json" "repos/$owner/$repo/pages" -f "build_type=workflow" 2>&1 | Out-Null
  Write-Host "  Created with build_type=workflow." -ForegroundColor Green
}

# 2. Trigger the deploy workflow manually so we don't have to wait for the
#    next push.
Write-Host ""
Write-Host "[2/3] Triggering deploy workflow..." -ForegroundColor Cyan
gh workflow run deploy.yml --repo "$owner/$repo" 2>&1 | Out-Null
Write-Host "  Workflow run dispatched." -ForegroundColor Green

# 3. Give the user the URLs.
Write-Host ""
Write-Host "[3/3] URLs to watch:" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Workflow progress (refresh after ~30 sec):" -ForegroundColor Green
Write-Host "    https://github.com/$owner/$repo/actions"
Write-Host ""
Write-Host "  Pages settings (where 'GitHub Actions' is now the source):" -ForegroundColor Green
Write-Host "    https://github.com/$owner/$repo/settings/pages"
Write-Host ""
Write-Host "  Live site (~60-90 sec after the workflow turns green):" -ForegroundColor Green
Write-Host "    https://$owner.github.io/$repo/"
Write-Host ""
Write-Host "  Tip: open the live URL in an incognito/private window so you see" -ForegroundColor Yellow
Write-Host "  what a fresh visitor sees (no cached state)." -ForegroundColor Yellow
