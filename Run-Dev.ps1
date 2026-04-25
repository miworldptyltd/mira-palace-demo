# Run-Dev.ps1 — local preview for Mira Palace.
# Self-contained per Agent Working Agreement §10. Port-polite: probes for a
# free port instead of killing whatever is running.

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $root

Write-Host ""
Write-Host "Mira Palace — local preview" -ForegroundColor Cyan
Write-Host "============================" -ForegroundColor Cyan

# --- [1/5] Prerequisites -----------------------------------------------------
Write-Host ""
Write-Host "[1/5] Prerequisites" -ForegroundColor Cyan

$py = $null
foreach ($c in @("py", "python", "python3")) {
  try { & $c --version *>$null; if ($LASTEXITCODE -eq 0) { $py = $c; break } } catch {}
}
if (-not $py) {
  Write-Host "  Python is not on PATH. Install Python 3.10+ from python.org and re-run." -ForegroundColor Red
  exit 1
}
Write-Host ("  Python: " + (& $py --version))

# --- [2/5] Pick a free port (do NOT kill anything) --------------------------
Write-Host ""
Write-Host "[2/5] Picking a free port" -ForegroundColor Cyan

function Test-PortFree([int]$p) {
  $tcp = Get-NetTCPConnection -LocalPort $p -State Listen -ErrorAction SilentlyContinue
  return ($null -eq $tcp -or $tcp.Count -eq 0)
}

$candidates = @(8765, 8766, 8767, 4321, 5173, 8088, 8888)
$port = $null
foreach ($p in $candidates) {
  if (Test-PortFree $p) { $port = $p; break }
}
if (-not $port) {
  Write-Host "  All preferred ports are taken. Edit this script and add another to the candidates list." -ForegroundColor Red
  exit 1
}
Write-Host "  Using port: $port"

# --- [3/5] Build site --------------------------------------------------------
Write-Host ""
Write-Host "[3/5] Rebuilding site" -ForegroundColor Cyan
& $py "scripts/build.py"
if ($LASTEXITCODE -ne 0) { Write-Host "Build failed. Stopping." -ForegroundColor Red; exit 1 }

# --- [4/5] Start the preview server in the background ----------------------
Write-Host ""
Write-Host "[4/5] Starting preview server on http://localhost:$port (no-cache mode)" -ForegroundColor Cyan
$server = Start-Process -FilePath $py -ArgumentList @("scripts/dev_server.py", $port) -PassThru -WindowStyle Hidden
"$($server.Id) $port" | Out-File -FilePath ".preview-pid" -Encoding ascii
Start-Sleep -Seconds 2

# --- [5/5] Content-level health check (per §10.5) --------------------------
Write-Host ""
Write-Host "[5/5] Health check" -ForegroundColor Cyan
$ok = $false
try {
  $res = Invoke-WebRequest -Uri "http://localhost:$port/index.html" -UseBasicParsing -TimeoutSec 5
  if ($res.StatusCode -eq 200 -and $res.Content -match "Mira Palace") { $ok = $true }
} catch {}

if ($ok) {
  Write-Host "  OK — home page responded with 'Mira Palace' content." -ForegroundColor Green
} else {
  Write-Host "  WARNING — server didn't respond as expected. Try the URL anyway." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "============================" -ForegroundColor Green
Write-Host "  Preview:   http://localhost:$port/" -ForegroundColor Green
Write-Host "  PID file:  .preview-pid (used by Stop-Dev.ps1)" -ForegroundColor Green
Write-Host "  Stop with: powershell -ExecutionPolicy Bypass -File '.\Stop-Dev.ps1'" -ForegroundColor Green
Write-Host "============================" -ForegroundColor Green
Write-Host ""

# Open the browser for them
Start-Process "http://localhost:$port/"

Write-Host "Server is running in the background. This window can stay open or be closed." -ForegroundColor Cyan
Write-Host "When you're done previewing, run Stop-Dev.ps1 to shut it down cleanly." -ForegroundColor Cyan
