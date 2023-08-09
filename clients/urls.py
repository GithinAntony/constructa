from django.urls import path
from . import views

app_name='clients'
urlpatterns = [
    path('sign-in',views.sign_in,name='sign_in'),
    path('sign-up',views.sign_up,name='sign_up'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout', views.logout, name='logout'),  
    path('edit-profile', views.edit_profile, name='edit_profile'), 
    path('edit-profile-pic', views.edit_profile_pic, name='edit_profile_pic'),
    path('edit-profile-password', views.edit_profile_password, name='edit_profile_password'),
    path('messages-list', views.messages_list, name='messages_list'),  
    path('messages-single/<int:id>', views.messages_single, name='messages_single'),
    path('signup-check-email',views.signup_check_email,name='signup_check_email'),
    path('signup-check-mobile',views.signup_check_mobile,name='signup_check_mobile'),       
]
