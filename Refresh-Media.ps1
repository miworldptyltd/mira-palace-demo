# Refresh-Media.ps1 — rescan site\assets\video and site\assets\audio,
# regenerate the media manifest + every page, restart the preview server.
# Self-contained per Agent Working Agreement §10. Politely stops only the PID
# we recorded ourselves; never kills random processes on the port.

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $root

Write-Host ""
Write-Host "Mira Palace - Refresh media (rescan assets)" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan

# 1. Stop the previous server (if we have a recorded PID).
if (Test-Path ".preview-pid") {
  $line = Get-Content ".preview-pid" | Select-Object -First 1
  if ($line) {
    $oldPid = ($line -split ' ')[0]
    try {
      $proc = Get-Process -Id $oldPid -ErrorAction SilentlyContinue
      if ($proc) {
        Stop-Process -Id $oldPid -Force
        Write-Host "  Stopped previous server (PID $oldPid)." -ForegroundColor Yellow
      }
    } catch {}
  }
  Remove-Item ".preview-pid" -ErrorAction SilentlyContinue
}

# 2. List the files actually on disk so the build's discovery is auditable.
Write-Host ""
Write-Host "Files in site\assets\video:" -ForegroundColor Cyan
Get-ChildItem -Path (Join-Path $root "site\assets\video") -File -ErrorAction SilentlyContinue |
  ForEach-Object { "  {0,-30} {1,8:N1} MB" -f $_.Name, ($_.Length/1MB) } | ForEach-Object { Write-Host $_ }

Write-Host ""
Write-Host "Files in site\assets\audio:" -ForegroundColor Cyan
Get-ChildItem -Path (Join-Path $root "site\assets\audio") -File -ErrorAction SilentlyContinue |
  ForEach-Object { "  {0,-30} {1,8:N1} MB" -f $_.Name, ($_.Length/1MB) } | ForEach-Object { Write-Host $_ }

# 3. Run the build (regenerates every HTML page AND writes media-manifest.js).
Write-Host ""
Write-Host "Running build..." -ForegroundColor Cyan
$python = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $python) { $python = (Get-Command python3 -ErrorAction SilentlyContinue).Source }
if (-not $python) { Write-Host "ERROR: no python on PATH" -ForegroundColor Red; exit 1 }
& $python (Join-Path $root "scripts\build.py")
if ($LASTEXITCODE -ne 0) { Write-Host "Build failed." -ForegroundColor Red; exit $LASTEXITCODE }

# 4. Show the head of the generated manifest so the user can SEE what was wired up.
$manifest = Join-Path $root "site\assets\js\media-manifest.js"
if (Test-Path $manifest) {
  Write-Host ""
  Write-Host "Generated media-manifest.js:" -ForegroundColor Cyan
  Get-Content $manifest | ForEach-Object { Write-Host "  $_" -ForegroundColor DarkGray }
} else {
  Write-Host "WARN: media-manifest.js was not written - the customise picker will fall back to 'none' only." -ForegroundColor Yellow
}

# 5. Start a fresh preview server.
Write-Host ""
Write-Host "Starting preview server..." -ForegroundColor Cyan
& (Join-Path $root "Run-Dev.ps1")
