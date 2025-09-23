from django.core.management.base import BaseCommand
from home.models import Project

class Command(BaseCommand):
    help = 'Update projects to keep only real ones with authentic links'
    
    def handle(self, *args, **options):
        self.stdout.write('Updating projects to keep only real ones...')
        
        # Keep only real projects with authentic GitHub links
        real_projects = [
            {
                'title': 'Portfolio Website',
                'slug': 'portfolio-website',
                'description': 'A modern, responsive portfolio website built with Django and Bootstrap, showcasing my skills, projects, and achievements with a beautiful dark theme.',
                'detailed_description': '''This portfolio website demonstrates my full-stack development capabilities using Django for the backend and modern CSS/JavaScript for the frontend. 

Features include:
• Responsive design with dark theme
• Project showcase with filtering and search
• Contact form with email integration
• Admin panel for content management
• SEO optimization
• Performance optimization with static file serving
• Modern animations and interactions

The website is built with Django 4.2, Bootstrap 5, and custom CSS with a focus on user experience and performance.''',
                'project_type': 'web_app',
                'status': 'completed',
                'github_url': 'https://github.com/bikalpokharel/PORTFOLIO',
                'demo_url': '',  # Add your live demo URL here if you have one
                'is_featured': True,
                'order': 1,
            },
            {
                'title': 'School Management System',
                'slug': 'school-management-php',
                'description': 'A comprehensive school management platform built with PHP and MySQL for managing students, teachers, and administrative tasks.',
                'detailed_description': '''A complete school management system that handles all aspects of school administration.

Key Features:
• Student enrollment and management
• Teacher and staff management
• Course and subject management
• Grade and attendance tracking
• Fee management system
• Report generation
• User role-based access control
• Responsive web interface

Built with PHP 7.4, MySQL, Bootstrap, and jQuery for a robust and user-friendly experience.''',
                'project_type': 'web_app',
                'status': 'in_progress',
                'github_url': 'https://github.com/bikalpokharel/School-website-',
                'demo_url': '',  # Add your live demo URL here if you have one
                'is_featured': True,
                'order': 2,
            },
            {
                'title': 'Travel Assistant AI',
                'slug': 'travel-assistant-ai',
                'description': 'AI-powered travel companion that helps users book hotels, discover hidden gems, and find local food experiences using machine learning.',
                'detailed_description': '''An intelligent travel assistant that uses AI to provide personalized travel recommendations.

Features:
• Hotel booking with price comparison
• Local attraction recommendations
• Restaurant and food suggestions
• Weather integration
• Budget planning
• Itinerary generation
• Multi-language support
• Mobile-responsive design

Technologies: Python, Django, TensorFlow, Scikit-learn, React Native, and various travel APIs.''',
                'project_type': 'ai_project',
                'status': 'in_progress',
                'github_url': 'https://github.com/bikalpokharel/travel-assistant-pro-v1',
                'demo_url': '',  # Add your live demo URL here if you have one
                'is_featured': True,
                'order': 3,
            },
            {
                'title': 'ML Pipeline Notebook',
                'slug': 'ml-pipeline-notebook',
                'description': 'Machine learning pipeline notebook for data preprocessing, model training, and evaluation with various algorithms.',
                'detailed_description': '''A comprehensive machine learning pipeline that demonstrates data science workflows.

Features:
• Data preprocessing and cleaning
• Feature engineering
• Multiple ML algorithms (Random Forest, SVM, Neural Networks)
• Model evaluation and comparison
• Cross-validation techniques
• Hyperparameter tuning
• Data visualization
• Jupyter notebook format

Technologies: Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Jupyter.''',
                'project_type': 'ml_project',
                'status': 'completed',
                'github_url': 'https://github.com/bikalpokharel/ML_Pipeline',
                'demo_url': '',  # Add your live demo URL here if you have one
                'is_featured': True,
                'order': 4,
            },
        ]
        
        # Remove all existing projects
        Project.objects.all().delete()
        self.stdout.write('Removed all existing projects')
        
        # Add only real projects
        for project_data in real_projects:
            project = Project.objects.create(**project_data)
            self.stdout.write(f'Created real project: {project.title}')
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully updated projects! Now showing {len(real_projects)} real projects with authentic links.')
        )
