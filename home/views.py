from django.shortcuts import render
from projects.models import *

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def about_us(request):
    return render(request, 'home/about.html')

def our_projects(request):
    userdata = projects.objects.filter(publish=1).all()
    context = { 'userdata': userdata }    
    return render(request, 'home/projects.html', context)

def projects_single(request,project_id):
    userdata = projects.objects.get(unique_id=project_id)
    userdata_images = projects_image.objects.filter(project=userdata).all()
    context = { 'userdata': userdata, 'userdata_images': userdata_images }    
    return render(request, 'home/projects-single.html', context)

def projects_list(request):
    userdata = projects.objects.filter(publish=1).all()
    context = { 'userdata': userdata } 
    return render(request, 'home/projects-list.html', context)  

def testimonials(request):
    return render(request, 'home/testimonials.html')

def faq(request):
    return render(request, 'home/faq.html')

def news(request):
    return render(request, 'home/news.html')

def contact(request):
    return render(request, 'home/contact.html')