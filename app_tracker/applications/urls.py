from django.urls import path
from . import views

urlpatterns = [
    path('<str:company>', views.details, name='details'),
]