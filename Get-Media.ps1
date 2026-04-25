# Get-Media.ps1 — download placeholder hero videos and ambient music tracks
# into site/assets/video/ and site/assets/audio/.
#
# Re-runs are safe: existing files are skipped UNLESS they are over the size
# cap (means we accidentally pulled a UHD copy on a previous run).
# Self-contained per Agent Working Agreement §10.

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $root

Write-Host ""
Write-Host "Mira Palace - placeholder media downloader" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan

$videoDir = Join-Path $root "site\assets\video"
$audioDir = Join-Path $root "site\assets\audio"
New-Item -ItemType Directory -Force -Path $videoDir | Out-Null
New-Item -ItemType Directory -Force -Path $audioDir | Out-Null

# Cap individual video files at 30 MB so the hero starts playing fast.
$videoSizeCap = 30MB
$audioSizeCap = 20MB

# Each entry: target path, size cap, list of URLs to try (first that works wins).
$assets = @(
  # ---- VIDEOS (HD only — UHD is too big to start playing) -----------------
  @{ Path = (Join-Path $videoDir "hero-pool.mp4"); Cap = $videoSizeCap;
     Urls = @(
       "https://videos.pexels.com/video-files/2169880/2169880-hd_1280_720_30fps.mp4",
       "https://videos.pexels.com/video-files/2169880/2169880-hd_1920_1080_30fps.mp4",
       "https://assets.mixkit.co/videos/2738/2738-720.mp4"
     ) },
  @{ Path = (Join-Path $videoDir "hero-coast.mp4"); Cap = $videoSizeCap; ForceRedo = $true;
     Urls = @(
       "https://videos.pexels.com/video-files/1437396/1437396-hd_1920_1080_24fps.mp4",
       "https://videos.pexels.com/video-files/1093662/1093662-hd_1920_1080_30fps.mp4",
       "https://videos.pexels.com/video-files/2169307/2169307-hd_1920_1080_30fps.mp4",
       "https://assets.mixkit.co/videos/4148/4148-720.mp4"
     ) },
  @{ Path = (Join-Path $videoDir "hero-sunset.mp4"); Cap = $videoSizeCap; ForceRedo = $true;
     Urls = @(
       "https://videos.pexels.com/video-files/2169305/2169305-hd_1920_1080_30fps.mp4",
       "https://videos.pexels.com/video-files/2491284/2491284-hd_1920_1080_24fps.mp4",
       "https://videos.pexels.com/video-files/3018669/3018669-hd_1920_1080_25fps.mp4"
     ) },
  @{ Path = (Join-Path $videoDir "hero-aerial.mp4"); Cap = $videoSizeCap;
     Urls = @(
       "https://videos.pexels.com/video-files/2169879/2169879-hd_1920_1080_30fps.mp4",
       "https://videos.pexels.com/video-files/2491284/2491284-hd_1920_1080_24fps.mp4",
       "https://videos.pexels.com/video-files/3018669/3018669-hd_1920_1080_25fps.mp4",
       "https://videos.pexels.com/video-files/2169882/2169882-hd_1920_1080_30fps.mp4"
     ) },
  @{ Path = (Join-Path $videoDir "hero-waves.mp4"); Cap = $videoSizeCap;
     Urls = @(
       "https://videos.pexels.com/video-files/856256/856256-hd_1920_1080_30fps.mp4",
       "https://videos.pexels.com/video-files/1721294/1721294-hd_1920_1080_30fps.mp4",
       "https://videos.pexels.com/video-files/1093662/1093662-hd_1920_1080_30fps.mp4"
     ) },
  @{ Path = (Join-Path $videoDir "hero-lobby.mp4"); Cap = $videoSizeCap;
     Urls = @(
       "https://videos.pexels.com/video-files/3015529/3015529-hd_1920_1080_24fps.mp4",
       "https://videos.pexels.com/video-files/2034115/2034115-hd_1920_1080_30fps.mp4",
       "https://videos.pexels.com/video-files/4763824/4763824-hd_1920_1080_25fps.mp4"
     ) },
  @{ Path = (Join-Path $videoDir "hero-spa.mp4"); Cap = $videoSizeCap;
     Urls = @(
       "https://videos.pexels.com/video-files/4994378/4994378-hd_1920_1080_25fps.mp4",
       "https://videos.pexels.com/video-files/4046389/4046389-hd_1920_1080_30fps.mp4",
       "https://videos.pexels.com/video-files/3209076/3209076-hd_1920_1080_25fps.mp4"
     ) },
  # ---- AUDIO (multiple CDNs to dodge whichever blocks today) -------------
  @{ Path = (Join-Path $audioDir "track-piano.mp3"); Cap = $audioSizeCap; ForceRedo = $true;
     Urls = @(
       "https://commondatastorage.googleapis.com/codeskulptor-demos/riceracer_assets/music/lose.ogg",
       "https://commondatastorage.googleapis.com/codeskulptor-demos/riceracer_assets/music/intro.ogg",
       "https://commondatastorage.googleapis.com/codeskulptor-demos/asteroidwarrior_assets/sound/explode.ogg"
     ) },
  @{ Path = (Join-Path $audioDir "track-ambient.mp3"); Cap = $audioSizeCap;
     Urls = @(
       "https://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg",
       "https://www.bensound.com/bensound-music/bensound-slowmotion.mp3",
       "https://file-examples.com/storage/fef5050b88706b3b3306f0d/2017/11/file_example_MP3_1MG.mp3"
     ) },
  @{ Path = (Join-Path $audioDir "track-santur.mp3"); Cap = $audioSizeCap;
     Urls = @(
       "https://www.bensound.com/bensound-music/bensound-india.mp3",
       "https://commondatastorage.googleapis.com/codeskulptor-demos/riceracer_assets/music/win.ogg",
       "https://file-examples.com/storage/fef5050b88706b3b3306f0d/2017/11/file_example_MP3_2MG.mp3"
     ) },
  @{ Path = (Join-Path $audioDir "track-ocean.mp3"); Cap = $audioSizeCap;
     Urls = @(
       "https://commondatastorage.googleapis.com/codeskulptor-demos/pyman_assets/intromusic.ogg",
       "https://commondatastorage.googleapis.com/codeskulptor-demos/riceracer_assets/music/menu.ogg",
       "https://www.bensound.com/bensound-music/bensound-relaxing.mp3"
     ) },
  @{ Path = (Join-Path $audioDir "track-zen.mp3"); Cap = $audioSizeCap; ForceRedo = $true;
     Urls = @(
       "https://commondatastorage.googleapis.com/codeskulptor-demos/pyman_assets/song.ogg",
       "https://commondatastorage.googleapis.com/codeskulptor-demos/pyman_assets/eatpill.ogg",
       "https://commondatastorage.googleapis.com/codeskulptor-demos/riceracer_assets/music/race.ogg"
     ) },
  @{ Path = (Join-Path $audioDir "track-spa.mp3"); Cap = $audioSizeCap; ForceRedo = $true;
     Urls = @(
       "https://commondatastorage.googleapis.com/codeskulptor-demos/pyman_assets/playerdeath.ogg",
       "https://commondatastorage.googleapis.com/codeskulptor-demos/asteroidwarrior_assets/sound/firstshot.ogg",
       "https://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3"
     ) },
  @{ Path = (Join-Path $audioDir "track-lounge.mp3"); Cap = $audioSizeCap;
     Urls = @(
       "https://upload.wikimedia.org/wikipedia/commons/c/cb/Aretha_Franklin_-_Respect.ogg",
       "https://upload.wikimedia.org/wikipedia/commons/4/4f/Tchaikovsky_-_Swan_Lake_-_Scene_(end).ogg",
       "https://commondatastorage.googleapis.com/codeskulptor-demos/riceracer_assets/music/menu.ogg"
     ) }
)

