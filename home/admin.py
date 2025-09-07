from django.contrib import admin
from django.utils.html import format_html
from .models import *

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            'fields': ('site_name', 'tagline', 'bio', 'profile_image', 'years_experience')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url')
        }),
        ('Files', {
            'fields': ('resume',)
        }),
    )
    
    def has_add_permission(self, request):
        return not SiteConfiguration.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'level', 'is_featured', 'order']
    list_filter = ['category', 'proficiency', 'is_featured']
    list_editable = ['level', 'is_featured', 'order']
    search_fields = ['name']
    ordering = ['category', 'order']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_type', 'status', 'is_featured', 'created_at']
    list_filter = ['project_type', 'status', 'is_featured', 'created_at']
    list_editable = ['is_featured', 'status']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['technologies']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'detailed_description', 'image')
        }),
        ('Project Details', {
            'fields': ('project_type', 'status', 'technologies')
        }),
        ('Links', {
            'fields': ('github_url', 'demo_url')
        }),
        ('Display Options', {
            'fields': ('is_featured', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'experience_type', 'start_date', 'end_date', 'is_current']
    list_filter = ['experience_type', 'is_current', 'start_date']
    list_editable = ['is_current']
    search_fields = ['title', 'company', 'description']
    filter_horizontal = ['skills_gained']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'rating', 'is_active', 'created_at']
    list_filter = ['rating', 'is_active', 'created_at']
    list_editable = ['is_active', 'rating']
    search_fields = ['name', 'company', 'content']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published', 'created_at', 'updated_at']
    list_filter = ['is_published', 'created_at']
    list_editable = ['is_published']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    list_editable = ['is_read']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    
    def has_add_permission(self, request):
        return False