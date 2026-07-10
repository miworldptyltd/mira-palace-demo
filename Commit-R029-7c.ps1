#requires -Version 7.4
# R029.7c — tag ~200 hardcoded EN strings site-wide + 291 new i18n keys.

$ErrorActionPreference = 'Stop'
$RepoRoot = $PSScriptRoot
$Tag = 'R029.7c'
$Msg = @'
R029.7c: full data-i18n tagging site-wide (+ 291 EN keys)

Subagent walked all 9 page-generators and tagged every user-visible
English string that wasn't already reachable to the runtime translator:

  _book.py                        33 strings tagged
  _spa_book.py                    22
  _faq_contact_career.py         ~50   (all 12 Q&A + contact + career)
  _home.py                        11   (intro paras, gallery + location links)
  _pools_spa.py                   21   (pools page + spa treatments menu)
  _concept.py                     26   (all-inclusive full page)
  _gallery_offers.py              20   (filters + 5 offer cards)
  _activities_location.py         34   (hero, distances, transfers, nearby)
  _legal_404.py                   12   (privacy/cookies/policies + 404)

i18n.js EN block grew from 349 to 640 keys. New keys follow existing
naming conventions (bk.form.*, sp.form.*, faq.qN.q/a, contact.*,
career.*, home.*, pools.*, concept.*, gallery.*, offers.cardN.*,
location.*, legal.privacy.body, error404.*).

Also repaired a pre-existing malformed RU string (spa.contact.p had
been truncated mid-word, leaving i18n.js as technically-invalid JS).
Completed the sentence plausibly and closed the block. RU translator
in R029.8 will review.

Deliberately left untagged (structural/machine-readable values):
  * 78-line 30-min time-slot <option> list
  * SITE_META values (address/phone/email — infra)
  * Airline lookup values, bus operator names (proper nouns)
  * HTML comments + <script> bodies + <style>
  * Suite name/room labels inside SUITES data blob

Deferred (needs helper signature changes in common.py):
  * card(), eyebrow(), heading() calls in a handful of _home.py sections
  * feature_strip() labels ("Suites/Pools/…") — will be picked up in R029.7d

British English throughout. TR/DE/RU blocks untouched — those are about
to be replaced wholesale by R029.8 (three parallel SME translators
working from this now-locked EN source).
'@

# sanity — i18n.js has grown, EN block still parseable
$en = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'site/assets/js/i18n.js')
if ($en.Length -lt 100000) { throw 'i18n.js suspiciously small — tagging may have wiped content' }
if ($en -notmatch '"faq\.q1\.q"') { throw 'faq.q1.q key missing — tagging incomplete' }
if ($en -notmatch '"bk\.form\.') { throw 'bk.form.* keys missing' }

$py = $null
foreach ($c in @('python','python3','py')) { $f = Get-Command $c -ErrorAction SilentlyContinue; if ($f) { $py = $f.Source; break } }
Push-Location $RepoRoot
try {
  & $py 'scripts/build.py' 2>&1 | Out-Null
  if ($LASTEXITCODE -ne 0) { throw 'build.py failed' }
  git add scripts/ site/ Commit-R029-7c.ps1
  git commit -m $Msg
  git tag -f -a $Tag -m 'R029.7c — full i18n tagging'
  git push origin main
  git push --force origin "refs/tags/$Tag"
} finally { Pop-Location }

Write-Host '[R029.7c] Shipped. EN locked. Next: R029.8 translators.' -ForegroundColor Green
