# 🚀 PythonAnywhere Deployment Guide

## Step 1: Create PythonAnywhere Account
1. Go to [PythonAnywhere.com](https://www.pythonanywhere.com)
2. Sign up for a **FREE** account
3. Choose a username (this will be part of your URL)

## Step 2: Upload Your Code

### Option A: Git Clone (Recommended)
```bash
# In PythonAnywhere console
cd ~
git clone https://github.com/your-github-username/myportfolio.git
cd myportfolio
```

### Option B: Upload ZIP
1. Download your project as ZIP
2. Upload via PythonAnywhere Files tab
3. Extract in your home directory

## Step 3: Set Up Virtual Environment
```bash
# In PythonAnywhere console
cd ~/myportfolio
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 4: Configure Django Settings
1. Go to PythonAnywhere Dashboard → Web
2. Click "Add a new web app"
3. Choose "Manual configuration" → Python 3.11
4. Set these paths:
   - **Source code**: `/home/yourusername/myportfolio`
   - **Working directory**: `/home/yourusername/myportfolio`

## Step 5: Configure WSGI File
1. Click on "WSGI configuration file" link
2. Replace the content with the content from `pythonanywhere_wsgi.py`
3. Update `yourusername` with your actual PythonAnywhere username

## Step 6: Set Up Static Files
1. In PythonAnywhere console:
```bash
cd ~/myportfolio
source venv/bin/activate
python manage.py collectstatic --noinput
```

2. In Web tab, add static files mapping:
   - **URL**: `/static/`
   - **Directory**: `/home/yourusername/myportfolio/staticfiles/`

## Step 7: Set Up Media Files
In Web tab, add media files mapping:
- **URL**: `/media/`
- **Directory**: `/home/yourusername/myportfolio/media/`

## Step 8: Configure Environment Variables
1. Go to Web tab → Environment variables section
2. Add:
   - **Name**: `DEBUG` → **Value**: `False`
   - **Name**: `SECRET_KEY` → **Value**: `your-super-secret-key-here`

## Step 9: Run Database Migrations
```bash
cd ~/myportfolio
source venv/bin/activate
python manage.py migrate
python manage.py createsuperuser
python manage.py setup_portfolio
python manage.py sync_github_projects
```

## Step 10: Reload Web App
1. Go to Web tab
2. Click **"Reload"** button
3. Visit your site: `https://yourusername.pythonanywhere.com`

## 🎉 Your Portfolio is Live!

### Important Notes:
- Your site URL: `https://yourusername.pythonanywhere.com`
- Admin panel: `https://yourusername.pythonanywhere.com/admin/`
- Free accounts have 3 months of uptime
- SSL certificate is included for free

### Troubleshooting:
- Check error logs in Web tab → Error log
- Test in PythonAnywhere console first
- Make sure all file paths use your actual username

### Updates:
To update your site:
```bash
cd ~/myportfolio
git pull origin main
source venv/bin/activate
python manage.py collectstatic --noinput
# Click Reload in Web tab
```
