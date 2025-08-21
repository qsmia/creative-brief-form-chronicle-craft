# ChronicleChraft Creative Brief Form - Local Setup Script
# Run this script in PowerShell to set up local development environment

Write-Host "🛠️ ChronicleChraft Creative Brief Form - Local Setup" -ForegroundColor Blue
Write-Host "==================================================" -ForegroundColor Blue

# Check if Python is installed
if (-not (Get-Command "python" -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python is not installed. Please install Python 3.11+ first." -ForegroundColor Red
    exit 1
}

# Check Python version
$pythonVersion = python --version 2>&1
Write-Host "✅ Found Python: $pythonVersion" -ForegroundColor Green

# Install dependencies
Write-Host "📦 Installing Python dependencies..." -ForegroundColor Yellow
python -m pip install --upgrade pip
pip install -r requirements.txt

# Create .env file if it doesn't exist
if (-not (Test-Path ".env")) {
    Write-Host "🔧 Creating .env file..." -ForegroundColor Yellow
    Copy-Item ".env.example" ".env"
    
    Write-Host "⚙️ Please edit the .env file with your email configuration:" -ForegroundColor Yellow
    Write-Host "   - SMTP_USERNAME: Your Gmail address" -ForegroundColor Cyan
    Write-Host "   - SMTP_PASSWORD: Your Gmail app password" -ForegroundColor Cyan
    Write-Host "   - SECRET_KEY: Generate a random secret key" -ForegroundColor Cyan
    
    # Generate a secret key
    $secretKey = python -c "import secrets; print(secrets.token_hex(32))"
    Write-Host "   Generated SECRET_KEY: $secretKey" -ForegroundColor Green
    
    Write-Host ""
    Write-Host "📧 Gmail Setup Instructions:" -ForegroundColor Yellow
    Write-Host "1. Enable 2-Factor Authentication on your Gmail account" -ForegroundColor White
    Write-Host "2. Go to Google Account Settings → Security → App passwords" -ForegroundColor White
    Write-Host "3. Generate password for 'Mail'" -ForegroundColor White
    Write-Host "4. Copy the 16-character password to SMTP_PASSWORD in .env" -ForegroundColor White
}

Write-Host ""
Write-Host "🧪 To test locally:" -ForegroundColor Green
Write-Host "   python app_production.py" -ForegroundColor Cyan
Write-Host ""
Write-Host "🌐 To deploy to production:" -ForegroundColor Green
Write-Host "   .\deploy.ps1 -Platform heroku" -ForegroundColor Cyan
Write-Host "   .\deploy.ps1 -Platform vercel" -ForegroundColor Cyan
Write-Host ""
Write-Host "✅ Local setup complete!" -ForegroundColor Green
