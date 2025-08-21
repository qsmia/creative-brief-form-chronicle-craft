# 🚀 Railway Deployment Guide - Creative Brief Form

## Overview
Deploy your Creative Brief Form to Railway with custom domain `www.creative-brief.chroniclecraft.tech`

## 🔧 Step 1: Deploy to Railway

### Method A: GitHub Deployment (Recommended)
1. **Create a GitHub repository** (if you don't have one):
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Creative Brief Form"
   git branch -M main
   git remote add origin https://github.com/yourusername/creative-brief-form.git
   git push -u origin main
   ```

2. **Sign up for Railway**: https://railway.app
3. **Connect GitHub account**
4. **Import your repository**
5. **Railway will auto-detect** it's a Python app
6. **Deploy automatically**

### Method B: Railway CLI (Alternative)
1. **Install Railway CLI**:
   ```bash
   npm install -g @railway/cli
   ```
2. **Login and deploy**:
   ```bash
   railway login
   railway init
   railway up
   ```

## ⚙️ Step 2: Configure Environment Variables

In your Railway dashboard:
1. **Go to Variables tab**
2. **Add these environment variables**:

```env
SMTP_SERVER=smtp.hostinger.com
SMTP_PORT=587
SMTP_USERNAME=irfan@chroniclecraft.tech
SMTP_PASSWORD=!Creative@2025!
FROM_EMAIL=irfan@chroniclecraft.tech
TO_EMAIL=irfan@chroniclecraft.tech
SECRET_KEY=a7f8e9d2c1b4a6e5f8d9c2b1a4e7f0d3c6b9a2e5f8d1c4b7a0e3f6d9c2b5a8e1f4d7
FLASK_ENV=production
DEBUG=False
WEBSITE_URL=https://www.creative-brief.chroniclecraft.tech
```

## 🌐 Step 3: Add Custom Domain

### In Railway Dashboard:
1. **Go to Settings → Domains**
2. **Add Custom Domain**: `www.creative-brief.chroniclecraft.tech`
3. **Railway will provide DNS instructions**

### In Hostinger DNS Management:
1. **Login to Hostinger control panel**
2. **Go to Domains → DNS Zone**
3. **Add/Edit CNAME record**:
   ```
   Type: CNAME
   Name: www.creative-brief
   Value: [Railway provided domain - something like: xyz123.railway.app]
   TTL: 300 (or default)
   ```

## 📋 Complete Deployment Steps

### 1. Push to GitHub (if not done):
```bash
# In your project directory
git init
git add .
git commit -m "Deploy Creative Brief Form to Railway"
git branch -M main
git remote add origin https://github.com/YOURUSERNAME/creative-brief-form.git
git push -u origin main
```

### 2. Deploy to Railway:
1. **Visit**: https://railway.app
2. **Sign up/Login** with GitHub
3. **Click "New Project"**
4. **Select "Deploy from GitHub repo"**
5. **Choose your repository**
6. **Railway auto-deploys**

### 3. Configure Environment:
Add all the environment variables listed above in Railway dashboard.

### 4. Add Custom Domain:
Follow the DNS configuration steps above.

### 5. Test:
Visit `https://www.creative-brief.chroniclecraft.tech`

## 🧪 Testing Your Deployment

1. **Check Railway logs** for any errors
2. **Visit health endpoint**: `https://www.creative-brief.chroniclecraft.tech/health`
3. **Submit test form**
4. **Verify email delivery**

## 💰 Cost Information

**Railway Free Tier**:
- ✅ $5 credit monthly (enough for small apps)
- ✅ Custom domains included
- ✅ SSL certificates included
- ✅ No credit card required to start

## 🆘 Troubleshooting

### Domain not working?
- Check DNS propagation (can take up to 24 hours)
- Verify CNAME record is correct
- Ensure subdomain exists in Hostinger

### App not starting?
- Check Railway logs for Python errors
- Verify environment variables are set
- Check `requirements.txt` is complete

### Email not sending?
- Verify SMTP credentials in Railway variables
- Check Railway logs for email errors
- Test SMTP connection

## 🔄 Alternative Platforms

If Railway doesn't work for you:

### Render (render.com)
- Similar to Railway
- Free tier available
- Custom domains on free tier
- Easy GitHub deployment

### Vercel (vercel.com)
- Great for Python apps
- Custom domains
- Simple deployment

---

**Your app will be live at**: `https://www.creative-brief.chroniclecraft.tech`  
**Email configured for**: `irfan@chroniclecraft.tech`  
**Ready for production use** ✅
