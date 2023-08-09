from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import *
from projects.models import user_registration, business_profile_image, messages_index, messages_contain
from django.db.models import Avg, Count
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

# Create your views here.
def sign_in(request):
    if request.method == 'POST':
            data_record = request.POST
            if user_registration.objects.filter(mobile_number=data_record['mobile_number'],password=data_record['password'],user_type='builders'):
                user_details = user_registration.objects.get(mobile_number=data_record['mobile_number'],password=data_record['password'],user_type='builders')
                if user_details.status == 'active':
                    request.session['is_logged_in'] = True
                    request.session['user_type'] = 'builders'                    
                    request.session['user_id'] = user_details.unique_id   
                    request.session['first_name'] = user_details.first_name
                    request.session['last_name'] = user_details.last_name                                     
                    request.session['email_address'] = user_details.email_address
                    request.session['mobile_number'] = user_details.mobile_number
                    return redirect(reverse('builders:dashboard'))
                else:
                    messages.error(request, 'User is suspended. Contact the admin!')
                    return redirect(reverse('builders:sign_in'))
            else:
                messages.error(request, 'Invalid credentials!')
                return redirect(reverse('builders:sign_in'))
    return render(request, 'builders/sign-in.html')

def sign_up(request):
    if request.method == 'POST':
        data_record = request.POST
        if user_registration.objects.filter(email_address=data_record['email_address'],user_type='builders'):
            messages.error(request, 'Email already exists! Please try again!')
            return redirect(reverse('builders:sign_up'))
        elif user_registration.objects.filter(mobile_number=data_record['mobile_number'],user_type='builders'):
            messages.error(request, 'Mobile number already exists! Please try again!')
            return redirect(reverse('builders:sign_up'))
        else:
            profile_photo = request.FILES['profile_photo']
            folder = 'builders' # subfolder name
            fs = FileSystemStorage(location=f'media/{folder}')            
            file_name = fs.save(profile_photo.name, profile_photo)

            signup = user_registration(
                user_type = 'builders',                
                first_name = data_record['first_name'],
                last_name = data_record['last_name'],
                mobile_number = data_record['mobile_number'],
                email_address = data_record['email_address'],
                password = data_record['password'],
                address_line_1 = data_record['address_line_1'],
                address_line_2 = data_record['address_line_2'],
                district = data_record['district'],
                state = data_record['state'],
                pin_code = data_record['pin_code'],
                profile_photo = f'{folder}/{file_name}',
                status='active',
            )            
            signup.save()

            messages.success(request, 'Builder registered successfully!')
            return redirect(reverse('builders:sign_in'))
    context = {}
    return render(request, 'builders/sign-up.html', context)


def logout(request):
    del request.session['is_logged_in']
    del request.session['first_name']
    del request.session['last_name']
    del request.session['email_address']
    del request.session['user_id']
    del request.session['mobile_number']
    del request.session['user_type']
    return redirect(reverse('builders:sign_in'))

def dashboard(request):
    userdata = user_registration.objects.get(unique_id=request.session['user_id'])
    context = { 'userdata': userdata }
    return render(request, 'builders/dashboard.html', context)   

def edit_profile(request):
    userdata = user_registration.objects.get(unique_id=request.session['user_id'])
    if request.method == 'POST':
        data_record = request.POST
        # update the user object with the new data from the form
        if user_registration.objects.filter(email_address=data_record['email_address'],user_type='builders').exclude(unique_id=request.session['user_id']):
            messages.error(request, 'Email already exists! Please try again!')
            return redirect(reverse('builders:edit_profile'))
        elif user_registration.objects.filter(mobile_number=data_record['mobile_number'],user_type='builders').exclude(unique_id=request.session['user_id']):
            messages.error(request, 'Mobile number already exists! Please try again!')
            return redirect(reverse('builders:edit_profile'))
        else:
            userdata.first_name = data_record['first_name']
            userdata.last_name = data_record['last_name']
            userdata.mobile_number = data_record['mobile_number']
            userdata.email_address = data_record['email_address']
            userdata.address_line_1 = data_record['address_line_1']
            userdata.address_line_2 = data_record['address_line_2']
            userdata.district = data_record['district']
            userdata.state = data_record['state']
            userdata.pin_code = data_record['pin_code']
            userdata.save() # save the updated user object
            messages.success(request, 'Profile updated successfully!')
            return redirect(reverse('builders:edit_profile')) # redirect to the user detail pagee    
    context = { 'userdata': userdata }
    return render(request, 'builders/edit-profile.html', context)

