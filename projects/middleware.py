from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

class SessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.path.startswith('/projects/service-message/'):
            path_parts = request.path.split('/')
            service_id = path_parts[-1]  # The second-to-last part of the URL path
            required_session_vars = {
                'is_logged_in': True,
            }
            for key, value in required_session_vars.items():
                if key not in request.session or request.session[key] != value:
                 messages.error(request, 'Please enter your login details to access this page')
                 return redirect(reverse('projects:services_single', args=[service_id]))
                
        if request.path.startswith('/projects/service-message-list') or request.path.startswith('/projects/chat-message'):
            required_session_vars = {
                'is_logged_in': True,
            }
            for key, value in required_session_vars.items():
                if key not in request.session or request.session[key] != value:
                 messages.error(request, 'Please enter your login details to access this page')
                 return redirect(reverse('clients:sign_in'))   
                
        # If the user is authenticated, continue processing the request
        response = self.get_response(request)
        return response