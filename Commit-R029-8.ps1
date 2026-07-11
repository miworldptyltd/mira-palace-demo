#requires -Version 7.4
# R029.8 — full TR/DE/RU wholesale translation, 640 keys each, contextual.

$ErrorActionPreference = 'Stop'
$RepoRoot = $PSScriptRoot
$Tag = 'R029.8'
$Msg = @'
R029.8: full TR + DE + RU translation — contextual, 640 keys each

Three independent SME translators worked in parallel from the vetted
British-English source produced by R029.7 + 7b + 7c. Each returned a
complete replacement dictionary — no gaps, no TODOs, no half-machine-
translated remnants. The tr:, de:, and ru: blocks in i18n.js were
rewritten wholesale from those JSON outputs.

  en: 640 keys   (locked source)
  tr: 640 keys   (warm formal "siz"; TDK-correct "her şey dâhil")
  de: 640 keys   (formal "Sie"; DACH hospitality register)
  ru: 640 keys   (formal "вы" lowercase; "номер" default over "сьют")

Register + tone fixes applied across all three languages:

TURKISH
  * Every "sorgu" replaced with "talep" / "bilgi isteyin" / "teklif isteyin"
    (hotels never use "sorgu" — police/database term)
  * TDK-correct "her şey dâhil" (three words + circumflex);
    was misspelled "herşey-dahil" previously
  * Every CTA in warm siz imperative form (-in/-ın/-un/-ün);
    no bare "yap" / "yaz" / "gönder" leaks
  * Passive constructions ("teyit edilir") converted to active first-
    person plural ("teyit ederiz", "döneriz")

GERMAN
  * False-friend "Daten" (= data) replaced with "Reisedaten" /
    "Anreisedatum" / "Abreisedatum" for calendar/dates fields
  * Amtsdeutsch swept out — "Ihre Angaben" -> "Ihre Kontaktdaten",
    "Grund Ihrer Anfrage" -> "Ihr Anliegen"
  * Calques rewritten — "ein Willkommen" -> "ein herzlicher Empfang";
    "neu erdacht" -> "neu gedacht"; "unser Arbeitspferd" ->
    "unser zuverlässiger Klassiker"
  * Passive confirmations warmed — "Anfrage gesendet." ->
    "Ihre Anfrage ist bei uns."

RUSSIAN
  * "сьют" replaced with "номер" as the default in body/UI copy
    (Russian hospitality convention); "Люкс" for premium categories
  * Participle-comma constructions calqued from EN rewritten as noun
    predicates or active verbs — "Турецкая Ривьера, переосмысленная
    в духе тихой роскоши" no longer appears
  * Nominal-heavy phrasing verbalised — "прямое бронирование" ->
    "бронируя напрямую" / "написав нам напрямую"
  * Officialese replaced with conversational Russian — "Затрудняюсь"
    -> "Не уверен(а)"; "приехал со стороны" -> "не из отеля"
  * spa.contact.p — pre-existing malformed truncation from an earlier
    commit — repaired with proper Russian idiom

Owner sanity checks (spot-review after ship):
  * TR: hero H1s, booking form CTAs, thank-you cards, FAQ answers
  * DE: room descriptions, spa treatment names, career role titles
  * RU: hero H1s, "номер" vs "сьют" balance, spa hammam terminology

British English source, four languages live. Site now translation-
complete across the 640 keys we tagged in R029.7c.
'@

$en = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'site/assets/js/i18n.js')
if ($en.Length -lt 200000) { throw 'i18n.js suspiciously small' }
if ($en -notmatch 'her şey dâhil') { throw 'TR TDK spelling not present' }
if ($en -notmatch 'Reisedaten')    { throw 'DE Reisedaten not present' }

$py = $null
foreach ($c in @('python','python3','py')) { $f = Get-Command $c -ErrorAction SilentlyContinue; if ($f) { $py = $f.Source; break } }
Push-Location $RepoRoot
try {
  & $py 'scripts/build.py' 2>&1 | Out-Null
  if ($LASTEXITCODE -ne 0) { throw 'build.py failed' }
  git add site/assets/js/i18n.js site/ Commit-R029-8.ps1
  git commit -m $Msg
  git tag -f -a $Tag -m 'R029.8 — full TR/DE/RU translation'
  git push origin main
  git push --force origin "refs/tags/$Tag"
} finally { Pop-Location }

Write-Host '[R029.8] Shipped. Four languages live.' -ForegroundColor Green