def edit_profile_pic(request):
    userdata = user_registration.objects.get(unique_id=request.session['user_id'])
    if request.method == 'POST':
        uploaded_file = request.FILES['profile_photo']
        folder = 'builders' # subfolder name
        fs = FileSystemStorage(location=f'media/{folder}')
        file_name = fs.save(uploaded_file.name, uploaded_file)
        userdata.profile_photo = f'{folder}/{file_name}'
        userdata.save()
        messages.success(request, 'Profile picture changed successfully!')
    return redirect(reverse('builders:edit_profile'))

def edit_profile_password(request):
    userdata = user_registration.objects.get(unique_id=request.session['user_id'])
    if request.method == 'POST':
        data_record = request.POST
        if userdata.password == data_record['old_password']:
            userdata.password = data_record['password']
            userdata.save()
            messages.success(request, 'Password updated successfully!')
        else:
            messages.error(request, 'Please enter correct previous password!') 
        return redirect(reverse('builders:edit_profile'))

def projects_list(request):
    userdata = projects.objects.filter(user_type=request.session['user_type'],user_id=request.session['user_id']).all()
    context = { 'userdata' : userdata, 'request' : request }
    return render(request, 'projects/projects-list.html', context)

def projects_add(request):
    if request.method == 'POST':
        data_record = request.POST
        if projects.objects.filter(title=data_record['title']):
            messages.error(request, 'Title already exists! Please try again!')
            return redirect(reverse('builders:projects_add'))
        else:
            projects_data = projects(
                user_type=request.session['user_type'],
                user_id=request.session['user_id'],
                title=data_record['title'],
                description=data_record['description'],
                client=data_record['client'],
                architect=data_record['architect'],
                location=data_record['location'],
                size=data_record['size'],
                year_completed=data_record['year_completed'],
                categories=data_record['categories'],
            )            
            projects_data.save()
            last_inserted_id = projects_data.unique_id
            messages.success(request, 'Project added successfully! Now you can add related pictures! ')
            return redirect(reverse('builders:projects_edit', args=[last_inserted_id]))
    context = { 'request': request }    
    return render(request, 'projects/projects-add.html', context)

def projects_edit(request,project_id):
    userdata = projects.objects.get(unique_id=project_id)
    userdata_image = userdata.projects_images_conn.all()
    if request.method == 'POST':
        data_record = request.POST
        # update the user object with the new data from the form
        if projects.objects.filter(title=data_record['title']).exclude(unique_id=project_id):
            messages.error(request, 'Title already exists! Please try again!')
            return redirect(reverse('builders:projects_edit', args=[project_id]))
        else:
            userdata.title = data_record['title']
            userdata.description = data_record['description']
            userdata.client = data_record['client']
            userdata.architect = data_record['architect']
            userdata.location = data_record['location']
            userdata.size = data_record['size']
            userdata.year_completed = data_record['year_completed']
            userdata.categories = data_record['categories']
            userdata.save() # save the updated user object
            messages.success(request, 'Project updated successfully!')
            return redirect(reverse('builders:projects_edit', args=[project_id])) 
        
    context = { 'userdata': userdata, 'userdata_image': userdata_image, 'request' : request }
    return render(request, 'projects/projects-edit.html', context)

def projects_delete(request,project_id):    
    userdata = get_object_or_404(projects, unique_id=project_id)
    userdata.delete()
    messages.success(request, 'Project deleted successfully!')    
    return redirect(reverse('builders:projects_list'))  

def projects_edit_photos(request,project_id):
    if request.method == 'POST':
        uploaded_file = request.FILES['title_photo']
        folder = 'projects' # subfolder name
        fs = FileSystemStorage(location=f'media/{folder}')
        file_name = fs.save(uploaded_file.name, uploaded_file)
        projects_data = projects_image(
        project = projects.objects.get(unique_id=project_id),  
        image = f'{folder}/{file_name}'
        )            
        projects_data.save()
        messages.success(request, 'Picture added successfully!')
    return redirect(reverse('builders:projects_edit', args=[project_id]))  

def projects_edit_photos_delete(request,project_id,project_images_id):
    photo = get_object_or_404(projects_image, unique_id=project_images_id)
    photo.delete()
    messages.success(request, 'Picture deleted successfully!')    
    return redirect(reverse('builders:projects_edit', args=[project_id]))   


