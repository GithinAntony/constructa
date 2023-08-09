from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls',namespace='home'),),
    path('architects/',include('architects.urls',namespace='architects'),),
    path('builders/',include('builders.urls',namespace='builders'),),
    path('clients/',include('clients.urls',namespace='clients'),), 
    path('contractors/',include('contractors.urls',namespace='contractors'),),
    path('civil_engineers/',include('civil_engineers.urls',namespace='civil_engineers'),),
    path('projects/',include('projects.urls',namespace='projects'),),        
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
