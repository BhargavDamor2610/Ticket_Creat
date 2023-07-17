"""
URL configuration for Ticket_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp import views
urlpatterns = [
    path('', views.Home, name='Home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add_user/', views.add_user, name='add_user'),
    path('User/', views.User, name='User'),
    path('department/', views.department, name='department'),
    path('add_department/', views.add_department, name='add_department'),
    path('department_edit/<int:pk>/', views.department_edit, name='department_edit'),
    path('delete_department/<int:pk>/', views.delete_department, name='delete_department'),
    

]
