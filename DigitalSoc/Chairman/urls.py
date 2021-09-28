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
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('Cprofile/', views.cprofile, name='Cprofile'), 
    path('index/', views.index, name='index'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('otp/', views.otp, name='otp'),
    path('reset-password/', views.reset_password, name='reset-password'),
    path('add-member/', views.add_member, name='add-member'),
    path('view-member/', views.view_member, name='view-member'),
    path('add-notice/', views.add_notice, name='add-notice'),
    path('add-events/', views.add_events, name='add-events'),
    path('view-notice/', views.view_notice, name='view-notice'),
    path('view-events/', views.view_events, name='view-events'),
    path('view-complain/', views.view_complain, name='view-complain'),
    path('all-watchman/', views.all_watchman, name='all-watchman'),
    path('approved/<int:pk>', views.approved, name='approved'),
    path('rejected/<int:pk>', views.rejected, name='rejected'),
    path('del-notice/<int:pk>/', views.del_notice, name='del-notice'),
]
