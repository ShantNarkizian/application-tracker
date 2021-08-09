from django.urls import path
from . import views

urlpatterns = [
    path('<str:company>', views.details, name='details'),
    path('<str:company>/interview', views.interview_details, name='interview_details'),
]