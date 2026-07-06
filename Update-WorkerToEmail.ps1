#requires -Version 7.4
# R029 hotfix — repoint TO_EMAIL. Ran once 2026-07-06. Token REDACTED.
# Re-populate $Token from the Systems Health register if you need to re-run.

$ErrorActionPreference = 'Stop'

$Token   = '<CLOUDFLARE_WORKERS_EDIT_TOKEN>'
$Account = '22454088d7841d89c5e82a155a6654b7'
$Script  = 'mira-palace-enquiry'
$NewTo   = 'miworldptyltd@gmail.com'

if ($Token -like '<*>') { throw 'Fill in $Token from Systems Health doc.' }

$H = @{ Authorization = "Bearer $Token"; 'Content-Type' = 'application/json' }
$url = "https://api.cloudflare.com/client/v4/accounts/$Account/workers/scripts/$Script/secrets"
$body = @{ name = 'TO_EMAIL'; text = $NewTo; type = 'secret_text' } | ConvertTo-Json -Compress
$r = Invoke-RestMethod -Method PUT -Uri $url -Headers $H -Body $body
Write-Host ("TO_EMAIL -> {0}   success={1}" -f $NewTo, $r.success)
