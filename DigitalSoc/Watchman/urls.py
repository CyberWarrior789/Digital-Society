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
    path('sign-up', views.sign_up, name='sign-up'),
    path('Wprofile', views.wprofile, name='Wprofile'),
    path('Wview-member', views.wview_member, name='Wview-member'),
    path('Wview-notice', views.wview_notice, name='Wview-notice'),
    path('Wview-events', views.wview_events, name='Wview-events'),
    path('add-visitor', views.add_visitor, name='add-visitor'),
    path('edit-visitor', views.edit_visitor, name='edit-visitor'),
    path('view-visitor', views.view_visitor, name='view-visitor'),
]