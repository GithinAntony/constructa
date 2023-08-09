from django.db import models 
from django.utils.timezone import now

#user registration
class user_registration(models.Model):
    choices = [
        ('contractors', 'Contractors'),
        ('builders', 'Builders'),
        ('civil_engineers', 'Civil Engineers'),
        ('clients', 'Clients'), 
        ('architects', 'Architects'),
    ]      
    unique_id=models.AutoField(primary_key=True, blank=False)
    user_type = models.CharField(max_length=20, choices=choices)
    first_name = models.CharField(max_length=100, null=True, blank=False)
    last_name = models.CharField(max_length=100, null=True, blank=False)
    email_address = models.CharField(max_length=255, null=True, blank=False)
    password = models.CharField(max_length=500, null=True, blank=False)
    mobile_number = models.CharField(max_length=15, null=True, blank=False)
    profile_photo = models.ImageField(upload_to='clients/', null=True, blank=True)
    address_line_1 = models.CharField(max_length=500, null=True, blank=False)   
    address_line_2 = models.CharField(max_length=500, null=True, blank=False)   
    district = models.CharField(max_length=100, null=True, blank=False)
    state = models.CharField(max_length=10,null=True, blank=False)    
    pin_code = models.CharField(max_length=8, null=True, blank=False)
    business_banner_photo = models.ImageField(upload_to='builders/', blank=True)
    business_title = models.CharField(max_length=255, null=True, blank=True)
    business_description = models.CharField(max_length=500, null=True, blank=True)
    business_email_address = models.CharField(max_length=255, null=True, blank=True)
    business_mobile_number = models.CharField(max_length=10, null=True, blank=True)
    business_address_line_1 = models.CharField(max_length=200, null=True, blank=True)   
    business_address_line_2 = models.CharField(max_length=200, null=True, blank=True)   
    business_district = models.CharField(max_length=100, null=True, blank=True)
    business_state = models.CharField(max_length=40,null=True, blank=True)    
    business_pin_code = models.CharField(max_length=6, null=True, blank=True)
    business_solution = models.CharField(max_length=500, null=True, blank=True)    
    status_choices = [
        ('pending', 'Pending'),
        ('active', 'Active'),
    ]
    business_profile_status = models.CharField(max_length=15, choices=status_choices, default="pending")
    status = models.CharField(max_length=15, choices=status_choices, default="active")
    date_added = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return str(self.email_address)


class business_profile_image(models.Model):
    unique_id = models.AutoField(primary_key=True, blank=False) 
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE, related_name='business_profile_image_conn',default=0)
    image = models.ImageField(upload_to='builders/business/', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return str(self.unique_id)   

class messages_index(models.Model):    
    unique_id=models.AutoField(primary_key=True, null=False) 
    recipient_user=models.ForeignKey(user_registration, on_delete=models.CASCADE, related_name='recipient_images_conn',default=0)
    sender_user=models.ForeignKey(user_registration, on_delete=models.CASCADE, related_name='sender_images_conn',default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return str(self.recipient_user)

class messages_contain(models.Model):   
    unique_id = models.AutoField(primary_key=True, null=False)
    msg_index = models.ForeignKey(messages_index, null=False, on_delete=models.CASCADE, related_name='msg_index_conn')
    participant_user = models.ForeignKey(user_registration, null=True, on_delete=models.SET_NULL)
    messages_text = models.TextField(default='', null=False)
    message_choices = [
        ('normal', 'Normal'),
        ('project', 'Project'),
    ]
    message_type = models.CharField(max_length=15, choices=message_choices, default="normal")    
    date_added=models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return self.messages_text  

class message_participants(models.Model):
    unique_id = models.AutoField(primary_key=True, null=False)
    msg_index = models.ForeignKey(messages_index, null=False, on_delete=models.CASCADE)        
    participant_user = models.ForeignKey(user_registration, null=True, on_delete=models.SET_NULL)
    type_choices = [
        ('sender', 'Sender'),
        ('recipient', 'Recipient'),
        ('others','Others'),
    ]
    participant_user_type = models.CharField(max_length=15, choices=type_choices, default="active")
    status_choices = [
        ('pending', 'Pending'),
        ('active', 'Active'),
    ]
    status = models.CharField(max_length=15, choices=status_choices, default="active")
    date_added=models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True) 

class projects(models.Model):
    unique_id = models.AutoField(primary_key=True, blank=False)
    msg_index = models.ForeignKey(messages_index, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE, default=0, related_name='user_projects')
    title = models.CharField(max_length=255, null=True, blank=False)
    description = models.CharField(max_length=500, null=True, blank=False)
    client = models.ForeignKey(user_registration, on_delete=models.CASCADE, default=0, related_name='client_projects')
    location = models.CharField(max_length=150, null=True, blank=False)
    size = models.IntegerField(default=0, blank=False)
    start_date = models.CharField(default=0, max_length=10, blank=False)  
    end_date = models.CharField(default=0, max_length=10, blank=False)  
    categories_choices = [  
        ('residential', 'Residential'),            
        ('commercial', 'Commercial'),    
        ('education', 'Education'),    
        ('government', 'Government'),    
        ('infrastructure', 'Infrastructure'),      
        ('healthcare', 'Healthcare'),
        ]
    categories = models.CharField(max_length=15, choices=categories_choices, default="residential")  
    status_choices = [
        ('started', 'Pending'),
        ('ongoing', 'Active'),
        ('completed', 'Completed'),
    ]
    project_status = models.CharField(max_length=15, choices=status_choices, default="started")
    tags = models.CharField(max_length=500, null=True, blank=True)
    publish = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.title          

class projects_image(models.Model):
    unique_id = models.AutoField(primary_key=True, blank=False) 
    project = models.ForeignKey(projects, on_delete=models.CASCADE, related_name='projects_images_conn')
    image = models.ImageField(upload_to='projects/', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)  

   

