from django.urls import path
from . import views

app_name='contractors'
urlpatterns = [
    path('sign-in',views.sign_in,name='sign_in'),
    path('sign-up',views.sign_up,name='sign_up'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('edit-profile', views.edit_profile, name='edit_profile'), 
    path('edit-profile-pic', views.edit_profile_pic, name='edit_profile_pic'),
    path('edit-profile-password', views.edit_profile_password, name='edit_profile_password'), 
    path('projects-list', views.projects_list, name='projects_list'),  
    path('projects-add', views.projects_add, name='projects_add'), 
    path('projects-edit/<int:project_id>', views.projects_edit, name='projects_edit'),
    path('projects-delete/<int:project_id>', views.projects_delete, name='projects_delete'),        
    path('projects-edit-photos/<int:project_id>', views.projects_edit_photos, name='projects_edit_photos'),
    path('projects-edit-photos-delete/<int:project_id>/<int:project_images_id>', views.projects_edit_photos_delete, name='projects_edit_photos_delete'),
    path('business-profile',views.business_profile, name='business_profile'),
    path('business-profile-edit',views.business_profile_edit, name='business_profile_edit'),
    path('business-profile-photos',views.business_profile_photos, name='business_profile_photos'),
    path('business-profile-photos-delete/<int:image_id>',views.business_profile_photos_delete, name='business_profile_photos_delete'),    
    path('signup-check-email',views.signup_check_email,name='signup_check_email'),
    path('signup-check-mobile',views.signup_check_mobile,name='signup_check_mobile'),                            
]
