# 014 cutover §2：搬运本地相（非入库物）M2 -> M1
# 用法: powershell -NoProfile -ExecutionPolicy Bypass -File copy-local-phase.ps1
$ErrorActionPreference = 'Continue'
$src = 'D:\SEP-CN'
$dst = 'C:\Users\ykla\Documents\SEP-CN'
$dirs = @('en', 'yuanwen', 'script', 'state', '.secrets')

foreach ($d in $dirs) {
  $s = Join-Path $src $d
  $t = Join-Path $dst $d
  if (-not (Test-Path $s)) { Write-Host ("{0}: SKIP（源不存在）" -f $d); continue }
  $t0 = Get-Date
  $log = Join-Path $env:TEMP ("014-robocopy-{0}.log" -f ($d -replace '[^\w]', '_'))
  robocopy $s $t /MIR /R:1 /W:1 /MT:16 /NFL /NDL /NP /LOG:$log | Out-Null
  $rc = $LASTEXITCODE
  $n = (Get-ChildItem -Path $t -Recurse -File -ErrorAction SilentlyContinue | Measure-Object).Count
  $gb = [math]::Round(((Get-ChildItem -Path $t -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum / 1GB), 2)
  $verdict = if ($rc -lt 8) { 'OK' } else { 'FAIL' }
  Write-Host ("{0}: {1} rc={2} files={3} size={4}GB secs={5:N0}" -f $d, $verdict, $rc, $n, $gb, ((Get-Date) - $t0).TotalSeconds)
}
