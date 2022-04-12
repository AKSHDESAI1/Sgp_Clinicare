"""oClinicPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

admin.site.site_header = 'Clinicare'
admin.site.site_title = 'Clinicare Panel'
admin.site.index_title = 'Welcme to Clinicare Panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('login1/', views.login1, name='login1'),
    path('logout1/', views.logout1, name='logout1'),
    path('signin1/', views.signin1, name='signin1'),
    path('', views.home1, name='home1'),
    path('info/', views.info, name='info'),
    path('profile/', views.profile, name='profile'),
    path('connection/', views.connection, name='connection'),
    path('migrane_chat/', views.migrane_chat, name='migrane_chat'),
    path('heartattack_chat/', views.heartattack_chat, name='heartattack_chat'),
    path('covid-19_chat/', views.covid_19, name='covid_19'),
    path('thyroid_chat/', views.thyroid, name='thyroid'),
    path('diabetes_chat/', views.diabetes, name='diabetes'),
    path('404_Error/', views.error, name='error'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('checkup/', views.checkup, name='checkup'),
    
    path('profile1/', views.profile1, name='profile1'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('detail/<int:my_id>/', views.detail, name='detail'),
    path('userchangepassword/<str:my_id1>/', views.changepassword1, name='changepassword1')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
