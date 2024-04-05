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
from adminpanel import views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
     path('staff/', include('userpanel.urls')),
    path('adminpanel/', views.adminpanel, name='home'),
    path('', views.login_view, name='home'),
    # path('staff/', views.staff, name='staff'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
      path('change-password/', views.change_password_view, name='change_password'),
    #   path('usercreation/', views.usercreation, name='usercreation'),
      path('usercreation/', views.usercreation, name='upload_file'),
      path('auditformniro/', views.auditformniro, name='auditform'),
      path('create-alert/', views.create_alert, name='create_alert'),
      path('watch-alert/', views.watch_alert, name='watch_alert'),
      path('create-test/', views.create_test, name='create_test'),
      path('take-test/', views.take_test, name='take_test'),
      path('test-detail/<int:form_id>/', views.test_detail, name='test-detail'),
      path('create-sop/', views.create_sop, name='create_sop'),
      path('watch-sop/', views.watch_sop, name='watch_sop'),
      path('create_video/', views.create_video, name='create_video'),
      path('watch_video/', views.watch_video, name='watch_video'),
      path('profile/', views.profile, name='profile'),
    #   path('complete-alert/', views.complete_alert, name='complete_alert'),
     path('alerts/<int:alert_id>/', views.alert_detail, name='alert_detail'),  # Change alert_detail to your actual detail view
     path('deletealert/<int:alert_id>/', views.delete_alert, name='delete_alert'),  # Change alert_detail to your actual detail view
      path('deletevideo/<int:pk>/', views.delete_video, name='delete_video'),
        # path('generate-certificate/<int:evaluation_id>/', views.generate_certificate, name='generate_certificate'),
       path('recheck/<str:sessionid>/', views.recheck_view, name='recheck'),
       path('recheck-done/<str:sessionid>/', views.recheck_done, name='recheck_done'),
       path('recheck-forms/', views.recheck_form, name='recheck_form'),
       path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
       path('form-dashboard/', views.form_dashboard, name='form-dashboard'),
       path('updateprofile/', views.updateprofile, name='updateprofile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
