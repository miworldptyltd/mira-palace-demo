# Resize-PDF.ps1 — scale a PDF from A4 to A5 (or any size).
# Self-contained per AWA §10. Uses Python's pypdf (no GS / qpdf needed).
#
# Usage:
#   .\Resize-PDF.ps1 "C:\path\to\input.pdf"
#   .\Resize-PDF.ps1 "C:\path\to\input.pdf" -OutputPath "C:\path\out.pdf"
#   .\Resize-PDF.ps1 "C:\path\to\input.pdf" -Target A4    # scale up
#   .\Resize-PDF.ps1 "C:\path\to\input.pdf" -Target A6    # smaller

param(
  [Parameter(Mandatory=$true, Position=0)] [string]$InputPath,
  [string]$OutputPath = "",
  [ValidateSet("A3","A4","A5","A6")] [string]$Target = "A5"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $InputPath)) {
  Write-Host "ERROR: Input file not found: $InputPath" -ForegroundColor Red
  exit 1
}

# Target paper sizes in DIN-A points (1mm = 72/25.4 pt).
$sizes = @{
  "A3" = @(842, 1191)
  "A4" = @(595, 842)
  "A5" = @(420, 595)
  "A6" = @(298, 420)
}
$tw, $th = $sizes[$Target]

if (-not $OutputPath) {
  $dir = Split-Path $InputPath -Parent
  $base = [System.IO.Path]::GetFileNameWithoutExtension($InputPath)
  $OutputPath = Join-Path $dir ($base + "-$Target.pdf")
}

Write-Host ""
Write-Host "Resize PDF -> $Target" -ForegroundColor Cyan
Write-Host "  in : $InputPath"
Write-Host "  out: $OutputPath"

# Find python
$python = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $python) { $python = (Get-Command python3 -ErrorAction SilentlyContinue).Source }
if (-not $python) { Write-Host "ERROR: no python on PATH" -ForegroundColor Red; exit 1 }

# Ensure pypdf is available
& $python -c "import pypdf" 2>$null
if ($LASTEXITCODE -ne 0) {
  Write-Host "  Installing pypdf..." -ForegroundColor Yellow
  & $python -m pip install --quiet pypdf 2>$null
}

# Resize via a one-shot Python invocation
$script = @"
import sys
from pypdf import PdfReader, PdfWriter, Transformation
src, dst, tw, th = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
r = PdfReader(src)
w = PdfWriter()
for page in r.pages:
    pw = float(page.mediabox.width)
    ph = float(page.mediabox.height)
    # Match orientation: if source is landscape, target lands landscape
    if pw > ph:
        target_w, target_h = max(tw, th), min(tw, th)
    else:
        target_w, target_h = min(tw, th), max(tw, th)
    sx = target_w / pw
    sy = target_h / ph
    s = min(sx, sy)  # preserve aspect (no distortion)
    page.add_transformation(Transformation().scale(sx=s, sy=s))
    # Centre on the target page
    new_w = pw * s
    new_h = ph * s
    page.add_transformation(Transformation().translate(tx=(target_w-new_w)/2, ty=(target_h-new_h)/2))
    page.mediabox.lower_left  = (0, 0)
    page.mediabox.upper_right = (target_w, target_h)
    page.cropbox = page.mediabox
    w.add_page(page)
with open(dst, 'wb') as f:
    w.write(f)
print(f'pages: {len(r.pages)}')
"@

& $python -c $script $InputPath $OutputPath $tw $th
if ($LASTEXITCODE -eq 0) {
  $sz = (Get-Item $OutputPath).Length / 1KB
  Write-Host ("  OK  {0:N1} KB" -f $sz) -ForegroundColor Green
} else {
  Write-Host "  Failed." -ForegroundColor Red
}
