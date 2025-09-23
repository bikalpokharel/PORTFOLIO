from django.urls import path
from . import views
from . import webhooks

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
    path('webhook/github/', webhooks.github_webhook, name='github_webhook'),
]