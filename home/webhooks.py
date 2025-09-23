from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
import json
import hmac
import hashlib
from home.models import Project
from datetime import datetime

@csrf_exempt
@require_POST
def github_webhook(request):
    """
    GitHub webhook handler to automatically add new repositories to portfolio
    """
    # Verify webhook signature (optional but recommended)
    if hasattr(settings, 'GITHUB_WEBHOOK_SECRET'):
        signature = request.META.get('HTTP_X_HUB_SIGNATURE_256', '')
        if not verify_webhook_signature(request.body, signature, settings.GITHUB_WEBHOOK_SECRET):
            return HttpResponse('Unauthorized', status=401)
    
    try:
        payload = json.loads(request.body)
        event_type = request.META.get('HTTP_X_GITHUB_EVENT', '')
        
        if event_type == 'repository':
            handle_repository_event(payload)
        elif event_type == 'push':
            handle_push_event(payload)
            
    except json.JSONDecodeError:
        return HttpResponse('Invalid JSON', status=400)
    except Exception as e:
        return HttpResponse(f'Error: {str(e)}', status=500)
    
    return HttpResponse('OK', status=200)

def verify_webhook_signature(payload, signature, secret):
    """Verify GitHub webhook signature"""
    if not signature.startswith('sha256='):
        return False
    
    expected_signature = 'sha256=' + hmac.new(
        secret.encode('utf-8'),
        payload,
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(signature, expected_signature)

def handle_repository_event(payload):
    """Handle repository creation/update events"""
    action = payload.get('action')
    repo = payload.get('repository', {})
    
    if action in ['created', 'publicized']:
        add_repository_to_portfolio(repo)
    elif action == 'deleted':
        remove_repository_from_portfolio(repo)

def handle_push_event(payload):
    """Handle push events to update repository info"""
    repo = payload.get('repository', {})
    if repo:
        update_repository_info(repo)

def add_repository_to_portfolio(repo):
    """Add a new repository to the portfolio"""
    repo_name = repo['name']
    repo_url = repo['html_url']
    description = repo['description'] or f'A {repo["language"] or "software"} project'
    
    # Skip if it's a fork, private, or archived
    if repo.get('fork') or repo.get('private') or repo.get('archived'):
        return
    
    # Skip portfolio repo itself
    if repo_name in ['bikalpokharel', 'PORTFOLIO']:
        return
    
    # Create slug from repository name
    slug = repo_name.lower().replace('_', '-').replace(' ', '-')
    
    # Check if project already exists
    if Project.objects.filter(slug=slug).exists():
        return
    
    # Determine project type
    project_type = determine_project_type(repo['language'], description)
    
    # Create project
    project_data = {
        'title': format_title(repo_name),
        'slug': slug,
        'description': description,
        'detailed_description': create_detailed_description(repo),
        'project_type': project_type,
        'status': 'completed',
        'github_url': repo_url,
        'demo_url': '',
        'is_featured': True,
        'order': 0,
    }
    
    Project.objects.create(**project_data)

def remove_repository_from_portfolio(repo):
    """Remove a repository from the portfolio"""
    repo_name = repo['name']
    slug = repo_name.lower().replace('_', '-').replace(' ', '-')
    
    try:
        project = Project.objects.get(slug=slug)
        project.delete()
    except Project.DoesNotExist:
        pass

def update_repository_info(repo):
    """Update repository information in the portfolio"""
    repo_name = repo['name']
    slug = repo_name.lower().replace('_', '-').replace(' ', '-')
    
    try:
        project = Project.objects.get(slug=slug)
        project.description = repo['description'] or project.description
        project.detailed_description = create_detailed_description(repo)
        project.save()
    except Project.DoesNotExist:
        pass

def determine_project_type(language, description):
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

def format_title(repo_name):
    """Format repository name into a proper title"""
    title = repo_name.replace('_', ' ').replace('-', ' ')
    title = ' '.join(word.capitalize() for word in title.split())
    return title

def create_detailed_description(repo):
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
