from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

class SessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/civil_engineers/'):
            required_session_vars = {
                'is_logged_in': True,
                'user_type': 'civil_engineers',
            }
            for key, value in required_session_vars.items():
                if key not in request.session or request.session[key] != value:
                # Check if the current URL is the login page
                    if not request.path.startswith(reverse('civil_engineers:sign_in')) and not request.path.startswith(reverse('civil_engineers:sign_up')) and not request.path.startswith(reverse('civil_engineers:signup_check_mobile')) and not request.path.startswith(reverse('civil_engineers:signup_check_email')):                
                        # Redirect to the login page
                        messages.error(request, 'Please enter your login details to access this page')
                        return redirect(reverse('civil_engineers:sign_in'))

        # If the user is authenticated, continue processing the request
        response = self.get_response(request)
        return response