# Audit-Clean.ps1 — one-shot pre-release housekeeping for v0.1.0.
# Self-contained per Agent Working Agreement §10. Idempotent — re-running is
# safe; each step checks before it acts.
#
# Removes:
#   - 4 orphan .mp3 files in site/assets/audio that are actually Ogg Vorbis
#     content (the correct .ogg siblings already exist and are referenced).
#   - .preview-pid (local dev-server scratch file).
# Moves:
#   - Mira_Palace_Rapor_TR_v1.{docx,pdf} from repo root into Planning/.
# Reports the new repo size when done.

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $root

Write-Host ""
Write-Host "Mira Palace - Pre-release audit & cleanup" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Orphan .mp3 files (Ogg content with mp3 extension).
$orphans = @(
  "site\assets\audio\track-ambient.mp3",
  "site\assets\audio\track-lounge.mp3",
  "site\assets\audio\track-ocean.mp3",
  "site\assets\audio\track-santur.mp3"
)
Write-Host ""
Write-Host "[1/4] Removing orphan .mp3 files (Ogg content; .ogg siblings already used)..." -ForegroundColor Cyan
foreach ($p in $orphans) {
  if (Test-Path $p) {
    Remove-Item $p -Force
    Write-Host "  removed $p" -ForegroundColor Green
  } else {
    Write-Host "  skip   $p (already gone)" -ForegroundColor DarkGray
  }
}

# 2. Local dev artifact.
Write-Host ""
Write-Host "[2/4] Removing .preview-pid..." -ForegroundColor Cyan
if (Test-Path ".preview-pid") {
  Remove-Item ".preview-pid" -Force
  Write-Host "  removed" -ForegroundColor Green
} else {
  Write-Host "  skip   (already gone)" -ForegroundColor DarkGray
}

# 3. Move Turkish manager report into Planning/.
Write-Host ""
Write-Host "[3/4] Tidying Turkish manager report into Planning/..." -ForegroundColor Cyan
if (-not (Test-Path "Planning")) { New-Item -ItemType Directory -Path "Planning" | Out-Null }
foreach ($name in @("Mira_Palace_Rapor_TR_v1.docx", "Mira_Palace_Rapor_TR_v1.pdf")) {
  if (Test-Path $name) {
    Move-Item -Path $name -Destination (Join-Path "Planning" $name) -Force
    Write-Host "  moved $name -> Planning\" -ForegroundColor Green
  } elseif (Test-Path (Join-Path "Planning" $name)) {
    Write-Host "  skip  $name (already in Planning\)" -ForegroundColor DarkGray
  }
}

# 4. Report sizes.
Write-Host ""
Write-Host "[4/4] Repo size after cleanup..." -ForegroundColor Cyan
$total = (Get-ChildItem -Recurse -Force | Where-Object { -not $_.PSIsContainer -and $_.FullName -notmatch "\\\.git\\" } | Measure-Object Length -Sum).Sum
$audio = (Get-ChildItem "site\assets\audio" -Force -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum
$video = (Get-ChildItem "site\assets\video" -Force -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum
Write-Host ("  audio:  {0,8:N1} MB" -f ($audio/1MB))
Write-Host ("  video:  {0,8:N1} MB" -f ($video/1MB))
Write-Host ("  total:  {0,8:N1} MB" -f ($total/1MB))

Write-Host ""
Write-Host "Done. Run .\Refresh-Media.ps1 to rebuild and verify the site still loads cleanly." -ForegroundColor Green
