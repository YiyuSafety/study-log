param(
[string]$Message = "update study log"
)

$ErrorActionPreference = "Stop"

# 进入仓库目录

Set-Location "G:\Code\study-log"

Write-Host "=============================="
Write-Host "当前目录：$(Get-Location)"
Write-Host "提交信息：$Message"
Write-Host "=============================="

# 检查是否是 Git 仓库

if (-not (Test-Path ".git")) {
Write-Host "错误：当前目录不是 Git 仓库。" -ForegroundColor Red
exit 1
}

# 查看当前状态

Write-Host "`n[1/5] 检查本地改动..."
git status

# 如果有本地改动，先提交

$changes = git status --porcelain

if ($changes) {
Write-Host "`n[2/5] 检测到本地改动，开始 add + commit..."
    git add .
    git commit -m $Message
} else {
    Write-Host "`n[2/5] 没有本地改动，跳过 commit。"
}

# 拉取远程更新并 rebase

Write-Host "`n[3/5] 拉取远程更新..."
git pull --rebase origin main

# 推送到 GitHub

Write-Host "`n[4/5] 推送到 GitHub..."
git push origin main

# 最终状态

Write-Host "`n[5/5] 最终状态："
git status

Write-Host "`n完成。"
