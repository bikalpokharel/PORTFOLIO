from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.core.paginator import Paginator
from .models import *
import logging

logger = logging.getLogger(__name__)

def get_site_config():
    """Get or create site configuration"""
    config, created = SiteConfiguration.objects.get_or_create(
        pk=1,
        defaults={
            'site_name': 'Bikal Sharma Pokharel',
            'tagline': 'Aspiring Data Scientist | AI/ML Enthusiast | Backend Developer',
            'bio': '''BSc Computer Science Student passionate about solving real-world problems 
                     through technology. Experienced in full-stack development, machine learning, 
                     and digital marketing.''',
            'email': 'pokharelbikalsharma@gmail.com',
            'location': 'Nepal',
            'years_experience': 2
        }
    )
    return config

def home(request):
    """Home page view"""
    config = get_site_config()
    featured_projects = Project.objects.filter(is_featured=True)[:6]
    skills = Skill.objects.filter(is_featured=True)
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    
    # Categorize skills
    skill_categories = {
        'programming': skills.filter(category='programming'),
        'frameworks': skills.filter(category='frameworks'),
        'tools': skills.filter(category='tools'),
        'cloud': skills.filter(category='cloud'),
    }
    
    context = {
        'config': config,
        'projects': featured_projects,
        'skills': skills,
        'skill_categories': skill_categories,
        'testimonials': testimonials,
        'page_title': 'Home'
    }
    return render(request, 'home/index.html', context)

def about(request):
    """About page view"""
    config = get_site_config()
    all_skills = Skill.objects.all()
    experiences = Experience.objects.all()
    
    # Categorize skills for about page
    skill_categories = {
        'Programming Languages': all_skills.filter(category='programming'),
        'Frameworks & Libraries': all_skills.filter(category='frameworks'),
        'Databases': all_skills.filter(category='databases'),
        'Tools & Technologies': all_skills.filter(category='tools'),
        'Cloud & DevOps': all_skills.filter(category='cloud'),
        'Other Skills': all_skills.filter(category='other'),
    }
    
    context = {
        'config': config,
        'skill_categories': skill_categories,
        'experiences': experiences,
        'page_title': 'About Me'
    }
    return render(request, 'home/about.html', context)

def projects(request):
    """Projects page view"""
    config = get_site_config()
    all_projects = Project.objects.all()
    
    # Filter by type if specified
    project_type = request.GET.get('type')
    if project_type:
        all_projects = all_projects.filter(project_type=project_type)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        all_projects = all_projects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(technologies__name__icontains=search_query)
        ).distinct()
    
    # Pagination
    paginator = Paginator(all_projects, 9)
    page_number = request.GET.get('page')
    projects_page = paginator.get_page(page_number)
    
    # Get project types for filter
    project_types = Project.PROJECT_TYPES
    
    context = {
        'config': config,
        'projects': projects_page,
        'project_types': project_types,
        'current_type': project_type,
        'search_query': search_query,
        'page_title': 'Projects'
    }
    return render(request, 'home/projects.html', context)

def project_detail(request, slug):
    """Project detail view"""
    config = get_site_config()
    project = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.filter(
        project_type=project.project_type
    ).exclude(id=project.id)[:3]
    
    context = {
        'config': config,
        'project': project,
        'related_projects': related_projects,
        'page_title': project.title
    }
    return render(request, 'home/project_detail.html', context)


def contact(request):
    """Contact page view"""
    config = get_site_config()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            # Save to database
            contact_obj = Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            # Send email notification
            try:
                full_message = f"""
New contact form submission:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
"""
                send_mail(
                    subject=f'Portfolio Contact: {subject}',
                    message=full_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[config.email],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
                logger.info(f'Contact form submitted by {email}')
            except Exception as e:
                messages.success(request, 'Message saved! I\'ll get back to you soon.')
                logger.error(f'Email sending failed: {str(e)}')
            
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    context = {
        'config': config,
        'page_title': 'Contact'
    }
    return render(request, 'home/contact.html', context)