"""FarmerBot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings
from mainapp import views as main_views
from adminapp import views as admin_views
from userapp import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_views.main_home,name="home"),
    path('about',main_views.main_about,name="about"),
    path('contact',main_views.main_contact,name="contact"),
    path('admin-login',admin_views.main_admin,name="admin_login"),
    path('admin-dashboard',admin_views.admin_dashboard,name="admin_dashboard"),
    path('admin-pending',admin_views.admin_pending,name="admin_pending"),
    path('accept-users/<int:user_id>/',admin_views.accept_users,name="accept_users"),
    path('reject-users/<int:user_id>/',admin_views.reject_users,name="reject_users"),
    path('change-status-users/<int:user_id>/',admin_views.change_status_users,name="change_status_users"),
    path('remove-users/<int:user_id>/',admin_views.remove_users,name="remove_users"),
        
    path('admin-all-user',admin_views.admin_all_user,name="admin_all_user"),
    path('admin-user-profile',admin_views.admin_user_profile,name="admin_user_profile"),
    path('admin-user-profile-view/<int:user_id>/',admin_views.admin_user_profile_view,name="admin_user_profile_view"),
    path('admin-feedback',admin_views.admin_feedback,name="admin_feedback"),
    path('admin-feedback-graph',admin_views.admin_feedback_graph,name="admin_feedback_graph"),
    
    path('user-login',user_views.main_user_login,name="user_login"),
    path('user-register',user_views.main_user_register,name="user_register"),
    path('user-dashboard',user_views.user_dashboard,name="user_dashboard"),
    path('user-chatbot-btn',user_views.user_chatbot_btn,name="user_chatbot_btn"),
    path('user-chatbot',user_views.user_chatbot,name="user_chatbot"),
    path('user-myprofile',user_views.user_myprofile,name="user_myprofile"),
    path('user-edit-profile',user_views.user_edit_profile,name="user_edit_profile"),
    path('user-password',user_views.user_password,name="user_password"),
    path('user-cropdetails',user_views.user_cropdetails,name="user_cropdetails"),
    path('user-fertilizer',user_views.user_fertilizer,name="user_fertilizer"),
    path('user-feedback',user_views.user_feedback,name="user_feedback"),
    
    
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
