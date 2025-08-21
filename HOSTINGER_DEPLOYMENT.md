# 🚀 Hostinger Deployment Guide - Creative Brief Form

## Overview
This guide will help you deploy your Creative Brief Form to Hostinger hosting with the subdomain `www.creative-brief.chroniclecraft.tech`.

## 📋 Prerequisites
- Hostinger hosting account with Python support
- Access to cPanel File Manager or FTP
- Subdomain `www.creative-brief.chroniclecraft.tech` already created

## 🔧 Step 1: Prepare Files for Upload

### Files to Upload:
- `passenger_wsgi.py` (WSGI entry point)
- `app_production.py` (Main application)
- `index.html` (Frontend)
- `styles.css` (Styling)
- `script.js` (Frontend logic)
- `requirements.txt` (Dependencies)
- `.env` (Environment variables - copy from .env.production)
- All image/asset files

### Files NOT to upload:
- `.env.production` (template only)
- `deploy.ps1`, `setup.ps1` (development scripts)
- `.git` folder
- `__pycache__` folders
- Development-only files

## 🌐 Step 2: Upload to Hostinger

### Method 1: Using cPanel File Manager
1. **Login to Hostinger cPanel**
2. **Navigate to File Manager**
3. **Go to your subdomain folder**:
   - Look for `public_html/www.creative-brief` or similar
   - If not exists, create it under `public_html/`
4. **Upload all required files** to this directory
5. **Set permissions**:
   - `passenger_wsgi.py`: 755
   - All other `.py` files: 644
   - Static files (html, css, js): 644

### Method 2: Using FTP
1. **Connect via FTP client** (FileZilla, WinSCP)
2. **Navigate to subdomain directory**
3. **Upload all files**
4. **Set proper permissions**

## ⚙️ Step 3: Configure Environment

### Create .env file on server:
1. **In cPanel File Manager**, create new file named `.env`
2. **Copy content from `.env.production`**:
```env
# Email Configuration (Hostinger SMTP)
SMTP_SERVER=smtp.hostinger.com
SMTP_PORT=587
SMTP_USERNAME=irfan@chroniclecraft.tech
SMTP_PASSWORD=!Creative@2025!
FROM_EMAIL=irfan@chroniclecraft.tech
TO_EMAIL=irfan@chroniclecraft.tech

# Application Configuration
FLASK_ENV=production
SECRET_KEY=a7f8e9d2c1b4a6e5f8d9c2b1a4e7f0d3c6b9a2e5f8d1c4b7a0e3f6d9c2b5a8e1f4d7
DEBUG=False

# Domain Configuration
DOMAIN_NAME=chroniclecraft.tech
WEBSITE_URL=https://www.creative-brief.chroniclecraft.tech
```

## 🐍 Step 4: Configure Python Application

### Option A: Using cPanel Python App Manager (Recommended)
1. **Go to cPanel → Software → Python Selector/Python App**
2. **Create New Application**:
   - **Python version**: 3.8 or higher
   - **Application root**: `/public_html/www.creative-brief` (or your subdomain path)
   - **Application URL**: `www.creative-brief.chroniclecraft.tech`
   - **Application startup file**: `passenger_wsgi.py`
   - **Application Entry point**: `application`

3. **Install Requirements**:
   - In the Python app interface, click "Run pip install"
   - Upload or specify `requirements.txt`
   - Click "Install"

### Option B: Manual Configuration
If your hosting doesn't have Python App Manager:

1. **Create .htaccess file**:
```apache
RewriteEngine on
PassengerEnabled on
PassengerAppRoot /home/username/public_html/www.creative-brief
PassengerPython /home/username/python/bin/python3
```

2. **Install dependencies manually** (via SSH if available):
```bash
pip3 install --user -r requirements.txt
```

## 🌍 Step 5: Domain Configuration

### Subdomain Setup:
1. **In Hostinger Panel → Domains → Subdomains**
2. **Verify subdomain exists**: `www.creative-brief.chroniclecraft.tech`
3. **Document root should point to**: `/public_html/www.creative-brief/`
4. **If not set correctly, update the path**

### SSL Certificate:
1. **In Hostinger Panel → Security → SSL/TLS**
2. **Enable SSL for the subdomain**
3. **Choose "Let's Encrypt" for free certificate**
4. **Force HTTPS redirect**

## 🧪 Step 6: Testing

### Test the deployment:
1. **Visit**: `https://www.creative-brief.chroniclecraft.tech`
2. **Check form loads properly**
3. **Submit a test form**
4. **Verify email delivery**
5. **Check error logs** in cPanel if issues occur

### Health Check:
- Visit: `https://www.creative-brief.chroniclecraft.tech/health` (if implemented)

## 📧 Step 7: Email Testing

### Test SMTP configuration:
1. **Submit test form**
2. **Check if emails are received at**: `irfan@chroniclecraft.tech`
3. **Check spam folder** if emails missing
4. **View application logs** for email errors

### Troubleshooting Email Issues:
- **SMTP Authentication Failed**: Verify password in `.env`
- **Connection refused**: Check if port 587 is allowed
- **Emails in spam**: Set up SPF/DKIM records

## 📁 Final Directory Structure on Server

```
/public_html/www.creative-brief/
├── passenger_wsgi.py          # WSGI entry point
├── app_production.py          # Main Flask app
├── index.html                 # Frontend
├── styles.css                 # Styling
├── script.js                  # JavaScript
├── requirements.txt           # Dependencies
├── .env                       # Environment variables
├── .htaccess                  # Apache configuration (if needed)
└── assets/                    # Any images or static files
    └── (image files)
```

## ✅ Go-Live Checklist

- [ ] All files uploaded to correct directory
- [ ] `.env` file created with correct credentials
- [ ] Python application configured in cPanel
- [ ] Dependencies installed
- [ ] Subdomain pointing to correct directory
- [ ] SSL certificate active
- [ ] Form loads without errors
- [ ] Test form submission successful
- [ ] Email delivery confirmed
- [ ] Error logging configured

## 🆘 Troubleshooting

### Common Issues:

1. **"Application not found" error**:
   - Check `passenger_wsgi.py` is in root directory
   - Verify file permissions (755 for .py files)
   - Check Python path in application settings

2. **"Module not found" errors**:
   - Ensure all requirements are installed
   - Check Python version compatibility
   - Verify virtual environment setup

3. **Email not sending**:
   - Check SMTP credentials in `.env`
   - Verify Hostinger allows SMTP on port 587
   - Test with different email provider if needed

4. **Static files not loading**:
   - Check file paths in `app_production.py`
   - Verify permissions on CSS/JS files
   - Check .htaccess rules

### Getting Help:
- Check Hostinger error logs in cPanel
- Contact Hostinger support for Python-specific issues
- Check application logs for detailed error messages

## 🔄 Updates & Maintenance

### To update the application:
1. **Download/backup current files**
2. **Upload new files via FTP/File Manager**
3. **Update `.env` if needed**
4. **Restart Python application** (if option available)
5. **Test functionality**

---

**Deployment prepared for**: www.creative-brief.chroniclecraft.tech  
**Email configured for**: irfan@chroniclecraft.tech  
**Ready for production deployment** ✅
