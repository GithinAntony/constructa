from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import *
from django.db.models import Avg, Count
from django.core.files.storage import FileSystemStorage

def services(request):
    #userdata_builders = user_registration.objects.all()
    if 'is_logged_in' not in request.session or request.session['is_logged_in'] != True:
        userdata_builders = user_registration.objects.filter(business_profile_status='active').all()
    else:
        userdata_builders = user_registration.objects.filter(business_profile_status='active').exclude(unique_id=request.session['user_id']).all()    
    context = { 'userdata_list' : userdata_builders }
    return render(request, 'projects/services-list.html', context) 

def services_single(request, service_id):
    userdata = user_registration.objects.get(unique_id=service_id)   
    userdata_image = userdata.business_profile_image_conn.all()
    
    if userdata.business_solution is not None:
        business_solution_list = userdata.business_solution.split(",")
    else:
        business_solution_list = []        
    context = { 'userdata': userdata, 'userdata_image': userdata_image, 'business_solution_list':business_solution_list, 'service_id_t':service_id }
    return render(request, 'projects/services-single.html', context) 

def services_message_list(request):
    user_messages_list = messages_index.objects.filter(sender_user_id=request.session['user_id']).all()
    user_messages_list_2 = messages_index.objects.filter(recipient_user_id=request.session['user_id']).all()
    user_messages_list_3 = message_participants.objects.filter(participant_user_id=request.session['user_id'],participant_user_type='others').all()

    user_messages_list_array = []

    if user_messages_list.count() > 0:
        for row in user_messages_list:
            user_messages_list_array.append({ 'messages_index': row, 'msg_type':'sender' }) 

    if user_messages_list_2.count() > 0:
        for row in user_messages_list_2:
            user_messages_list_array.append({ 'messages_index': row, 'msg_type':'recipient' })  

    if user_messages_list_3.count() > 0:
        for row in user_messages_list_3:
            user_messages_list_array.append({ 'messages_index': row.msg_index, 'msg_type':'participant' })  
              
    context = { 'user_messages_list_array':user_messages_list_array }
    return render(request, 'projects/services-message-list.html', context)      

def services_message(request,service_id):
    userdata = user_registration.objects.get(unique_id=service_id)    
    try:
        msg_index_data = messages_index.objects.get(recipient_user_id=service_id, sender_user_id=request.session['user_id'])
    except messages_index.DoesNotExist:
        msg_index_data = None

    if msg_index_data is not None:         
        msg_contain = messages_contain.objects.filter(msg_index=msg_index_data)
    else:
         msg_contain = ''

    if request.method == 'POST':
        data_record = request.POST
        if msg_index_data is not None:
            #msg_index_data = messages_index.objects.get(recipient_id=service_id,sender_id=request.session['user_id'])            
            messages_data =  messages_contain(
            msg_index = msg_index_data,
            participant_user_id = request.session['user_id'],
            messages_text = data_record['message'],
            )              
            messages_data.save()
        else:  
            latest_msg_index = messages_index.objects.latest('unique_id')
            messages_list_data = messages_index(
            recipient_user_id = service_id,
            sender_user_id = request.session['user_id'],
            )
            messages_list_data.save()

            latest_msg_index = messages_index.objects.latest('unique_id')
            participant_data_list = [(request.session['user_id'], 'sender'), (service_id, 'recipient')]
            for participant_user_id, participant_user_type in participant_data_list:
                message_participants_data = message_participants(
                    msg_index=latest_msg_index,
                    participant_user_id=participant_user_id,
                    participant_user_type=participant_user_type,
                )
                message_participants_data.save()

            # messages save
            messages_data =  messages_contain(
            msg_index = latest_msg_index,
            participant_user_id = request.session['user_id'],            
            messages_text = data_record['message'],
            )                
            messages_data.save()
        return redirect(reverse('projects:services_message', args=[service_id])) 
    msg_id = 0
    context = { 'userdata': userdata, 'userdata_sender':'', 'service_id':service_id, 'msg_index': msg_index_data, 'msg_contain': msg_contain, 'msg_id': msg_id }    
    return render(request, 'projects/services-message.html', context) 
    
