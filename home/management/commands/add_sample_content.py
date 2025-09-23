from django.core.management.base import BaseCommand
from home.models import Skill, Project, Experience, Testimonial, SiteConfiguration
from django.utils import timezone
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Add comprehensive sample content to the portfolio'
    
    def handle(self, *args, **options):
        self.stdout.write('Adding sample content to portfolio...')
        
        # Update site configuration
        config, created = SiteConfiguration.objects.get_or_create(
            pk=1,
            defaults={
                'site_name': 'Bikal Sharma Pokharel',
                'tagline': 'Aspiring Data Scientist | AI/ML Enthusiast | Backend Developer',
                'bio': '''BSc Computer Science Student passionate about solving real-world problems 
                         through technology. Experienced in full-stack development, machine learning, 
                         and digital marketing. Currently pursuing my degree while working on innovative 
                         projects that make a difference.''',
                'email': 'pokharelbikalsharma@gmail.com',
                'phone': '+977 9864546508',
                'location': 'Kathmandu, Nepal',
                'years_experience': 2,
                'github_url': 'https://github.com/bikalpokharel',
                'linkedin_url': 'https://www.linkedin.com/in/bikal-pokharel-1b69442a1/',
            }
        )
        if not created:
            self.stdout.write('Updated site configuration')
        else:
            self.stdout.write('Created site configuration')
        
        # Add comprehensive skills
        skills_data = [
            # Programming Languages
            {'name': 'Python', 'category': 'programming', 'proficiency': 'expert', 'level': 90, 'icon': 'fab fa-python', 'is_featured': True, 'order': 1},
            {'name': 'JavaScript', 'category': 'programming', 'proficiency': 'advanced', 'level': 85, 'icon': 'fab fa-js-square', 'is_featured': True, 'order': 2},
            {'name': 'Java', 'category': 'programming', 'proficiency': 'intermediate', 'level': 70, 'icon': 'fab fa-java', 'is_featured': True, 'order': 3},
            {'name': 'C++', 'category': 'programming', 'proficiency': 'intermediate', 'level': 65, 'icon': 'fas fa-code', 'is_featured': False, 'order': 4},
            {'name': 'PHP', 'category': 'programming', 'proficiency': 'advanced', 'level': 80, 'icon': 'fab fa-php', 'is_featured': True, 'order': 5},
            
            # Frameworks & Libraries
            {'name': 'Django', 'category': 'frameworks', 'proficiency': 'expert', 'level': 95, 'icon': 'fab fa-python', 'is_featured': True, 'order': 1},
            {'name': 'React', 'category': 'frameworks', 'proficiency': 'advanced', 'level': 80, 'icon': 'fab fa-react', 'is_featured': True, 'order': 2},
            {'name': 'Bootstrap', 'category': 'frameworks', 'proficiency': 'expert', 'level': 90, 'icon': 'fab fa-bootstrap', 'is_featured': True, 'order': 3},
            {'name': 'Node.js', 'category': 'frameworks', 'proficiency': 'intermediate', 'level': 70, 'icon': 'fab fa-node-js', 'is_featured': True, 'order': 4},
            {'name': 'Flask', 'category': 'frameworks', 'proficiency': 'advanced', 'level': 75, 'icon': 'fas fa-flask', 'is_featured': False, 'order': 5},
            
            # Databases
            {'name': 'PostgreSQL', 'category': 'databases', 'proficiency': 'advanced', 'level': 85, 'icon': 'fas fa-database', 'is_featured': True, 'order': 1},
            {'name': 'MySQL', 'category': 'databases', 'proficiency': 'advanced', 'level': 80, 'icon': 'fas fa-database', 'is_featured': True, 'order': 2},
            {'name': 'SQLite', 'category': 'databases', 'proficiency': 'expert', 'level': 90, 'icon': 'fas fa-database', 'is_featured': False, 'order': 3},
            {'name': 'MongoDB', 'category': 'databases', 'proficiency': 'intermediate', 'level': 65, 'icon': 'fas fa-leaf', 'is_featured': False, 'order': 4},
            
            # Tools & Technologies
            {'name': 'Git', 'category': 'tools', 'proficiency': 'expert', 'level': 90, 'icon': 'fab fa-git-alt', 'is_featured': True, 'order': 1},
            {'name': 'Docker', 'category': 'tools', 'proficiency': 'intermediate', 'level': 70, 'icon': 'fab fa-docker', 'is_featured': True, 'order': 2},
            {'name': 'Linux', 'category': 'tools', 'proficiency': 'advanced', 'level': 80, 'icon': 'fab fa-linux', 'is_featured': True, 'order': 3},
            {'name': 'VS Code', 'category': 'tools', 'proficiency': 'expert', 'level': 95, 'icon': 'fas fa-code', 'is_featured': False, 'order': 4},
            {'name': 'Jupyter', 'category': 'tools', 'proficiency': 'advanced', 'level': 85, 'icon': 'fab fa-python', 'is_featured': True, 'order': 5},
            
            # Cloud & DevOps
            {'name': 'AWS', 'category': 'cloud', 'proficiency': 'intermediate', 'level': 60, 'icon': 'fab fa-aws', 'is_featured': True, 'order': 1},
            {'name': 'Heroku', 'category': 'cloud', 'proficiency': 'advanced', 'level': 75, 'icon': 'fas fa-cloud', 'is_featured': True, 'order': 2},
            {'name': 'DigitalOcean', 'category': 'cloud', 'proficiency': 'intermediate', 'level': 65, 'icon': 'fas fa-cloud', 'is_featured': False, 'order': 3},
            
            # AI/ML
            {'name': 'TensorFlow', 'category': 'other', 'proficiency': 'intermediate', 'level': 70, 'icon': 'fas fa-brain', 'is_featured': True, 'order': 1},
            {'name': 'Scikit-learn', 'category': 'other', 'proficiency': 'advanced', 'level': 80, 'icon': 'fas fa-chart-line', 'is_featured': True, 'order': 2},
            {'name': 'Pandas', 'category': 'other', 'proficiency': 'expert', 'level': 90, 'icon': 'fas fa-table', 'is_featured': True, 'order': 3},
            {'name': 'NumPy', 'category': 'other', 'proficiency': 'advanced', 'level': 85, 'icon': 'fas fa-calculator', 'is_featured': True, 'order': 4},
        ]
        
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'Created skill: {skill.name}')
        
        # Add comprehensive projects
        projects_data = [
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
                'github_url': 'https://github.com/bikalpokharel/portfolio',
                'demo_url': 'https://bikalpokharel.com',
                'is_featured': True,
                'order': 1,
            },
            {
                'title': 'School Management System',
                'slug': 'school-management-php',
                'description': 'A comprehensive school management platform built with PHP and MySQL for managing students, teachers, courses, and administrative tasks.',
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
                'github_url': 'https://github.com/bikalpokharel/school-management',
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
                'github_url': 'https://github.com/bikalpokharel/travel-ai',
                'is_featured': True,
                'order': 3,
            },
            {
                'title': 'E-commerce Analytics Dashboard',
                'slug': 'ecommerce-analytics-dashboard',
                'description': 'A comprehensive analytics dashboard for e-commerce businesses with real-time data visualization and business intelligence features.',
                'detailed_description': '''A powerful analytics platform that provides deep insights into e-commerce performance.

Key Features:
• Real-time sales analytics
• Customer behavior tracking
• Inventory management
• Revenue forecasting
• Interactive data visualizations
• Custom report generation
• API integrations
• Automated alerts

Built with Python, Django, React, Chart.js, and PostgreSQL for handling large datasets efficiently.''',
                'project_type': 'data_science',
                'status': 'completed',
                'github_url': 'https://github.com/bikalpokharel/ecommerce-analytics',
                'demo_url': 'https://analytics-demo.bikalpokharel.com',
                'is_featured': True,
                'order': 4,
            },
            {
                'title': 'Weather Prediction ML Model',
                'slug': 'weather-prediction-ml',
                'description': 'Machine learning model for weather prediction using historical data and various algorithms for accurate forecasting.',
                'detailed_description': '''A sophisticated weather prediction system using multiple ML algorithms.

Features:
• Historical weather data analysis
• Multiple prediction algorithms (Random Forest, LSTM, ARIMA)
• Real-time data integration
• Accuracy comparison between models
• API for weather predictions
• Web interface for visualization
• Mobile app integration

Technologies: Python, Scikit-learn, TensorFlow, Pandas, NumPy, Django REST Framework.''',
                'project_type': 'ml_project',
                'status': 'completed',
                'github_url': 'https://github.com/bikalpokharel/weather-prediction',
                'is_featured': True,
                'order': 5,
            },
            {
                'title': 'Task Management Mobile App',
                'slug': 'task-management-mobile',
                'description': 'Cross-platform mobile application for task management with team collaboration features and real-time synchronization.',
                'detailed_description': '''A feature-rich task management app for individuals and teams.

Key Features:
• Task creation and management
• Team collaboration
• Real-time synchronization
• File attachments
• Due date reminders
• Progress tracking
• Offline functionality
• Push notifications

Built with React Native, Node.js, MongoDB, and Socket.io for real-time features.''',
                'project_type': 'mobile_app',
                'status': 'in_progress',
                'github_url': 'https://github.com/bikalpokharel/task-manager',
                'is_featured': False,
                'order': 6,
            },
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                slug=project_data['slug'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'Created project: {project.title}')
        
        # Add work experience
        experiences_data = [
            {
                'title': 'Full-Stack Developer',
                'company': 'Tech Solutions Nepal',
                'location': 'Kathmandu, Nepal',
                'experience_type': 'work',
                'start_date': date(2023, 6, 1),
                'end_date': None,
                'is_current': True,
                'description': '''Working as a full-stack developer on various web applications and mobile projects. 
                
Responsibilities include:
• Developing responsive web applications using Django and React
• Building RESTful APIs and integrating third-party services
• Database design and optimization
• Code review and mentoring junior developers
• Client communication and project management
• Implementing CI/CD pipelines''',
                'order': 1,
            },
            {
                'title': 'Data Science Intern',
                'company': 'AI Research Lab',
                'location': 'Kathmandu, Nepal',
                'experience_type': 'internship',
                'start_date': date(2023, 1, 1),
                'end_date': date(2023, 5, 31),
                'is_current': False,
                'description': '''Internship focused on machine learning and data analysis projects.

Key achievements:
• Developed predictive models for business analytics
• Worked with large datasets using Python and SQL
• Created data visualizations and reports
• Collaborated with research team on AI projects
• Gained experience with TensorFlow and Scikit-learn''',
                'order': 2,
            },
            {
                'title': 'Freelance Web Developer',
                'company': 'Self-Employed',
                'location': 'Remote',
                'experience_type': 'freelance',
                'start_date': date(2022, 9, 1),
                'end_date': date(2023, 12, 31),
                'is_current': False,
                'description': '''Provided web development services to various clients.

Services offered:
• Custom website development
• E-commerce solutions
• Database design and implementation
• Website maintenance and updates
• SEO optimization
• Client training and support''',
                'order': 3,
            },
            {
                'title': 'BSc Computer Science',
                'company': 'Tribhuvan University',
                'location': 'Kathmandu, Nepal',
                'experience_type': 'education',
                'start_date': date(2021, 9, 1),
                'end_date': date(2025, 6, 30),
                'is_current': True,
                'description': '''Pursuing Bachelor of Science in Computer Science with focus on software engineering and data science.

Relevant coursework:
• Data Structures and Algorithms
• Database Management Systems
• Software Engineering
• Machine Learning
• Web Development
• Computer Networks
• Operating Systems''',
                'order': 4,
            },
        ]
        
        for exp_data in experiences_data:
            experience, created = Experience.objects.get_or_create(
                title=exp_data['title'],
                company=exp_data['company'],
                defaults=exp_data
            )
            if created:
                self.stdout.write(f'Created experience: {experience.title} at {experience.company}')
        
        # Add testimonials
        testimonials_data = [
            {
                'name': 'Sarah Johnson',
                'position': 'Project Manager',
                'company': 'TechCorp Solutions',
                'content': '''Bikal delivered an exceptional e-commerce platform for our business. His attention to detail, 
                technical expertise, and ability to understand our requirements made the project a huge success. 
                The website is fast, user-friendly, and has significantly improved our online sales.''',
                'rating': 5,
                'is_active': True,
                'order': 1,
            },
            {
                'name': 'Dr. Rajesh Kumar',
                'position': 'Research Director',
                'company': 'AI Research Lab',
                'content': '''Working with Bikal during his internship was a pleasure. He showed great initiative in 
                learning new technologies and contributed significantly to our machine learning projects. 
                His analytical thinking and problem-solving skills are impressive.''',
                'rating': 5,
                'is_active': True,
                'order': 2,
            },
            {
                'name': 'Michael Chen',
                'position': 'Startup Founder',
                'company': 'InnovateTech',
                'content': '''Bikal helped us build our MVP from scratch. His full-stack development skills and 
                understanding of modern web technologies were crucial to our success. He's reliable, 
                professional, and always delivers quality work on time.''',
                'rating': 5,
                'is_active': True,
                'order': 3,
            },
            {
                'name': 'Priya Sharma',
                'position': 'Marketing Director',
                'company': 'Digital Marketing Agency',
                'content': '''The analytics dashboard Bikal created for us has revolutionized how we track our 
                marketing campaigns. The insights we get are invaluable, and the interface is intuitive. 
                Highly recommend his services!''',
                'rating': 5,
                'is_active': True,
                'order': 4,
            },
        ]
        
        for testimonial_data in testimonials_data:
            testimonial, created = Testimonial.objects.get_or_create(
                name=testimonial_data['name'],
                company=testimonial_data['company'],
                defaults=testimonial_data
            )
            if created:
                self.stdout.write(f'Created testimonial from: {testimonial.name}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully added comprehensive sample content to the portfolio!')
        )
