# GitHub Auto-Sync Setup Guide

This guide explains how to set up automatic synchronization between your GitHub repositories and your portfolio website.

## 🚀 Features

- **Automatic Project Addition**: New GitHub repositories are automatically added to your portfolio
- **Real-time Updates**: Repository information is updated when you push changes
- **Smart Categorization**: Projects are automatically categorized based on language and description
- **Manual Sync**: You can manually sync all repositories at any time

## 📋 Setup Instructions

### 1. Manual Sync (Recommended for Testing)

Run this command to sync all your current GitHub repositories:

```bash
python manage.py sync_github_projects --username bikalpokharel
```

**Options:**
- `--username`: Your GitHub username (default: bikalpokharel)
- `--token`: GitHub personal access token (optional, for private repos)
- `--force`: Force update existing projects

### 2. Automatic Sync with GitHub Webhooks

#### Step 1: Deploy Your Portfolio

Deploy your portfolio to a public URL (e.g., Heroku, DigitalOcean, etc.)

#### Step 2: Set Webhook Secret

In your production settings, set the webhook secret:

```python
GITHUB_WEBHOOK_SECRET = 'your-secure-random-string-here'
```

#### Step 3: Configure GitHub Webhook

1. Go to your GitHub repository settings
2. Navigate to **Webhooks** → **Add webhook**
3. Set the **Payload URL** to: `https://yourdomain.com/webhook/github/`
4. Set **Content type** to: `application/json`
5. Set **Secret** to the same value as `GITHUB_WEBHOOK_SECRET`
6. Select events: **Repository** and **Push**
7. Click **Add webhook**

#### Step 4: Test the Webhook

1. Create a new repository on GitHub
2. The repository should automatically appear in your portfolio
3. Check the webhook delivery logs in GitHub for any errors

## 🔧 How It Works

### Project Categorization

Projects are automatically categorized based on:

- **Web App**: Contains keywords like 'web', 'website', 'app', 'django', 'flask', 'react'
- **ML Project**: Contains keywords like 'ml', 'machine learning', 'ai', 'tensorflow', 'pytorch'
- **Mobile App**: Contains keywords like 'mobile', 'android', 'ios', 'react native', 'flutter'
- **AI Project**: Contains keywords like 'ai', 'artificial intelligence', 'chatbot', 'nlp'
- **Data Science**: Contains keywords like 'data', 'analysis', 'visualization', 'pandas', 'numpy'
- **Other**: Default category for other projects

### Repository Filtering

The system automatically excludes:
- Forked repositories
- Private repositories
- Archived repositories
- The portfolio repository itself

### Project Information

Each project includes:
- **Title**: Formatted from repository name
- **Description**: Repository description or auto-generated
- **Detailed Description**: Includes repository stats, creation date, technologies
- **GitHub URL**: Direct link to the repository
- **Project Type**: Automatically determined category
- **Status**: Set to 'completed' for active repositories

## 🛠️ Management Commands

### Sync All Repositories
```bash
python manage.py sync_github_projects --username bikalpokharel
```

### Sync with GitHub Token (for private repos)
```bash
python manage.py sync_github_projects --username bikalpokharel --token your-github-token
```

### Force Update Existing Projects
```bash
python manage.py sync_github_projects --username bikalpokharel --force
```

## 🔒 Security

- Webhook signatures are verified to ensure requests come from GitHub
- CSRF protection is disabled only for the webhook endpoint
- Webhook secret should be kept secure and not shared

## 📝 Customization

### Adding Demo URLs

After projects are synced, you can manually add demo URLs through the Django admin:

1. Go to `/admin/`
2. Navigate to **Projects**
3. Edit any project
4. Add the **Demo URL** field
5. Save

### Customizing Project Descriptions

You can customize project descriptions in the Django admin or by editing the repository description on GitHub.

## 🚨 Troubleshooting

### Webhook Not Working

1. Check that your portfolio is publicly accessible
2. Verify the webhook URL is correct
3. Check webhook delivery logs in GitHub
4. Ensure the webhook secret matches your settings

### Projects Not Syncing

1. Run the manual sync command to test
2. Check that repositories are not private, forked, or archived
3. Verify your GitHub username is correct
4. Check for any error messages in the command output

### Duplicate Projects

If you see duplicate projects:
1. Clear all projects: `python manage.py shell -c "from home.models import Project; Project.objects.all().delete()"`
2. Re-run the sync command

## 📞 Support

If you encounter any issues:
1. Check the Django logs
2. Verify your GitHub repository settings
3. Test with the manual sync command first
4. Check the webhook delivery logs in GitHub

---

**Your portfolio will now automatically stay up-to-date with your GitHub repositories!** 🎉