def chat_message(request,msg_id):
    msg_index_data = messages_index.objects.get(unique_id=msg_id)
    userdata_recipent = user_registration.objects.get(unique_id=msg_index_data.recipient_user_id)
    userdata_sender = user_registration.objects.get(unique_id=msg_index_data.sender_user_id) 
    msg_particpant = message_participants.objects.filter(msg_index_id=msg_id,participant_user_type="others")
    userdata_architect_t = user_registration.objects.filter(business_profile_status='active',user_type='architects').all()
    userdata_civil_engineer_t = user_registration.objects.filter(business_profile_status='active',user_type='civil_engineers').all()

    userdata_architect = []
    for row in userdata_architect_t:
        flag = 1
        for row1 in msg_particpant:
            if row1.participant_user.unique_id == row.unique_id:
                flag = 0
        if flag == 1:
            userdata_architect.append(row)        

    userdata_civil_engineer = []
    for row in userdata_civil_engineer_t:
        flag = 1
        for row1 in msg_particpant:
            if row1.participant_user.unique_id == row.unique_id:
                flag = 0
        if flag == 1:
            userdata_civil_engineer.append(row)                   
    
    msg_contain = messages_contain.objects.filter(msg_index=msg_index_data)
    projects_list = projects.objects.filter(msg_index=msg_index_data).all()

    if request.method == 'POST':
        data_record = request.POST
        #msg_index_data = messages_index.objects.get(recipient_id=service_id,sender_id=request.session['user_id'])            
        messages_data =  messages_contain(
            msg_index = msg_index_data,
            participant_user_id = request.session['user_id'],
            messages_text = data_record['message'],
            )              
        messages_data.save()
        return redirect(reverse('projects:chat_message', args=[msg_id])) 
    context = { 'userdata': userdata_recipent, 'userdata_sender': userdata_sender, 'msg_id':msg_id, 'msg_index': msg_index_data, 'msg_contain': msg_contain, 'projects_list': projects_list, 'userdata_architect': userdata_architect, 'userdata_civil_engineer': userdata_civil_engineer, 'msg_particpant': msg_particpant }    
    return render(request, 'projects/services-message.html', context) 

def chat_message_particpants(request,msg_id,user_type):
    if request.method == 'POST':
        data_record = request.POST
        if user_type == 1:
            participant = data_record['text_architects']
        else:
             participant = data_record['text_civil_engineers']   

        msg_particpants = message_participants(
            msg_index_id = msg_id,
            participant_user_id = participant,
            participant_user_type = 'others',
        )
        msg_particpants.save()
        messages.success(request, 'Architect added successfully!')        
        return redirect(reverse('projects:chat_message', args=[msg_id]))  

def chat_message_particpant_delete(request,particpant_id, msg_id): 
    project = get_object_or_404(message_participants, unique_id=particpant_id)
    project.delete()
    messages.success(request, 'Participant deleted successfully!')        
    return redirect(reverse('projects:chat_message', args=[msg_id]))            

def projects_add(request,msg_id):
    msg_index_data = messages_index.objects.get(unique_id=msg_id)
    if request.method == 'POST':
        data_record = request.POST
        messages_data =  projects(
            msg_index = msg_index_data,
            user_id = request.session['user_id'], 
            title = data_record['title'],
            description = data_record['description'],
            client_id = msg_index_data.sender_user_id,
            location = data_record['location'],
            size = data_record['size'],
            start_date = data_record['start_date'],  
            end_date = data_record['end_date'],
            categories = data_record['categories_choices'],               
            )              
        messages_data.save()  
        messages.success(request, 'Project added successfully!')
        add_project_msg(request, msg_id, "Project added - " + data_record['title'])    
        return redirect(reverse('projects:chat_message', args=[msg_id]))   
    project_status_choices = [  ('started', 'Started'),  ('ongoing', 'Ongoing'),  ('completed', 'Completed'),] 
    categories_choices = [  ('residential', 'Residential'), ('commercial', 'Commercial'), ('education', 'Education'), ('government', 'Government'), ('infrastructure', 'Infrastructure'), ('healthcare', 'Healthcare'),]               
    context = { 'msg_index_data': '', 'msg_id': msg_id, 'project_status_choices':project_status_choices, 'categories_choices':categories_choices }   
    return render(request, 'projects/projects-add.html', context)     

