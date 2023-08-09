from django.urls import path
from . import views

app_name='home'
urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('about-us',views.about_us,name='about_us'),
    path('our-projects',views.our_projects,name='our_projects'),
    path('projects-list',views.projects_list,name='projects_list'),     
    path('projects-single/<int:project_id>',views.projects_single,name='projects_single'),    
    path('testimonials',views.testimonials,name='testimonials'),
    path('faq',views.faq,name='faq'),
    path('news',views.news,name='news'),
    path('contact',views.contact,name='contact'),                        
]