$ok = 0; $fail = 0
foreach ($a in $assets) {
  $name = Split-Path $a.Path -Leaf
  if (Test-Path $a.Path) {
    $existing = (Get-Item $a.Path).Length
    $forceRedo = $false; if ($a.ContainsKey('ForceRedo')) { $forceRedo = $a.ForceRedo }
    if ($forceRedo) {
      Write-Host "  [redo] $name forced redo (e.g. wrong content from previous URL)" -ForegroundColor Yellow
      Remove-Item $a.Path -Force -ErrorAction SilentlyContinue
    } elseif ($existing -gt $a.Cap) {
      Write-Host "  [redo] $name is $([math]::Round($existing/1MB,1)) MB (over $([math]::Round($a.Cap/1MB,0)) MB cap) - re-downloading smaller version" -ForegroundColor Yellow
      Remove-Item $a.Path -Force -ErrorAction SilentlyContinue
    } elseif ($existing -gt 100000) {
      Write-Host "  [skip] $name already exists ($([math]::Round($existing/1MB,1)) MB)" -ForegroundColor DarkGray
      $ok++; continue
    }
  }
  $got = $false
  foreach ($u in $a.Urls) {
    Write-Host "  [..]   $name  <- $u"
    try {
      $ua = "MiraPalaceDemo/1.0 (apps@miworld.tech)"
      Invoke-WebRequest -Uri $u -OutFile $a.Path -UseBasicParsing -TimeoutSec 90 -UserAgent $ua -ErrorAction Stop
      $size = (Get-Item $a.Path).Length
      if ($size -lt 50000) { Remove-Item $a.Path -ErrorAction SilentlyContinue; throw "file too small ($size bytes)" }
      Write-Host "  [ok]   $name  ($([math]::Round($size/1MB,1)) MB)" -ForegroundColor Green
      $got = $true; break
    } catch {
      Write-Host "  [fail] $($_.Exception.Message)" -ForegroundColor DarkYellow
    }
    # Be polite to rate-limited hosts (Wikimedia returns 429 quickly otherwise)
    if ($u -match "wikimedia\.org") { Start-Sleep -Seconds 3 }
  }
  if ($got) { $ok++ } else { $fail++; Write-Host "  [skip] $name unavailable - that option will fall back gracefully" -ForegroundColor Red }
}

Write-Host ""
$summaryColor = if ($fail -eq 0) { "Green" } else { "Yellow" }
Write-Host "Done. $ok ok, $fail failed." -ForegroundColor $summaryColor
Write-Host ""
Write-Host "Next: run Restart-Dev.ps1 to rebuild and preview." -ForegroundColor Cyan