def projects_edit(request, project_id, msg_id):
    userdata = projects.objects.get(unique_id=project_id)
    userdata_image_t = projects_image.objects.filter(project=userdata).all()
    if request.method == 'POST':        
        data_record = request.POST

        tags = data_record.getlist('tags')
        tags_clean_list = list(filter(lambda value: value.strip(), tags))
        tags_string = ', '.join(tags_clean_list)  

        if userdata.project_status != data_record['project_status']:
            add_project_msg(request, msg_id, "Project status changed - " + data_record['project_status']) 
        if userdata.publish != data_record.get('publish_check', False):
            add_project_msg(request, msg_id, "Project published")  

        userdata.title = data_record['title']
        userdata.description = data_record['description']
        userdata.location = data_record['location']
        userdata.size = data_record['size']
        userdata.start_date = data_record['start_date']
        userdata.end_date = data_record['end_date']
        userdata.categories = data_record['categories_choices']
        userdata.project_status = data_record['project_status']
        userdata.publish = data_record.get('publish_check', False)
        userdata.tags = tags_string        
        userdata.save() # save the updated user object
        messages.success(request, 'Project updated successfully!')
        return redirect(reverse('projects:projects_edit', args=[project_id,msg_id]))
    project_status_choices = [  ('started', 'Started'),  ('ongoing', 'Ongoing'),  ('completed', 'Completed'),] 
    categories_choices = [  ('residential', 'Residential'), ('commercial', 'Commercial'), ('education', 'Education'), ('government', 'Government'), ('infrastructure', 'Infrastructure'), ('healthcare', 'Healthcare'),]         
    context = { 'projects': userdata, 'projects_image': userdata_image_t, 'project_id': project_id, 'msg_id':msg_id, 'project_status_choices':project_status_choices, 'categories_choices':categories_choices }   
    return render(request, 'projects/projects-edit.html', context)  

def projects_delete(request, project_id, msg_id):
    project = get_object_or_404(projects, unique_id=project_id)
    project.delete()
    messages.success(request, 'Picture deleted successfully!')        
    return redirect(reverse('projects:chat_message', args=[msg_id]))  
 
def projects_images(request, project_id, msg_id):
    if request.method == 'POST':
        uploaded_file = request.FILES['project_images']
        folder = 'projects' # subfolder name
        fs = FileSystemStorage(location=f'media/{folder}')
        file_name = fs.save(uploaded_file.name, uploaded_file)
        projects_image_data = projects_image(
        project_id = project_id,  
        image = f'{folder}/{file_name}'
        )            
        projects_image_data.save()
        messages.success(request, 'Picture added successfully!')
    return redirect(reverse('projects:projects_edit', args=[project_id,msg_id]))

def projects_images_delete(request, image_id, project_id, msg_id):
    photo = get_object_or_404(projects_image, unique_id=image_id)
    photo.delete()
    messages.success(request, 'Project deleted successfully!')    
    return redirect(reverse('projects:projects_edit', args=[project_id,msg_id]))     

def projects_list(request):
    userdata = projects.objects.filter(user_id=request.session['user_id']).all()
    context = { 'userdata': userdata } 
    return render(request, 'projects/projects-list.html', context)  

def projects_single(request,project_id):
    userdata = projects.objects.get(unique_id=project_id)
    userdata_images = projects_image.objects.filter(project=userdata).all()
    context = { 'userdata': userdata, 'userdata_images': userdata_images }  
    return render(request, 'projects/projects-single.html', context) 

def add_project_msg(request, msg_id, msg_text):
    msg_index_data = messages_index.objects.get(unique_id=msg_id)
    messages_data =  messages_contain(
            msg_index = msg_index_data,
            participant_user_id = request.session['user_id'],
            messages_text = msg_text,
            message_type = 'project'
            )              
    messages_data.save()
