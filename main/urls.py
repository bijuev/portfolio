from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),     
    path('portfolio/', views.portfolio, name='portfolio'), 
    path('resume/', views.resume, name='resume'),  
    path('services/', views.services, name='services'), 
    path('contact/', views.contact, name='contact'), 
    path('projects/', views.projects, name='projects'), 
    path('', views.home, name='home'),           
]
