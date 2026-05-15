# Copy-Photos.ps1 — copy + resize + rename Mira Palace photos from
#   C:\Claude Projects\Mira Palace\reference\gallery\pictures\Hotel Pictures\
# into
#   C:\Claude Projects\Mira Palace\website\site\assets\img\<section>\
#
# Resizes to max 1920 px wide, JPEG quality 85 (typical ~250-400 KB per image).
# Renames to clean slugs like `deluxe-01.jpg`, `king-12.jpg`, `garden-04.jpg`.
# Self-contained per AWA §10. Idempotent — re-running is safe.

$ErrorActionPreference = "Stop"
$root  = Split-Path -Parent $MyInvocation.MyCommand.Definition
$parent = Split-Path -Parent $root   # C:\Claude Projects\Mira Palace
Set-Location $root

$source = Join-Path $parent "reference\gallery\pictures\Hotel Pictures"
$dest   = Join-Path $root "site\assets\img"

Write-Host ""
Write-Host "Mira Palace - Import Hotel Pictures" -ForegroundColor Cyan
Write-Host "====================================" -ForegroundColor Cyan
Write-Host "  Source: $source"
Write-Host "  Dest:   $dest"

if (-not (Test-Path $source)) {
  Write-Host "  ERROR: source folder not found" -ForegroundColor Red
  exit 1
}

# Folder slug map — keep website paths short and clean.
$slugs = @{
  "standard suite" = "standard"
  "deluxe suite"   = "deluxe"
  "family suite"   = "family"
  "king suite"     = "king"
  "spa"            = "spa"
  "garden"         = "garden"
}

# Pick python
$python = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $python) { $python = (Get-Command python3 -ErrorAction SilentlyContinue).Source }
if (-not $python) { Write-Host "ERROR: no python on PATH" -ForegroundColor Red; exit 1 }

# Ensure Pillow is available
& $python -c "import PIL" 2>$null
if ($LASTEXITCODE -ne 0) {
  Write-Host "  Installing Pillow..." -ForegroundColor Yellow
  & $python -m pip install --quiet Pillow 2>$null
}

$totalIn = 0; $totalOut = 0; $bytesIn = 0L; $bytesOut = 0L

foreach ($folder in $slugs.Keys) {
  $slug = $slugs[$folder]
  $src  = Join-Path $source $folder
  $dst  = Join-Path $dest $slug

  if (-not (Test-Path $src)) {
    Write-Host "  [skip] $folder — not in source" -ForegroundColor Yellow
    continue
  }
  if (-not (Test-Path $dst)) {
    New-Item -ItemType Directory -Path $dst -Force | Out-Null
  }

  $files = Get-ChildItem -Path $src -File |
           Where-Object { $_.Extension -match '\.(jpe?g|png|webp)$' } |
           Sort-Object Name
  if ($files.Count -eq 0) {
    Write-Host "  [skip] $folder — no images" -ForegroundColor Yellow
    continue
  }

  Write-Host ""
  Write-Host "  $folder  ->  $slug\  ($($files.Count) files)" -ForegroundColor Cyan

  $i = 0
  foreach ($f in $files) {
    $i++
    $outName = "{0}-{1:00}.jpg" -f $slug, $i
    $outPath = Join-Path $dst $outName
    $script = @"
import sys
from PIL import Image
import PIL.ImageOps
src, dst = sys.argv[1], sys.argv[2]
img = Image.open(src)
# Honour EXIF orientation so portrait phone shots aren't sideways on the web.
img = PIL.ImageOps.exif_transpose(img)
if img.mode in ('RGBA', 'P', 'LA'):
    img = img.convert('RGB')
# Resize to max 1920 px wide, preserve aspect.
max_w = 1920
if img.width > max_w:
    h = int(img.height * max_w / img.width)
    img = img.resize((max_w, h), Image.LANCZOS)
img.save(dst, 'JPEG', quality=85, optimize=True, progressive=True)
"@
    & $python -c $script $f.FullName $outPath
    if ($LASTEXITCODE -eq 0 -and (Test-Path $outPath)) {
      $totalOut++
      $totalIn++
      $bytesIn  += $f.Length
      $bytesOut += (Get-Item $outPath).Length
      $kbOut = (Get-Item $outPath).Length / 1KB
      Write-Host ("    OK  {0,-30} -> {1,-22}  {2,6:N0} KB" -f $f.Name.Substring(0, [Math]::Min(28, $f.Name.Length)), $outName, $kbOut) -ForegroundColor Green
    } else {
      Write-Host ("    FAIL {0}" -f $f.Name) -ForegroundColor Red
    }
  }
}

Write-Host ""
Write-Host ("  Done. {0} files in ({1:N1} MB) -> {2} files out ({3:N1} MB)" -f $totalIn, ($bytesIn/1MB), $totalOut, ($bytesOut/1MB)) -ForegroundColor Green
Write-Host ""
Write-Host "  Next: run .\Publish-Site.ps1 to rebuild and deploy" -ForegroundColor Green
