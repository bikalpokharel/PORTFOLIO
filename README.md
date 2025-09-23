# Bikal Sharma Pokharel - Portfolio Website

A modern, responsive portfolio website built with Django showcasing skills, projects, and professional experience.

## 🚀 Features

- **Modern Design**: Beautiful dark theme with purple/blue gradients
- **Responsive Layout**: Works perfectly on all devices
- **Project Showcase**: Filterable project gallery with detailed descriptions
- **Skills Display**: Categorized skills with proficiency levels
- **Contact Form**: Working contact form with email integration
- **Admin Panel**: Easy content management through Django admin
- **SEO Optimized**: Meta tags, sitemap, and search engine friendly
- **Performance**: Optimized static files and images

## 🛠️ Technologies Used

### Backend
- **Django 4.2.7** - Web framework
- **SQLite** - Development database
- **PostgreSQL** - Production database (psycopg2-binary)
- **Pillow** - Image processing

### Frontend
- **Bootstrap 5.3.2** - CSS framework
- **Custom CSS** - Dark theme with animations
- **Font Awesome 6.4.0** - Icons
- **AOS** - Scroll animations
- **Google Fonts** - Typography

### Deployment
- **Gunicorn** - WSGI server
- **WhiteNoise** - Static file serving
- **python-decouple** - Environment variables

## 📦 Installation

### Prerequisites
- Python 3.11+
- pip
- virtualenv

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd myportfolio
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Add sample content**
   ```bash
   python manage.py add_sample_content
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the website**
   - Website: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## ⚙️ Configuration

### Email Settings
Update email configuration in `myportfolio/settings.py`:

```python
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Gmail App Password
```

**To get Gmail App Password:**
1. Enable 2-factor authentication on your Google account
2. Go to Google Account settings > Security > App passwords
3. Generate a new app password for "Mail"
4. Use this password in your settings

### Environment Variables
For production, use environment variables:

```bash
export SECRET_KEY="your-secret-key"
export DEBUG=False
export ALLOWED_HOSTS="yourdomain.com,www.yourdomain.com"
export DATABASE_URL="postgresql://user:password@localhost/dbname"
```

## 📁 Project Structure

```
myportfolio/
├── home/                    # Main app
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── urls.py             # URL patterns
│   ├── admin.py            # Admin configuration
│   ├── templates/          # HTML templates
│   └── management/         # Custom commands
├── myportfolio/            # Project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL config
│   └── wsgi.py             # WSGI config
├── static/                 # Static files
├── media/                  # User uploads
├── requirements.txt        # Dependencies
└── manage.py              # Django management
```

## 🎨 Customization

### Adding New Skills
1. Go to Django admin: `/admin/`
2. Navigate to "Skills"
3. Add new skills with categories and proficiency levels

### Adding Projects
1. Go to Django admin: `/admin/`
2. Navigate to "Projects"
3. Add project details, images, and links

### Customizing Design
- Edit `static/css/custom.css` for custom styles
- Modify templates in `home/templates/home/`
- Update color scheme in `base.html` CSS variables

## 🚀 Deployment

### Heroku Deployment

1. **Install Heroku CLI**

2. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

3. **Set environment variables**
   ```bash
   heroku config:set SECRET_KEY="your-secret-key"
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"
   ```

4. **Add PostgreSQL**
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

5. **Deploy**
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

6. **Run migrations**
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py add_sample_content
   heroku run python manage.py createsuperuser
   ```

### DigitalOcean/VPS Deployment

1. **Setup server**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv nginx postgresql
   ```

2. **Clone and setup**
   ```bash
   git clone <your-repo>
   cd myportfolio
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure database**
   ```bash
   sudo -u postgres createdb portfolio_db
   sudo -u postgres createuser portfolio_user
   ```

4. **Configure Nginx**
   ```bash
   sudo nano /etc/nginx/sites-available/portfolio
   ```

5. **Setup Gunicorn service**
   ```bash
   sudo nano /etc/systemd/system/portfolio.service
   ```

## 📊 Current Content

- **7 Projects** - Various web apps, ML projects, and mobile apps
- **31 Skills** - Programming languages, frameworks, tools, and technologies
- **5 Experiences** - Work experience, internships, and education
- **4 Testimonials** - Client feedback and recommendations
- **0 Contacts** - Contact form submissions

## 🔧 Management Commands

- `python manage.py add_sample_content` - Add comprehensive sample data
- `python manage.py collectstatic` - Collect static files for production
- `python manage.py createsuperuser` - Create admin user

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Contact

**Bikal Sharma Pokharel**
- Email: pokharelbikalsharma@gmail.com
- GitHub: [bikalpokharel](https://github.com/bikalpokharel)
- LinkedIn: [bikal-pokharel](https://www.linkedin.com/in/bikal-pokharel-1b69442a1/)
- Phone: +977 9864546508

---

**Ready for deployment!** 🚀
