# ChronicleChraft Creative Brief Form - Deployment Guide

## 🚀 Production Setup & Deployment Options

This guide covers setting up your Creative Brief Form for production deployment with proper email functionality.

---

## 📋 Prerequisites

- Python 3.11+ installed
- Git installed
- Access to your `irfan@chroniclecraft.tech` email account
- A hosting platform account (Heroku, Vercel, Railway, etc.)

---

## 🔧 Email Configuration Setup

### 1. Gmail SMTP Setup (Recommended)

If you want to send emails from Gmail:

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate App Password**:
   - Go to Google Account Settings → Security
   - Under "Signing in to Google" → App passwords
   - Generate password for "Mail"
   - Copy the 16-character password

3. **Update Environment Variables**:
   ```env
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USERNAME=your-gmail@gmail.com
   SMTP_PASSWORD=your-16-char-app-password
   FROM_EMAIL=noreply@chroniclecraft.tech
   TO_EMAIL=irfan@chroniclecraft.tech
   ```

### 2. Custom Domain SMTP (Professional Option)

For `@chroniclecraft.tech` email addresses:

**Option A: Google Workspace**
```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=irfan@chroniclecraft.tech
SMTP_PASSWORD=your-workspace-password
```

**Option B: Other Email Providers**
- **Outlook/Hotmail**: `smtp.office365.com:587`
- **Yahoo**: `smtp.mail.yahoo.com:587`
- **SendGrid**: `smtp.sendgrid.net:587` (Professional option)
- **Mailgun**: Configure via their SMTP settings

---

## 🌐 Deployment Options

### Option 1: Heroku (Recommended for beginners)

