# Restart-Dev.ps1 — stop the running preview server (if any), rebuild the
# site, and start a fresh server. One self-contained call.
# Per Agent Working Agreement §10.

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $root

Write-Host ""
Write-Host "Mira Palace - Restart preview" -ForegroundColor Cyan
Write-Host "==============================" -ForegroundColor Cyan

# Stop any previous PID we recorded.
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

# Now run the full Run-Dev pipeline in this same window.
& (Join-Path $root "Run-Dev.ps1")
