# 🚀 Quick Start - ChronicleChraft Creative Brief Form

## Deployment in 3 Steps

### Step 1: Setup
```powershell
# Run in PowerShell
.\setup.ps1
```
This installs dependencies and creates your `.env` file.

### Step 2: Configure Email
1. **Enable 2FA** on your Gmail account
2. **Generate App Password**:
   - Gmail Settings → Security → App passwords → Mail
   - Copy the 16-character password
3. **Edit `.env` file**:
   ```env
   SMTP_USERNAME=your-email@gmail.com
   SMTP_PASSWORD=your-16-char-app-password
   ```

### Step 3: Deploy
```powershell
# Deploy to Heroku
.\deploy.ps1 -Platform heroku -AppName your-app-name

# OR Deploy to Vercel
.\deploy.ps1 -Platform vercel
```

## 🧪 Test Locally First
```powershell
python app_production.py
```
Visit: http://localhost:5000

## 🌐 Custom Domain Setup

### For chroniclecraft.tech:
1. **DNS Setup**:
   ```dns
   Type: CNAME
   Name: forms
   Value: your-app-url.herokuapp.com
   ```

2. **Heroku Domain**:
   ```bash
   heroku domains:add forms.chroniclecraft.tech
   ```

## 📧 Email Providers

### Gmail (Recommended)
- Easy setup with app passwords
- Reliable delivery
- Free tier available

### Professional Options
- **SendGrid**: Best for high volume
- **Mailgun**: Developer-friendly
- **Google Workspace**: Professional @chroniclecraft.tech

## ✅ Go-Live Checklist

- [ ] Dependencies installed (`.\setup.ps1`)
- [ ] Email configured in `.env`
- [ ] Local testing successful
- [ ] Deployed to hosting platform
- [ ] Environment variables set on platform
- [ ] Custom domain configured (optional)
- [ ] Test form submission end-to-end
- [ ] Both admin and client emails received

## 🆘 Need Help?

1. **Check DEPLOYMENT_GUIDE.md** for detailed instructions
2. **Test email config**: Visit `/health` endpoint
3. **View logs**: Check your hosting platform's logs
4. **Email issues**: Verify Gmail app password setup

---

**Quick Links:**
- 📖 [Full Deployment Guide](DEPLOYMENT_GUIDE.md)
- 🌐 Current Live Site: https://kkh7ikcydxd1.manus.space
- 📧 Email: irfan@chroniclecraft.tech
