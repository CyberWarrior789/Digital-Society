"""DigitalSoc URL Configuration

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
from django.urls import path,include
from . import views

urlpatterns = [
    path('Mprofile/', views.Mprofile, name='Mprofile'), 
    path('Madd-member/', views.Madd_member, name='Madd-member'),
    path('Mview-member/', views.Mview_member, name='Mview-member'),
    path('Madd-complain/', views.Madd_complain, name='Madd-complain'),
    path('Mview-notice', views.mview_notice, name='Mview-notice'),
    path('Mview-events', views.mview_events, name='Mview-events'),
]
