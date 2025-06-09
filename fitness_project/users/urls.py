from django.contrib import admin
from .views import register
from django.contrib.auth import views as views_auth
from django.urls import path, include


urlpatterns = [
    
    path('register/', register, name='register'),
    path('login/', views_auth.LoginView.as_view(template_name='users/login.html', extra_context = {}), name='login'),
    path('logout/', 
     views_auth.LogoutView.as_view(
         template_name='users/logout.html',
         next_page='home' 
     ), 
     name='logout'),



    # маршруты для восстановления пароля
    path('password_reset/', views_auth.PasswordResetView.as_view(
        template_name='users/password_reset.html',
        email_template_name='users/password_reset_email.html',
        subject_template_name='users/password_reset_subject.txt'
    ), name='password_reset'),
    
    path('password_reset/done/', views_auth.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'
    ), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', views_auth.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    
    path('reset/done/', views_auth.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'
    ), name='password_reset_complete'),

]