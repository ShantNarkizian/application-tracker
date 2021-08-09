"""app_tracker URL Configuration

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
from django.urls import path, include

from website.views import website, new_application, about_page, archive_page
from applications.views import new_interview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', website, name="website"),
    path('new_interview', new_interview, name='new_interview'),
    path('newapp', new_application, name="new_application"),
    path('about', about_page, name="about_page"),
    path('archive', archive_page, name="archive_page"),
    path('application/', include("applications.urls")),
]
