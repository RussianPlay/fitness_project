from django.contrib import admin
from .views import register
from django.contrib.auth import views as views_auth
from django.urls import path, include


urlpatterns = [
    
    path('register/', register, name='register'),
    path('login/', views_auth.LoginView.as_view(template_name='users/login.html', extra_context = {}), name='login'),
    path('logout/', views_auth.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]