1. **Install Heroku CLI** from [heroku.com](https://devcenter.heroku.com/articles/heroku-cli)

2. **Deploy Steps**:
   ```bash
   # Navigate to project folder
   cd C:\Users\TECHNOSELLERS\Desktop\creative-brief-form-chronicle-craft

   # Initialize git (if not already done)
   git init
   git add .
   git commit -m "Initial commit"

   # Create Heroku app
   heroku create your-app-name

   # Set environment variables
   heroku config:set SMTP_SERVER=smtp.gmail.com
   heroku config:set SMTP_PORT=587
   heroku config:set SMTP_USERNAME=your-email@gmail.com
   heroku config:set SMTP_PASSWORD=your-app-password
   heroku config:set FROM_EMAIL=noreply@chroniclecraft.tech
   heroku config:set TO_EMAIL=irfan@chroniclecraft.tech
   heroku config:set SECRET_KEY=your-random-secret-key-here
   heroku config:set WEBSITE_URL=https://your-app-name.herokuapp.com

   # Deploy
   git push heroku main
   ```

3. **Custom Domain Setup**:
   ```bash
   # Add your domain
   heroku domains:add forms.chroniclecraft.tech

   # Get DNS target (add this as CNAME in your DNS)
   heroku domains
   ```

### Option 2: Vercel (Fast & Simple)

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Deploy**:
   ```bash
   cd C:\Users\TECHNOSELLERS\Desktop\creative-brief-form-chronicle-craft
   vercel --prod
   ```

3. **Environment Variables** (via Vercel Dashboard):
   - Go to your project → Settings → Environment Variables
   - Add all the SMTP variables listed above

### Option 3: Railway (Modern Platform)

1. **Connect GitHub**:
   - Push your code to GitHub
   - Connect Railway to your repository

2. **Environment Variables**:
   ```env
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USERNAME=your-email@gmail.com
   SMTP_PASSWORD=your-app-password
   FROM_EMAIL=noreply@chroniclecraft.tech
   TO_EMAIL=irfan@chroniclecraft.tech
   SECRET_KEY=generate-random-key
   WEBSITE_URL=https://your-app.railway.app
   ```

### Option 4: DigitalOcean App Platform

1. **Upload to GitHub**
2. **Connect DigitalOcean** to your repository
3. **Configure Environment Variables** in the dashboard
4. **Deploy automatically**

---

## 🏗️ Custom Domain Setup

### For chroniclecraft.tech Domain

1. **DNS Configuration**:
   ```dns
   Type: CNAME
   Name: forms (or creative-brief)
   Value: your-hosting-platform-url
   ```

2. **SSL Certificate**:
   - Most platforms (Heroku, Vercel, Railway) provide automatic SSL
   - For custom setups, use Let's Encrypt

3. **Update Environment Variables**:
   ```env
   WEBSITE_URL=https://forms.chroniclecraft.tech
   ```

---

## 🔐 Security Configuration

### Environment Variables Checklist

Create a `.env` file (don't commit this):
```env
# Email Settings
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
FROM_EMAIL=noreply@chroniclecraft.tech
TO_EMAIL=irfan@chroniclecraft.tech

# Security
SECRET_KEY=your-super-secret-key-generate-this-randomly
DEBUG=False
FLASK_ENV=production

# Domain
WEBSITE_URL=https://your-domain.com
```

### Generate Secret Key (Python):
```python
import secrets
print(secrets.token_hex(32))
```

---

## 🧪 Testing Your Deployment

### 1. Local Testing
```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables (create .env file)
# Run locally
python app_production.py
```

### 2. Production Testing
1. **Health Check**: Visit `https://your-domain.com/health`
2. **Form Test**: Submit a test form
3. **Email Test**: Verify both admin and client emails are received

---

## 📧 Email Troubleshooting

### Common Issues:

1. **"Authentication Failed"**:
   - Verify Gmail app password is correct
   - Ensure 2FA is enabled on Gmail
   - Check username/password in environment variables

2. **"Connection Refused"**:
   - Verify SMTP server and port
   - Check firewall settings on hosting platform

3. **Emails Going to Spam**:
   - Set up SPF/DKIM records for your domain
   - Use a professional email service (SendGrid, Mailgun)

### Email Service Alternatives:

**SendGrid (Recommended for high volume)**:
```env
SMTP_SERVER=smtp.sendgrid.net
SMTP_PORT=587
SMTP_USERNAME=apikey
SMTP_PASSWORD=your-sendgrid-api-key
```

**Mailgun**:
```env
SMTP_SERVER=smtp.mailgun.org
SMTP_PORT=587
SMTP_USERNAME=your-mailgun-username
SMTP_PASSWORD=your-mailgun-password
```

---

## 🔄 Maintenance & Updates

### Regular Tasks:
1. **Monitor Email Delivery**: Check logs for failed email attempts
2. **Update Dependencies**: `pip install --upgrade -r requirements.txt`
3. **Security Updates**: Keep Flask and dependencies updated
4. **Backup Form Submissions**: Consider adding database storage

### Monitoring:
- Set up uptime monitoring (UptimeRobot, Pingdom)
- Configure error logging (Sentry)
- Monitor email delivery rates

---

## 🆘 Support & Contact

**Technical Issues**:
- Check application logs on your hosting platform
- Test email configuration with `/health` endpoint
- Verify all environment variables are set correctly

**Email Configuration Help**:
- Gmail: [Google App Passwords Guide](https://support.google.com/accounts/answer/185833)
- Outlook: [Microsoft App Passwords](https://support.microsoft.com/en-us/account-billing/using-app-passwords-with-apps-that-don-t-support-two-step-verification-5896ed9b-4263-e681-128a-a6f2979a7944)

---

## ✅ Go-Live Checklist

- [ ] Environment variables configured
- [ ] Email sending tested and working
- [ ] Custom domain configured (if applicable)
- [ ] SSL certificate active
- [ ] Form submission tested end-to-end
- [ ] Both admin and client emails received
- [ ] Error handling verified
- [ ] Monitoring set up
- [ ] Backup plan in place

---

**Created for ChronicleChraft Creative Solutions**  
**Version**: 1.0 Production Ready  
**Last Updated**: August 2025
