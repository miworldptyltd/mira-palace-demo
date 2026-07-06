#requires -Version 7.4
<#
.SYNOPSIS
  R029 — set the 5 Worker env vars via Cloudflare API in one shot.

.DESCRIPTION
  Idempotent. Ran once on 2026-07-06 and successfully set all 5 secrets.
  Secrets are REDACTED from this file — pull them from the Systems Health
  register at C:\Claude Projects\Mira Palace\Mira_Palace_Systems_Health.docx
  if you need to re-run.

  Never commit real secret values to this file.
#>

$ErrorActionPreference = 'Stop'

# Fill these from the Systems Health register before re-running.
$Token   = '<CLOUDFLARE_WORKERS_EDIT_TOKEN>'
$Account = '<CLOUDFLARE_ACCOUNT_ID>'
$Script  = 'mira-palace-enquiry'

$Secrets = [ordered]@{
  RESEND_API_KEY   = '<RESEND_API_KEY>'
  TURNSTILE_SECRET = '<TURNSTILE_SECRET>'
  TO_EMAIL         = 'info@miworld.tech'
  FROM_EMAIL       = 'onboarding@resend.dev'
  ALLOWED_ORIGINS  = 'https://miworldptyltd.github.io'
}

# Guard: refuse to run with placeholders.
foreach ($k in @('Token','Account')) {
  if ((Get-Variable $k -ValueOnly) -like '<*>') {
    throw "Fill in `\$$k first (see Systems Health register)."
  }
}
foreach ($k in $Secrets.Keys) {
  if ($Secrets[$k] -like '<*>') {
    throw "Fill in `\$Secrets['$k'] first (see Systems Health register)."
  }
}

$Headers = @{ Authorization = "Bearer $Token"; 'Content-Type' = 'application/json' }

Write-Host '[R029] Verifying token...' -ForegroundColor Cyan
$v = Invoke-RestMethod -Method GET -Uri 'https://api.cloudflare.com/client/v4/user/tokens/verify' -Headers $Headers
if (-not ($v.success -and $v.result.status -eq 'active')) { throw 'Token verify failed' }
Write-Host '  [ok]' -ForegroundColor Green

$url = "https://api.cloudflare.com/client/v4/accounts/$Account/workers/scripts/$Script/secrets"
foreach ($name in $Secrets.Keys) {
  $body = @{ name = $name; text = $Secrets[$name]; type = 'secret_text' } | ConvertTo-Json -Compress
  $r = Invoke-RestMethod -Method PUT -Uri $url -Headers $Headers -Body $body
  Write-Host ("  {0} -> success={1}" -f $name, $r.success) -ForegroundColor $(if ($r.success) {'Green'} else {'Red'})
}
Write-Host '[R029] Done.' -ForegroundColor Cyan
