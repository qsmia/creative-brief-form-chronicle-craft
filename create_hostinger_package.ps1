# Create Hostinger Deployment Package
Write-Host "🚀 Creating Hostinger Deployment Package..." -ForegroundColor Blue

# Create deployment directory
$deployDir = "hostinger_deployment"
if (Test-Path $deployDir) {
    Remove-Item $deployDir -Recurse -Force
}
New-Item -ItemType Directory -Name $deployDir

# Files to include in deployment
$filesToCopy = @(
    "passenger_wsgi.py",
    "app_production.py", 
    "index.html",
    "styles.css",
    "script.js",
    "requirements.txt",
    ".env.production",
    "kkh7ikcydxd1_manus_s_2025-08-20_15-53-06_6027.webp",
    "HOSTINGER_DEPLOYMENT.md"
)

# Copy files to deployment directory
Write-Host "📁 Copying files..." -ForegroundColor Yellow
foreach ($file in $filesToCopy) {
    if (Test-Path $file) {
        Copy-Item $file -Destination $deployDir
        Write-Host "  ✅ $file" -ForegroundColor Green
    } else {
        Write-Host "  ⚠️ $file (not found, skipping)" -ForegroundColor Yellow
    }
}

# Rename .env.production to .env in deployment folder
if (Test-Path "$deployDir\.env.production") {
    Rename-Item "$deployDir\.env.production" -NewName ".env"
    Write-Host "  OK .env.production to .env" -ForegroundColor Green
}

# Create archive
Write-Host "📦 Creating ZIP archive..." -ForegroundColor Yellow
Compress-Archive -Path "$deployDir\*" -DestinationPath "hostinger_creative_brief_deployment.zip" -Force

Write-Host ""
Write-Host "🎉 Deployment package created successfully!" -ForegroundColor Green
Write-Host "📁 Files prepared in: $deployDir" -ForegroundColor Cyan
Write-Host "📦 Archive created: hostinger_creative_brief_deployment.zip" -ForegroundColor Cyan
Write-Host ""
Write-Host "📋 Next Steps:" -ForegroundColor Blue
Write-Host "1. Extract hostinger_creative_brief_deployment.zip" -ForegroundColor White
Write-Host "2. Upload all files to your Hostinger cPanel File Manager" -ForegroundColor White
Write-Host "3. Follow the instructions in HOSTINGER_DEPLOYMENT.md" -ForegroundColor White
Write-Host "4. Configure Python application in cPanel" -ForegroundColor White
Write-Host "5. Test at: https://www.creative-brief.chroniclecraft.tech" -ForegroundColor White
