from django.utils.html import format_html
from django.contrib import admin
from .models import *

class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('mobile_number', 'user_type', 'first_name', 'last_name', 'display_image', 'email_address', 'business_title', 'business_profile_status')
    list_filter = ('user_type', 'business_profile_status', 'status')
    search_fields = ('first_name', 'last_name', 'email_address', 'mobile_number', 'business_title')

    def display_image(self, obj):
        if obj.profile_photo:
            return format_html('<img src="{}" style="max-height:100px;"/>', obj.profile_photo.url)
        else:
            return '-'
    display_image.allow_tags = True
    display_image.short_description = 'Image'

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'msg_index', 'user', 'client', 'location', 'size', 'start_date', 'end_date', 'categories', 'project_status', 'tags', 'publish', 'date_added', 'date_updated')
    list_filter = ('project_status', 'publish', 'date_added')
    search_fields = ('title', 'description', 'client__first_name', 'client__last_name', 'user__first_name', 'user__last_name')

class ProjectsImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'display_image', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('project__title',)
    
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:100px;"/>', obj.image.url)
        else:
            return '-'
    display_image.allow_tags = True
    display_image.short_description = 'Image'

class BusinessProfileImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_image', 'date_added', 'date_updated')
    search_fields = ('user__first_name', 'user__last_name', 'user__email_address')
    list_filter = ('date_added', 'date_updated')
    
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:100px;"/>', obj.image.url)
        else:
            return '-'
    display_image.allow_tags = True
    display_image.short_description = 'Image'  

class MessagesIndexAdmin(admin.ModelAdmin):
    list_display = ('recipient_user', 'sender_user', 'date_added', 'date_updated') 

class MessagesContainAdmin(admin.ModelAdmin):
    list_display = ('msg_index', 'participant_user', 'messages_text', 'message_type', 'date_added', 'date_updated')
    list_filter = ('message_type',)
    search_fields = ('msg_index__recipient_user__email_address', 'msg_index__sender_user__email_address', 'participant_user__email_address', 'messages_text')
    ordering = ('-unique_id',)    
    
class MessageParticipantsAdmin(admin.ModelAdmin):
    list_display = ('msg_index', 'participant_user', 'participant_user_type', 'status', 'date_added', 'date_updated')
    list_filter = ('participant_user_type', 'status', 'date_added')
    search_fields = ('msg_index__recipient_user__username', 'msg_index__sender_user__username', 'participant_user__username')
    ordering = ('-date_added',)       

admin.site.register(user_registration, UserRegistrationAdmin)
admin.site.register(projects, ProjectsAdmin)
admin.site.register(projects_image, ProjectsImageAdmin) 
admin.site.register(business_profile_image, BusinessProfileImageAdmin)
admin.site.register(messages_index, MessagesIndexAdmin)
admin.site.register(messages_contain, MessagesContainAdmin)
admin.site.register(message_participants, MessageParticipantsAdmin)


