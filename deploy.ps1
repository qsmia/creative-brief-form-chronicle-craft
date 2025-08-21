# ChronicleChraft Creative Brief Form - Windows Deployment Script
# Run this script in PowerShell to deploy your application

param(
    [Parameter(Mandatory=$false)]
    [string]$Platform = "heroku",
    
    [Parameter(Mandatory=$false)]
    [string]$AppName = "chroniclecraft-forms"
)

Write-Host "🚀 ChronicleChraft Creative Brief Form Deployment" -ForegroundColor Blue
Write-Host "=================================================" -ForegroundColor Blue

# Check if required tools are installed
function Test-Command($cmdname) {
    return [bool](Get-Command -Name $cmdname -ErrorAction SilentlyContinue)
}

# Check prerequisites
Write-Host "📋 Checking prerequisites..." -ForegroundColor Yellow

if (-not (Test-Command "git")) {
    Write-Host "❌ Git is not installed. Please install Git first." -ForegroundColor Red
    exit 1
}

if (-not (Test-Command "python")) {
    Write-Host "❌ Python is not installed. Please install Python 3.11+ first." -ForegroundColor Red
    exit 1
}

Write-Host "✅ Prerequisites check passed!" -ForegroundColor Green

# Initialize git repository if not exists
if (-not (Test-Path ".git")) {
    Write-Host "🔧 Initializing Git repository..." -ForegroundColor Yellow
    git init
    git add .
    git commit -m "Initial commit - ChronicleChraft Creative Brief Form"
}

# Platform-specific deployment
switch ($Platform.ToLower()) {
    "heroku" {
        Write-Host "🌐 Deploying to Heroku..." -ForegroundColor Green
        
        if (-not (Test-Command "heroku")) {
            Write-Host "❌ Heroku CLI is not installed. Please install from https://devcenter.heroku.com/articles/heroku-cli" -ForegroundColor Red
            exit 1
        }
        
        # Create Heroku app
        Write-Host "Creating Heroku app: $AppName" -ForegroundColor Yellow
        heroku create $AppName
        
        # Set environment variables
        Write-Host "⚙️ You need to set up environment variables. Run these commands:" -ForegroundColor Yellow
        Write-Host "heroku config:set SMTP_SERVER=smtp.gmail.com" -ForegroundColor Cyan
        Write-Host "heroku config:set SMTP_PORT=587" -ForegroundColor Cyan
        Write-Host "heroku config:set SMTP_USERNAME=your-email@gmail.com" -ForegroundColor Cyan
        Write-Host "heroku config:set SMTP_PASSWORD=your-app-password" -ForegroundColor Cyan
        Write-Host "heroku config:set FROM_EMAIL=noreply@chroniclecraft.tech" -ForegroundColor Cyan
        Write-Host "heroku config:set TO_EMAIL=irfan@chroniclecraft.tech" -ForegroundColor Cyan
        Write-Host "heroku config:set SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')" -ForegroundColor Cyan
        Write-Host "heroku config:set WEBSITE_URL=https://$AppName.herokuapp.com" -ForegroundColor Cyan
        
        Read-Host "Press Enter after setting up environment variables..."
        
        # Deploy
        Write-Host "🚀 Deploying to Heroku..." -ForegroundColor Green
        git push heroku main
        
        Write-Host "✅ Deployment complete! Your app is available at: https://$AppName.herokuapp.com" -ForegroundColor Green
    }
    
    "vercel" {
        Write-Host "🌐 Deploying to Vercel..." -ForegroundColor Green
        
        if (-not (Test-Command "vercel")) {
            Write-Host "❌ Vercel CLI is not installed. Install with: npm i -g vercel" -ForegroundColor Red
            exit 1
        }
        
        Write-Host "🚀 Running Vercel deployment..." -ForegroundColor Green
        vercel --prod
        
        Write-Host "⚙️ Don't forget to set environment variables in Vercel dashboard!" -ForegroundColor Yellow
    }
    
    default {
        Write-Host "❌ Unsupported platform: $Platform. Supported: heroku, vercel" -ForegroundColor Red
        exit 1
    }
}

Write-Host ""
Write-Host "🎉 Deployment process completed!" -ForegroundColor Green
Write-Host "📖 Check DEPLOYMENT_GUIDE.md for detailed configuration instructions." -ForegroundColor Blue