def business_profile(request):
    userdata = user_registration.objects.get(unique_id=request.session['user_id'])
    userdata_image = userdata.business_profile_image_conn.all()
    if userdata.business_solution is not None:
        business_solution_list = userdata.business_solution.split(",")
    else:
        business_solution_list = []
    context = {
        'userdata': userdata,
        'userdata_image': userdata_image,
        'business_solution_list': business_solution_list
    }
    return render(request, 'builders/business-profile.html', context)

def business_profile_edit(request):
    userdata = user_registration.objects.get(unique_id=request.session['user_id'])
    userdata_image = userdata.business_profile_image_conn.all()
    if request.method == 'POST':
        data_record = request.POST
        # update the user object with the new data from the form
        if user_registration.objects.filter(business_title=data_record['business_title']).exclude(unique_id=request.session['user_id']).exists():
            messages.error(request, 'Title already exists! Please try again!')
            return redirect(reverse('builders:business_profile_edit'))
        else:
            if 'business_banner_photo' in request.FILES:
                uploaded_file = request.FILES['business_banner_photo']
                folder = 'builders' # subfolder name
                fs = FileSystemStorage(location=f'media/{folder}')            
                file_name = fs.save(uploaded_file.name, uploaded_file)
                userdata.business_banner_photo = f'{folder}/{file_name}'
                
            business_solutions_list = data_record.getlist('business_solutions')
            business_solutions_clean_list = list(filter(lambda value: value.strip(), business_solutions_list))
            business_solutions_string = ', '.join(business_solutions_clean_list)
            userdata.business_title = data_record['business_title']
            userdata.business_description = data_record['business_description']
            userdata.business_mobile_number = data_record['business_mobile_number']
            userdata.business_email_address = data_record['business_email_address']
            userdata.business_address_line_1 = data_record['business_address_line_1']
            userdata.business_address_line_2 = data_record['business_address_line_2']
            userdata.business_district = data_record['business_district']
            userdata.business_state = data_record['business_state']
            userdata.business_pin_code = data_record['business_pin_code']
            userdata.business_profile_status = 'active'
            userdata.business_solution = business_solutions_string
            userdata.save() # save the updated user object
            
            messages.success(request, 'Business profile updated successfully!')
            return redirect(reverse('builders:business_profile_edit'))     
    context = { 'userdata': userdata, 'userdata_image': userdata_image }    
    return render(request, 'builders/business-profile-edit.html', context)
 

def business_profile_photos(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['business_profile_photo']
        folder = 'builders' # subfolder name
        fs = FileSystemStorage(location=f'media/{folder}')
        file_name = fs.save(uploaded_file.name, uploaded_file)
        business_profile_data = business_profile_image(
        user_id = request.session['user_id'],  
        image = f'{folder}/{file_name}'
        )            
        business_profile_data.save()
        messages.success(request, 'Picture added successfully!')
    return redirect(reverse('builders:business_profile_edit'))  

def business_profile_photos_delete(request,image_id):
    photo = get_object_or_404(business_profile_image, unique_id=image_id)
    photo.delete()
    messages.success(request, 'Picture deleted successfully!')    
    return redirect(reverse('builders:business_profile_edit'))     

def messages_list(request):
    userdata = user_registration.objects.get(unique_id=request.session['user_id'])
    context = { 'userdata': userdata }
    return render(request, 'clients/messages_list.html', context)  

def messages_single(request, unique_id):
    userdata = user_registration.objects.get(unique_id=request.session['user_id'])
    context = { 'userdata': userdata }
    return render(request, 'clients/messages_single.html', context) 

def signup_check_email(request):
    if request.method == 'POST':
        data_record = request.POST
        # Check if the email exists in the database
        if user_registration.objects.filter(email_address=data_record['email_a'],user_type='builders').exists():
            response_data = {'exists': True}
        else:
            response_data = {'exists': False}
        # Return the result as a JSON response
    else:
        response_data = {'exists': True}    
    return JsonResponse(response_data)

def signup_check_mobile(request):
    if request.method == 'POST':
        data_record = request.POST
        # Check if the phone number exists in the database
        if user_registration.objects.filter(mobile_number=data_record['phone_number'],user_type='builders').exists():
            response_data = {'exists': True}
        else:
            response_data = {'exists': False}
        # Return the result as a JSON response
    else:
        response_data = {'exists': True}    
    return JsonResponse(response_data)
