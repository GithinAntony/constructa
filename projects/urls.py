from django.urls import path
from . import views

app_name='projects'
urlpatterns = [
    path('services',views.services,name='services'),  
    path('services-single/<int:service_id>',views.services_single,name='services_single'),
    path('service-message-list', views.services_message_list, name='service_message_list'),    
    path('service-message/<int:service_id>',views.services_message,name='services_message'), 
    path('chat-message/<int:msg_id>',views.chat_message,name='chat_message'),
    path('chat-message-particpants/<int:msg_id>/<int:user_type>',views.chat_message_particpants,name='chat_message_particpants'),
    path('chat-message-particpant-delete/<int:particpant_id>/<int:msg_id>',views.chat_message_particpant_delete,name='chat_message_particpant_delete'),
    path('projects-add/<int:msg_id>',views.projects_add,name='projects_add'),     
    path('projects-edit/<int:project_id>/<int:msg_id>',views.projects_edit,name='projects_edit'), 
    path('projects-delete/<int:project_id>/<int:msg_id>',views.projects_delete,name='projects_delete'),     
    path('projects-images/<int:project_id>/<int:msg_id>',views.projects_images,name='projects_images'),   
    path('projects-images-delete/<int:image_id>/<int:project_id>/<int:msg_id>',views.projects_images_delete, name='projects_images_delete'),
    path('projects-list',views.projects_list,name='projects_list'), 
    path('projects-single/<int:project_id>',views.projects_single,name='projects_single'),                      
]
