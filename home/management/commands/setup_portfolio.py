from django.core.management.base import BaseCommand
from home.models import *

class Command(BaseCommand):
    help = 'Setup initial portfolio data'
    
    def handle(self, *args, **options):
        self.stdout.write('Setting up portfolio data...')
        
        # Create site configuration
        config, created = SiteConfiguration.objects.get_or_create(
            pk=1,
            defaults={
                'site_name': 'Bikal Sharma Pokharel',
                'tagline': 'Aspiring Data Scientist | AI/ML Enthusiast | Backend Developer',
                'bio': '''Hi, I'm Bikal Sharma Pokharel - an aspiring Data Scientist, AI/ML enthusiast, and Backend Developer. 
                         Currently pursuing my BSc in Computer Science, I'm passionate about creating innovative solutions that 
                         bridge the gap between technology and real-world problems.''',
                'email': 'pokharelbikalsharma@gmail.com',
                'location': 'Nepal',
                'years_experience': 2,
                'github_url': 'https://github.com/yourusername',
                'linkedin_url': 'https://linkedin.com/in/yourusername',
            }
        )
        
        # Create skills
        skills_data = [
            # Programming Languages
            {'name': 'Python', 'category': 'programming', 'proficiency': 'expert', 'level': 95, 'icon': 'fab fa-python'},
            {'name': 'JavaScript', 'category': 'programming', 'proficiency': 'advanced', 'level': 85, 'icon': 'fab fa-js'},
            {'name': 'PHP', 'category': 'programming', 'proficiency': 'intermediate', 'level': 75, 'icon': 'fab fa-php'},
            {'name': 'SQL', 'category': 'programming', 'proficiency': 'advanced', 'level': 80, 'icon': 'fas fa-database'},
            
            # Frameworks
            {'name': 'Django', 'category': 'frameworks', 'proficiency': 'expert', 'level': 90, 'icon': 'fab fa-python'},
            {'name': 'React', 'category': 'frameworks', 'proficiency': 'intermediate', 'level': 70, 'icon': 'fab fa-react'},
            {'name': 'Flask', 'category': 'frameworks', 'proficiency': 'intermediate', 'level': 75, 'icon': 'fab fa-python'},
            {'name': 'Bootstrap', 'category': 'frameworks', 'proficiency': 'advanced', 'level': 85, 'icon': 'fab fa-bootstrap'},
            
            # Databases
            {'name': 'PostgreSQL', 'category': 'databases', 'proficiency': 'advanced', 'level': 80, 'icon': 'fas fa-database'},
            {'name': 'MySQL', 'category': 'databases', 'proficiency': 'advanced', 'level': 78, 'icon': 'fas fa-database'},
            {'name': 'SQLite', 'category': 'databases', 'proficiency': 'advanced', 'level': 85, 'icon': 'fas fa-database'},
            {'name': 'MongoDB', 'category': 'databases', 'proficiency': 'intermediate', 'level': 65, 'icon': 'fas fa-leaf'},
            
            # Tools
            {'name': 'Git', 'category': 'tools', 'proficiency': 'advanced', 'level': 85, 'icon': 'fab fa-git-alt'},
            {'name': 'Docker', 'category': 'tools', 'proficiency': 'intermediate', 'level': 70, 'icon': 'fab fa-docker'},
            {'name': 'Jupyter Notebook', 'category': 'tools', 'proficiency': 'advanced', 'level': 88, 'icon': 'fas fa-book'},
            {'name': 'VS Code', 'category': 'tools', 'proficiency': 'expert', 'level': 95, 'icon': 'fas fa-code'},
            
            # Cloud
            {'name': 'AWS', 'category': 'cloud', 'proficiency': 'intermediate', 'level': 65, 'icon': 'fab fa-aws'},
            {'name': 'Heroku', 'category': 'cloud', 'proficiency': 'intermediate', 'level': 70, 'icon': 'fas fa-cloud'},
            {'name': 'DigitalOcean', 'category': 'cloud', 'proficiency': 'intermediate', 'level': 68, 'icon': 'fab fa-digital-ocean'},
            
            # Other
            {'name': 'Machine Learning', 'category': 'other', 'proficiency': 'advanced', 'level': 82, 'icon': 'fas fa-brain'},
            {'name': 'Digital Marketing', 'category': 'other', 'proficiency': 'intermediate', 'level': 75, 'icon': 'fas fa-bullhorn'},
            {'name': 'Canva', 'category': 'other', 'proficiency': 'intermediate', 'level': 70, 'icon': 'fas fa-palette'},
        ]
        
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'Created skill: {skill.name}')
        
        # Create sample projects
        projects_data = [
            {
                'title': 'Portfolio Website',
                'slug': 'portfolio-website',
                'description': 'A modern, responsive portfolio website built with Django and Bootstrap, showcasing my skills, projects, and achievements.',
                'detailed_description': 'This portfolio website demonstrates my full-stack development capabilities using Django for the backend and modern CSS/JavaScript for the frontend. Features include project showcase, contact forms, admin panel, and responsive design.',
                'project_type': 'web_app',
                'status': 'completed',
                'github_url': 'https://github.com/yourusername/portfolio',
                'demo_url': 'https://yourportfolio.com',
                'is_featured': True,
            },
            {
                'title': 'School Management System',
                'slug': 'school-management-php',
                'description': 'A comprehensive school management platform built with PHP and MySQL for managing students, teachers, and administrative tasks.',
                'project_type': 'web_app',
                'status': 'in_progress',
                'github_url': 'https://github.com/yourusername/school-management',
                'is_featured': True,
            },
            {
                'title': 'Travel Assistant AI',
                'slug': 'travel-assistant-ai',
                'description': 'AI-powered travel companion that helps users book hotels, discover hidden gems, and find local food experiences.',
                'project_type': 'ai_project',
                'status': 'in_progress',
                'github_url': 'https://github.com/yourusername/travel-ai',
                'is_featured': True,
            },
            {
                'title': 'ML Pipeline Notebook',
                'slug': 'ml-pipeline-notebook',
                'description': 'End-to-end machine learning workflows for data preprocessing, training, and deployment using Jupyter Notebook.',
                'project_type': 'ml_project',
                'status': 'completed',
                'github_url': 'https://github.com/yourusername/ml-pipeline',
                'is_featured': True,
            }
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                slug=project_data['slug'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'Created project: {project.title}')
                # Add some technologies to the project
                if project.title == 'Portfolio Website':
                    project.technologies.add(
                        Skill.objects.get(name='Django'),
                        Skill.objects.get(name='Python'),
                        Skill.objects.get(name='Bootstrap'),
                        Skill.objects.get(name='JavaScript')
                    )
                elif 'School' in project.title:
                    project.technologies.add(
                        Skill.objects.get(name='PHP'),
                        Skill.objects.get(name='MySQL'),
                        Skill.objects.get(name='Bootstrap')
                    )
                elif 'Travel' in project.title:
                    project.technologies.add(
                        Skill.objects.get(name='Python'),
                        Skill.objects.get(name='Machine Learning'),
                        Skill.objects.get(name='Flask')
                    )
                elif 'ML Pipeline' in project.title:
                    project.technologies.add(
                        Skill.objects.get(name='Python'),
                        Skill.objects.get(name='Machine Learning'),
                        Skill.objects.get(name='Jupyter Notebook')
                    )
        
        # Create sample experience
        experience_data = [
            {
                'title': 'Computer Science Student',
                'company': 'University/College Name',
                'experience_type': 'education',
                'start_date': '2022-01-01',
                'is_current': True,
                'description': 'Currently pursuing BSc in Computer Science with focus on software development, machine learning, and data structures.',
                'location': 'Nepal'
            },
            {
                'title': 'Freelance Web Developer',
                'company': 'Self-Employed',
                'experience_type': 'freelance',
                'start_date': '2023-06-01',
                'is_current': True,
                'description': 'Developing custom web applications for clients using Django, React, and modern web technologies.',
                'location': 'Remote'
            }
        ]
        
        for exp_data in experience_data:
            exp, created = Experience.objects.get_or_create(
                title=exp_data['title'],
                company=exp_data['company'],
                defaults=exp_data
            )
            if created:
                self.stdout.write(f'Created experience: {exp.title}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully set up portfolio data!')
        )