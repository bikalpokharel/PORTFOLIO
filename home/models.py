from django.db import models
from django.urls import reverse
from PIL import Image
import os

class Skill(models.Model):
    SKILL_CATEGORIES = [
        ('programming', 'Programming Languages'),
        ('frameworks', 'Frameworks & Libraries'),
        ('databases', 'Databases'),
        ('tools', 'Tools & Technologies'),
        ('cloud', 'Cloud & DevOps'),
        ('other', 'Other Skills'),
    ]
    
    PROFICIENCY_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES, default='other')
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_LEVELS, default='intermediate')
    level = models.IntegerField(default=50, help_text="Skill level percentage (0-100)")
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class")
    is_featured = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_proficiency_display()})"

class Project(models.Model):
    PROJECT_STATUS = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('planning', 'Planning'),
        ('on_hold', 'On Hold'),
    ]
    
    PROJECT_TYPES = [
        ('web_app', 'Web Application'),
        ('ml_project', 'Machine Learning'),
        ('mobile_app', 'Mobile App'),
        ('ai_project', 'AI Project'),
        ('data_science', 'Data Science'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    detailed_description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES, default='web_app')
    status = models.CharField(max_length=20, choices=PROJECT_STATUS, default='completed')
    technologies = models.ManyToManyField(Skill, blank=True)
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-is_featured', 'order', '-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 600 or img.width > 800:
                output_size = (800, 600)
                img.thumbnail(output_size)
                img.save(self.image.path)

class Experience(models.Model):
    EXPERIENCE_TYPES = [
        ('work', 'Work Experience'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance'),
        ('volunteer', 'Volunteer'),
        ('education', 'Education'),
    ]
    
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    experience_type = models.CharField(max_length=20, choices=EXPERIENCE_TYPES, default='work')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    skills_gained = models.ManyToManyField(Skill, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-start_date', 'order']
    
    def __str__(self):
        return f"{self.title} at {self.company}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating = models.IntegerField(default=5, help_text="Rating out of 5")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return f"Testimonial from {self.name}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

class SiteConfiguration(models.Model):
    site_name = models.CharField(max_length=100, default="Bikal Sharma Pokharel")
    tagline = models.CharField(max_length=200, default="Aspiring Data Scientist | AI/ML Enthusiast | Backend Developer")
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='files/', blank=True, null=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    email = models.EmailField(default="pokharelbikalsharma@gmail.com")
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, default="Nepal")
    years_experience = models.IntegerField(default=2)
    
    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"
    
    def __str__(self):
        return self.site_name
    
    def save(self, *args, **kwargs):
        if not self.pk and SiteConfiguration.objects.exists():
            raise ValueError('There can be only one SiteConfiguration instance')
        return super().save(*args, **kwargs)