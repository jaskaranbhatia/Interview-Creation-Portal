"""InterviewPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Interviews import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('interviews/', views.get_interviews, name='get_interviews'),
    path('participants/', views.list_participants, name='listings_par'),
    path('create_interview/', views.create_interview, name = 'create_interview'),
    path('create_participant/', views.create_participant, name = 'create_participant'),
    path('delete_interview/<str:interview_name>', views.delete_interview, name='delete_interview'),
    path('edit_interview/<str:interview_name>', views.edit_interview, name='edit_interview'),
    path('upload_resume/<str:pname>', views.upload_resume, name ='upload_resume'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)