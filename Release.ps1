# Release.ps1 — single command for a full Mira Palace release.
#
# What it does, in order:
#   1. Imports any new Mira Palace photos from reference\gallery\pictures\
#      (runs Copy-Photos.ps1 internally; skipped if already imported).
#   2. Rebuilds every HTML page from scratch.
#   3. Generates the next release tag in the form Rxxx (R001, R002, ...).
#   4. Updates VERSION and prepends a release note to CHANGELOG.md.
#   5. Commits everything to git and pushes to GitHub.
#   6. Prints the public URL plus the new release tag so you can tell
#      testers what they're looking at.
#
# Usage:
#   .\Release.ps1 "short description of what changed"
#   .\Release.ps1 "tweak"  -ForcePhotos    # re-imports photos even if present
#
# Self-contained per Agent Working Agreement §10.

param(
  [Parameter(Mandatory=$true, Position=0)]
  [string]$Message,
  [switch]$ForcePhotos
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $root

function Step($t) { Write-Host ""; Write-Host $t -ForegroundColor Cyan; Write-Host ("-" * $t.Length) -ForegroundColor DarkCyan }
function Pass($t) { Write-Host ("  [OK]   " + $t) -ForegroundColor Green }
function Info($t) { Write-Host ("  " + $t) -ForegroundColor DarkGray }
function Warn($t) { Write-Host ("  [warn] " + $t) -ForegroundColor Yellow }
function Fail($t) { Write-Host ("  [FAIL] " + $t) -ForegroundColor Red }

Write-Host ""
Write-Host "Mira Palace - Release" -ForegroundColor Cyan
Write-Host "=====================" -ForegroundColor Cyan
Write-Host "  Message: $Message"

# ---------------------------------------------------------------------------
# Safety: refuse to cut a release if no source files have changed since the
# last R-tag. CHANGELOG.md and VERSION are written BY this script, so they're
# not counted. Prevents accidental empty releases from re-running the script.
#
# Checks THREE places (committed changes + working dir + untracked) so the
# guard catches a release where source has been edited but not yet committed.
$lastTag = git tag -l "R[0-9][0-9][0-9]" 2>$null | Sort-Object -Descending | Select-Object -First 1
if ($lastTag) {
  $diffVsTag   = git diff --name-only $lastTag 2>$null      # tag → working dir (committed + unstaged)
  $stagedDiff  = git diff --name-only --cached 2>$null      # staged-but-uncommitted
  $untracked   = git ls-files --others --exclude-standard 2>$null  # new files not yet in git

  $allChanges = @()
  if ($diffVsTag)  { $allChanges += $diffVsTag }
  if ($stagedDiff) { $allChanges += $stagedDiff }
  if ($untracked)  { $allChanges += $untracked }
  $allChanges = $allChanges | Sort-Object -Unique

  $sourceChanged = $allChanges | Where-Object { $_ -and ($_ -notmatch '^(CHANGELOG\.md|VERSION)$') }
  if (-not $sourceChanged) {
    Write-Host ""
    Write-Host "  [STOP] No source changes since $lastTag." -ForegroundColor Yellow
    Write-Host "  Nothing new to release. Run is aborting before any commits or tags." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "  If you really want to re-deploy the same build (e.g. a force-rebuild)," -ForegroundColor DarkGray
    Write-Host "  delete the last tag first: git tag -d $lastTag" -ForegroundColor DarkGray
    Write-Host ""
    exit 0
  }
}

# ---------------------------------------------------------------------------
# Tidy: remove any stray _*.png test files from site/assets/img/ that may
# have been written during a previous build session. Underscore-prefixed
# files are never legitimate site assets — they're scratchpad output.
$stray = Get-ChildItem -Path "site\assets\img" -Filter "_*.png" -File -ErrorAction SilentlyContinue
if ($stray) {
  foreach ($f in $stray) {
    try { Remove-Item -Path $f.FullName -Force -ErrorAction Stop; Write-Host ("  [tidy] removed " + $f.Name) -ForegroundColor DarkGray }
    catch { Write-Host ("  [tidy] could not remove " + $f.Name) -ForegroundColor Yellow }
  }
}

# Retired pages: pages that used to be generated but have since been removed
# from the build. The build doesn't sweep these — list them here so a stale
# file from a previous build doesn't linger and stay reachable by direct URL.
$retiredPages = @("site\pools-beach.html", "site\assets\_spa_menu_source.pdf")
foreach ($p in $retiredPages) {
  if (Test-Path $p) {
    try { Remove-Item -Path $p -Force -ErrorAction Stop; Write-Host ("  [tidy] retired page removed: " + $p) -ForegroundColor DarkGray }
    catch { Write-Host ("  [tidy] could not remove retired page: " + $p) -ForegroundColor Yellow }
  }
}

# ---------------------------------------------------------------------------
Step "[1/7]  Photo import"

# Sentinel file we check for to decide whether photos have already been imported.
$sentinel = "site\assets\img\king\king-01.jpg"
$copyScript = Join-Path $root "Copy-Photos.ps1"

if ($ForcePhotos -or -not (Test-Path $sentinel)) {
  if (-not (Test-Path $copyScript)) {
    Fail "Copy-Photos.ps1 not found — cannot import photos"
    exit 1
  }
  Info "Running Copy-Photos.ps1 to import / refresh hotel photography..."
  & $copyScript
  if ($LASTEXITCODE -ne 0) {
    Fail "Photo import failed"
    exit 1
  }
  Pass "Photos imported"
} else {
  Info "Photos already present (use -ForcePhotos to re-import)"
}

# ---------------------------------------------------------------------------
Step "[2/7]  Compile Tailwind CSS  (R020 — was v3 Play CDN, now proper build)"

$twBin = Join-Path $root "tools\tailwindcss.exe"
if (-not (Test-Path $twBin)) {
  Info "Tailwind CLI not found — running Bootstrap-Tailwind.ps1 first ..."
  $bootstrap = Join-Path $root "Bootstrap-Tailwind.ps1"
  if (-not (Test-Path $bootstrap)) { Fail "Bootstrap-Tailwind.ps1 missing"; exit 1 }
  & $bootstrap
  if ($LASTEXITCODE -ne 0) { Fail "Tailwind bootstrap failed"; exit 1 }
}

$twIn  = Join-Path $root "scripts\tailwind\input.css"
$twOut = Join-Path $root "site\assets\css\site.css"
Info "Compiling $twIn -> site.css (minified)"
& $twBin -i $twIn -o $twOut --minify
if ($LASTEXITCODE -ne 0) { Fail "Tailwind CSS compile failed"; exit 1 }

$outSize = (Get-Item $twOut).Length
Pass ("site.css produced — {0:N0} bytes minified" -f $outSize)

# ---------------------------------------------------------------------------
Step "[3/7]  Rebuild every HTML page"

$python = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $python) { $python = (Get-Command python3 -ErrorAction SilentlyContinue).Source }
if (-not $python) { Fail "no python on PATH"; exit 1 }

