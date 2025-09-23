from django.core.management.base import BaseCommand
from home.models import Project
import requests
import json
from datetime import datetime

class Command(BaseCommand):
    help = 'Sync projects from GitHub repositories'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default='bikalpokharel',
            help='GitHub username to fetch repositories from'
        )
        parser.add_argument(
            '--token',
            type=str,
            help='GitHub personal access token (optional, for private repos)'
        )
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force update existing projects'
        )
    
    def handle(self, *args, **options):
        username = options['username']
        token = options['token']
        force = options['force']
        
        self.stdout.write(f'Syncing projects from GitHub user: {username}')
        
        # GitHub API endpoint
        url = f'https://api.github.com/users/{username}/repos'
        headers = {}
        
        if token:
            headers['Authorization'] = f'token {token}'
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            repos = response.json()
            
            self.stdout.write(f'Found {len(repos)} repositories')
            
            # Filter repositories (exclude forks, archived, etc.)
            relevant_repos = []
            for repo in repos:
                if (not repo['fork'] and 
                    not repo['archived'] and 
                    not repo['private'] and
                    repo['name'] not in ['bikalpokharel', 'PORTFOLIO']):  # Exclude portfolio repo itself
                    relevant_repos.append(repo)
            
            self.stdout.write(f'Found {len(relevant_repos)} relevant repositories')
            
            # Process each repository
            for repo in relevant_repos:
                self.process_repository(repo, force)
                
        except requests.exceptions.RequestException as e:
            self.stdout.write(
                self.style.ERROR(f'Error fetching repositories: {e}')
            )
            return
        
        self.stdout.write(
            self.style.SUCCESS('Successfully synced projects from GitHub!')
        )
    
    def process_repository(self, repo, force=False):
        """Process a single GitHub repository"""
        repo_name = repo['name']
        repo_url = repo['html_url']
        description = repo['description'] or f'A {repo["language"] or "software"} project'
        
        # Determine project type based on language and description
        project_type = self.determine_project_type(repo['language'], description)
        
        # Create slug from repository name
        slug = repo_name.lower().replace('_', '-').replace(' ', '-')
        
        # Check if project already exists
        existing_project = Project.objects.filter(slug=slug).first()
        
        if existing_project and not force:
            self.stdout.write(f'Project {repo_name} already exists, skipping...')
            return
        
        # Prepare project data
        project_data = {
            'title': self.format_title(repo_name),
            'slug': slug,
            'description': description,
            'detailed_description': self.create_detailed_description(repo),
            'project_type': project_type,
            'status': 'completed' if not repo['archived'] else 'completed',
            'github_url': repo_url,
            'demo_url': '',  # You can add demo URLs manually later
            'is_featured': True,
            'order': 0,
        }
        
        if existing_project:
            # Update existing project
            for key, value in project_data.items():
                setattr(existing_project, key, value)
            existing_project.save()
            self.stdout.write(f'Updated project: {repo_name}')
        else:
            # Create new project
            Project.objects.create(**project_data)
            self.stdout.write(f'Created new project: {repo_name}')
    
    def determine_project_type(self, language, description):
        """Determine project type based on language and description"""
        description_lower = description.lower()
        
        if any(word in description_lower for word in ['web', 'website', 'app', 'django', 'flask', 'react', 'vue', 'angular']):
            return 'web_app'
        elif any(word in description_lower for word in ['ml', 'machine learning', 'ai', 'artificial intelligence', 'data science', 'tensorflow', 'pytorch']):
            return 'ml_project'
        elif any(word in description_lower for word in ['mobile', 'android', 'ios', 'react native', 'flutter']):
            return 'mobile_app'
        elif any(word in description_lower for word in ['ai', 'artificial intelligence', 'chatbot', 'nlp']):
            return 'ai_project'
        elif any(word in description_lower for word in ['data', 'analysis', 'visualization', 'pandas', 'numpy']):
            return 'data_science'
        else:
            return 'other'
    
    def format_title(self, repo_name):
        """Format repository name into a proper title"""
        # Replace underscores and hyphens with spaces
        title = repo_name.replace('_', ' ').replace('-', ' ')
        # Capitalize each word
        title = ' '.join(word.capitalize() for word in title.split())
        return title
    
    def create_detailed_description(self, repo):
        """Create a detailed description for the project"""
        language = repo['language'] or 'Various'
        stars = repo['stargazers_count']
        forks = repo['forks_count']
        created = datetime.strptime(repo['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%B %Y')
        updated = datetime.strptime(repo['updated_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%B %Y')
        
        description = f'''A {language} project created in {created} and last updated in {updated}.

Repository Statistics:
• ⭐ {stars} stars
• 🍴 {forks} forks
• 📅 Created: {created}
• 🔄 Last updated: {updated}

Technologies: {language}

{repo['description'] or 'A software development project showcasing various programming concepts and best practices.'}

Visit the GitHub repository for more details, documentation, and source code.'''
        
        return description
