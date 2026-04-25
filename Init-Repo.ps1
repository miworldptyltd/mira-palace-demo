# Init-Repo.ps1 — one-shot setup for a new GitHub repo for Mira Palace.
# Self-contained per Agent Working Agreement §10.
#
# What it does:
#   1. Verifies git (and optionally the GitHub CLI `gh`) are installed.
#   2. Removes any broken partial .git folder left by the build sandbox.
#   3. Initialises a fresh git repo on branch `main`.
#   4. Configures your identity.
#   5. Makes the first commit with everything in the project.
#   6. If `gh` is installed and you're authenticated, creates a PUBLIC repo
#      called `mira-palace-demo` under your GitHub account and pushes.
#      Public is required for free GitHub Pages — paid Pro plans can use
#      private repos. The deployed URL is the same either way.
#   7. Turns on GitHub Pages so `https://<you>.github.io/mira-palace-demo/`
#      goes live within ~60 seconds of the push.
#
# USAGE (from anywhere — the script figures out its own path):
#   powershell -ExecutionPolicy Bypass -File "C:\Claude Projects\Mira Palace\Init-Repo.ps1"

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $root

$name  = "Mi World"
$email = "apps@miworld.tech"
$repo  = "mira-palace-demo"

Write-Host "`n[1/7] Prerequisite check..." -ForegroundColor Cyan

try { git --version *>$null }
catch {
  Write-Host "  git is not installed. Install from https://git-scm.com/download/win and re-run." -ForegroundColor Red
  exit 1
}
Write-Host "  git:  $(git --version)"

$hasGh = $false
try { gh --version *>$null; $hasGh = $true; Write-Host "  gh:   $(gh --version | Select-Object -First 1)" }
catch { Write-Host "  gh:   not installed (optional — you'll push manually if missing)" -ForegroundColor Yellow }

Write-Host "`n[2/7] Cleaning any partial .git directory from a previous attempt..." -ForegroundColor Cyan
if (Test-Path ".git") {
  Remove-Item -Path ".git" -Recurse -Force -ErrorAction Stop
  Write-Host "  Removed stale .git"
} else {
  Write-Host "  Nothing to clean."
}

Write-Host "`n[3/7] Initialising git repo on branch 'main'..." -ForegroundColor Cyan
git init -b main | Out-Null
git config user.name  $name
git config user.email $email
Write-Host "  Identity: $name <$email>"

Write-Host "`n[4/7] Staging + first commit + tag v0.1.0..." -ForegroundColor Cyan
git add -A
$staged = git diff --cached --stat | Select-Object -Last 1
Write-Host "  $staged"
git commit -m "release: v0.1.0 — first publishable demo build

- 28 generated pages: home, about, rooms (4), all-inclusive, dining (4),
  pools, spa (2), activities, location, gallery, offers, careers, contact,
  book, three legal pages, 404
- 8 hero videos, 8 ambient music tracks, picker UI with prev/next clusters
- Cross-page music continuity with seek-to-position resume
- 5 colour themes (Mediterranean / Sunset / Olive / Midnight / Onyx)
- Bilingual copyright (EN/TR) switched by nav flag, persisted across pages
- Top-nav dropdowns for Rooms / Dining / Spa with hover-grace behaviour
- HTTP Range support in dev_server.py mirrors GitHub Pages behaviour
- noindex meta + robots.txt Disallow + obscure URL = privacy posture
- LICENSE (proprietary), NOTICE — © Mi World, both legal entities

See CHANGELOG.md for full notes." | Out-Null
Write-Host "  Commit created:  $(git rev-parse --short HEAD)"
git tag -a v0.1.0 -m "v0.1.0 — first publishable demo build for hotel review"
Write-Host "  Tag created:     v0.1.0"

if (-not $hasGh) {
  Write-Host "`n[5/7] Skipping GitHub create/push — `gh` CLI not installed." -ForegroundColor Yellow
  Write-Host ""
  Write-Host "  To finish manually on your GitHub account:" -ForegroundColor Yellow
  Write-Host "    1. Go to https://github.com/new"
  Write-Host "    2. Name:         $repo"
  Write-Host "    3. Visibility:   Public  (required for free GitHub Pages)"
  Write-Host "    4. Do NOT initialise with README / license"
  Write-Host "    5. Then run these three lines in this folder:" -ForegroundColor Yellow
  Write-Host ""
  Write-Host "       git remote add origin https://github.com/<your-username>/$repo.git"
  Write-Host "       git branch -M main"
  Write-Host "       git push -u origin main"
  Write-Host ""
  Write-Host "  Or — install the GitHub CLI from https://cli.github.com/ and re-run me." -ForegroundColor Yellow
  exit 0
}

Write-Host "`n[5/7] Checking gh authentication..." -ForegroundColor Cyan
try { gh auth status *>$null } catch {
  Write-Host "  You are not logged in with `gh`. Run: gh auth login  — then re-run me." -ForegroundColor Red
  exit 1
}
Write-Host "  Authenticated."

Write-Host "`n[6/7] Creating PUBLIC repo + pushing (free Pages requires public)..." -ForegroundColor Cyan
# --public is required for GitHub Pages on free accounts. Paid Pro/Team
# accounts can switch to --private later via:  gh repo edit --visibility private
gh repo create $repo --public --source=. --remote=origin --push --disable-wiki --disable-issues | Out-Null
git push origin --tags 2>$null | Out-Null
Write-Host "  Repo created + pushed (with tags):  $(gh repo view --json url --jq .url)"

Write-Host "`n[7/7] Enabling GitHub Pages..." -ForegroundColor Cyan
# Build source = GitHub Actions (our workflow handles it)
$owner = gh api user --jq .login
gh api --method POST -H "Accept: application/vnd.github+json" "repos/$owner/$repo/pages" -f "source[branch]=main" -f "source[path]=/site" 2>$null | Out-Null
Write-Host "  Pages will build on the next push to main via .github/workflows/deploy.yml."

Write-Host "`n  Done. Preview URL will appear in the Actions tab within ~60 seconds:" -ForegroundColor Green
Write-Host "    https://github.com/$owner/$repo/actions"
Write-Host ""
Write-Host "  And the deployed site will live at:" -ForegroundColor Green
Write-Host "    https://$owner.github.io/$repo/"
Write-Host ""
Write-Host "  Remember: this URL is obscure but technically public. Share it only with the hotel owner." -ForegroundColor Yellow