& $python (Join-Path $root "scripts\build.py")
if ($LASTEXITCODE -ne 0) { Fail "Build failed"; exit 1 }
Pass "All HTML pages generated"

# ---------------------------------------------------------------------------
Step "[4/7]  Generate next release tag (Rxxx)"

# Sanity: must be inside a git repo
if (-not (Test-Path ".git")) { Fail "no .git folder — run Init-Repo.ps1 first"; exit 1 }

# Find the highest existing Rxxx tag (defaults to 0 if none exist).
$highest = 0
$tags = git tag -l "R[0-9][0-9][0-9]" 2>$null
if ($tags) {
  foreach ($t in $tags) {
    if ($t -match "^R(\d{3})$") {
      $n = [int]$Matches[1]
      if ($n -gt $highest) { $highest = $n }
    }
  }
}
# If we've never tagged with Rxxx but v0.1.0 is already pushed, treat
# v0.1.0 as R001 so this release becomes R002.
if ($highest -eq 0) {
  $sem = git tag -l "v0.1.0" 2>$null
  if ($sem) { $highest = 1 ; Info "(treating existing v0.1.0 tag as R001)" }
}
$nextNum = $highest + 1
$release = "R{0:000}" -f $nextNum
Pass "Next release: $release"

# ---------------------------------------------------------------------------
Step "[5/7]  Update VERSION and CHANGELOG.md"

$today = Get-Date -Format "yyyy-MM-dd"

# VERSION (overwrite)
Set-Content -Path "VERSION" -Value $release -NoNewline
Pass "VERSION  -> $release"

# CHANGELOG.md (prepend a new entry under the title line)
$changelogPath = "CHANGELOG.md"
$entry = @"
## [$release] - $today

$Message
"@
if (Test-Path $changelogPath) {
  $old = Get-Content $changelogPath -Raw
  # Insert new entry after the first '# Changelog' line + blank line block
  if ($old -match "(?ms)^(# Changelog.*?\n\n)(.*)$") {
    $head = $Matches[1]
    $body = $Matches[2]
    Set-Content -Path $changelogPath -Value ($head + $entry + "`n`n" + $body)
  } else {
    # Fallback: prepend to whole file
    Set-Content -Path $changelogPath -Value ($entry + "`n`n" + $old)
  }
  Pass "CHANGELOG.md updated"
} else {
  $title = "# Changelog`n`nAll notable changes to the Mira Palace website are listed here, newest first.`n`n"
  Set-Content -Path $changelogPath -Value ($title + $entry + "`n")
  Pass "CHANGELOG.md created"
}

# ---------------------------------------------------------------------------
Step "[6/7]  Commit and tag"

git add -A | Out-Null
$staged = git diff --cached --stat | Select-Object -Last 1
Info "  $staged"

# Build commit body
$body = @"
$release - $Message

Mira Palace website release $release.
See CHANGELOG.md for the full notes.
"@
git commit -m $body | Out-Null
if ($LASTEXITCODE -ne 0) {
  Warn "Nothing to commit (no changes since last release)."
} else {
  Pass "Commit:  $(git rev-parse --short HEAD)"
}

git tag -a $release -m "$release - $Message" 2>$null | Out-Null
Pass "Tag:     $release"

# ---------------------------------------------------------------------------
Step "[7/7]  Push to GitHub"

git push origin main 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) { Fail "git push origin main failed"; exit 1 }
git push origin --tags 2>&1 | Out-Null
Pass "Pushed main + tags to GitHub"

# ---------------------------------------------------------------------------
Step "Done"

$remote = git remote get-url origin
$urlMatch = [regex]::Match($remote, 'github\.com[:/](?<owner>[^/]+)/(?<repo>[^/.]+)')
if ($urlMatch.Success) {
  $owner = $urlMatch.Groups['owner'].Value
  $repo  = $urlMatch.Groups['repo'].Value
  Write-Host ""
  Write-Host "  Release:  $release" -ForegroundColor Green
  Write-Host "  Tag:      https://github.com/$owner/$repo/releases/tag/$release" -ForegroundColor Green
  Write-Host "  Pipeline: https://github.com/$owner/$repo/actions" -ForegroundColor Green
  Write-Host "  Live URL: https://$owner.github.io/$repo/" -ForegroundColor Green
  Write-Host ""
  Write-Host "  GitHub Actions will rebuild and publish the site within ~60 seconds." -ForegroundColor Yellow
  Write-Host "  Tell testers to refresh the live URL." -ForegroundColor Yellow
}
