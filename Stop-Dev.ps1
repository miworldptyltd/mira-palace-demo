# Stop-Dev.ps1 — shuts down ONLY the preview server we started, by PID.
# Never kills anything else. Per Agent Working Agreement §10.4.

$ErrorActionPreference = "Continue"
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $root

if (-not (Test-Path ".preview-pid")) {
  Write-Host "No .preview-pid file found — nothing to stop (or it was already stopped)." -ForegroundColor Yellow
  exit 0
}

$line = Get-Content ".preview-pid" | Select-Object -First 1
if (-not $line) {
  Remove-Item ".preview-pid" -ErrorAction SilentlyContinue
  Write-Host "Stale .preview-pid was empty — removed." -ForegroundColor Yellow
  exit 0
}

$parts = $line -split ' '
$pid   = $parts[0]
$port  = if ($parts.Count -ge 2) { $parts[1] } else { "?" }

try {
  $proc = Get-Process -Id $pid -ErrorAction SilentlyContinue
  if ($proc) {
    Stop-Process -Id $pid -Force
    Write-Host "Stopped Mira Palace preview server (PID $pid, port $port)." -ForegroundColor Green
  } else {
    Write-Host "PID $pid is not running — nothing to stop." -ForegroundColor Yellow
  }
} catch {
  Write-Host ("Could not stop PID $pid — " + $_.Exception.Message) -ForegroundColor Yellow
}

Remove-Item ".preview-pid" -ErrorAction SilentlyContinue
