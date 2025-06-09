"""
URL configuration for fitness_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView
from django_prometheus import exports






urlpatterns = [
    
    path('admin/', admin.site.urls),
    re_path(r"^$", RedirectView.as_view(pattern_name='home')),
    path('', include('users.urls')),
    path('store/', include('store.urls')),
    path('metrics/', exports.ExportToDjangoView, name='prometheus-django-metrics'),
    # path(..., name='home') 

]
