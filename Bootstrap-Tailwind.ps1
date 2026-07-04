# Bootstrap-Tailwind.ps1 — download the Tailwind v4 standalone CLI on demand.
#
# Why this script exists (R020):
#   From R020 the site is built with a real Tailwind step instead of the
#   old Play CDN. Tailwind v4 ships a single-file executable — no Node,
#   no npm. We just curl it once, cache it under tools/, and Release.ps1
#   invokes it on every build.
#
# Idempotent: if tools\tailwindcss.exe already exists AND is executable,
# this script exits successfully without re-downloading.
#
# Usage:
#   .\Bootstrap-Tailwind.ps1              # download if missing
#   .\Bootstrap-Tailwind.ps1 -Force       # force re-download (e.g. version bump)
#   .\Bootstrap-Tailwind.ps1 -Version 4.3.2   # pin to a specific release

param(
  [switch]$Force,
  [string]$Version = "4.3.2"   # bump when Tailwind releases a new stable
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $root

$toolsDir = Join-Path $root "tools"
$binPath  = Join-Path $toolsDir "tailwindcss.exe"

# Detect architecture — arm64 (Surface Pro X etc.) needs a different binary
$arch = if ([System.Environment]::Is64BitOperatingSystem) {
  if ($env:PROCESSOR_ARCHITECTURE -match "ARM64" -or $env:PROCESSOR_ARCHITEW6432 -match "ARM64") { "arm64" }
  else { "x64" }
} else { "x64" }

$assetName = "tailwindcss-windows-$arch.exe"
$url       = "https://github.com/tailwindlabs/tailwindcss/releases/download/v$Version/$assetName"

Write-Host ""
Write-Host "Tailwind CLI bootstrap" -ForegroundColor Cyan
Write-Host "======================" -ForegroundColor Cyan
Write-Host "  Target : $binPath"
Write-Host "  Version: $Version ($arch)"
Write-Host ""

# Skip download if already present and not forced
if ((Test-Path $binPath) -and -not $Force) {
  # Check the cached binary reports the expected version
  try {
    $reported = (& $binPath --help 2>&1 | Select-String -Pattern "tailwindcss v" | Select-Object -First 1).Line
    if ($reported -match "v$Version") {
      Write-Host "  [OK]   Cached binary matches v$Version — nothing to do." -ForegroundColor Green
      exit 0
    } else {
      Write-Host "  [warn] Cached binary reports: $reported (wanted v$Version) — refreshing." -ForegroundColor Yellow
    }
  } catch {
    Write-Host "  [warn] Cached binary unusable — refreshing." -ForegroundColor Yellow
  }
}

if (-not (Test-Path $toolsDir)) {
  New-Item -ItemType Directory -Path $toolsDir | Out-Null
  Write-Host "  [OK]   Created tools/" -ForegroundColor Green
}

Write-Host "  Downloading $assetName ..."
try {
  # -UseBasicParsing keeps it working on machines without full IE COM
  Invoke-WebRequest -Uri $url -OutFile $binPath -UseBasicParsing
} catch {
  Write-Host "  [FAIL] Download failed: $_" -ForegroundColor Red
  Write-Host "  URL:   $url" -ForegroundColor DarkGray
  Write-Host "  If your network blocks GitHub releases, ask your admin to allow" -ForegroundColor DarkGray
  Write-Host "  github.com and objects.githubusercontent.com." -ForegroundColor DarkGray
  exit 1
}

$size = (Get-Item $binPath).Length
Write-Host ("  [OK]   Downloaded {0:N0} bytes" -f $size) -ForegroundColor Green

# Sanity-check the binary
try {
  $reported = (& $binPath --help 2>&1 | Select-String -Pattern "tailwindcss v" | Select-Object -First 1).Line
  Write-Host "  [OK]   Binary reports: $reported" -ForegroundColor Green
} catch {
  Write-Host "  [FAIL] Downloaded binary won't run: $_" -ForegroundColor Red
  exit 1
}

Write-Host ""
Write-Host "  Tailwind CLI is ready at:" -ForegroundColor Green
Write-Host "    $binPath" -ForegroundColor Green
Write-Host ""
