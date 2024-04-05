"""
URL configuration for snapdeal project.

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
from userpanel import views
from django.urls import include, path
urlpatterns = [
    path('', views.staff, name='staff'),
    path('profile/', views.profile, name='profile'),
    path('auditform/<slug:session_id>/', views.audit_form_detail, name='audit_form_detail'),
    path('generate-certificate/<int:evaluation_id>/', views.generate_certificate, name='generate_certificate'),
    path('audit-reports/', views.auditReports, name='audit-reports'),
    path('test-reports/', views.testReports, name='test-reports'),
    path('user-dashboard/', views.userDashboard, name='user-ashboard'),
]
