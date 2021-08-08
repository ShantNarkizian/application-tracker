from django.shortcuts import render
from applications.models import Application
# Create your views here.
from django.http import HttpResponse


def welcome(request):
    return render(request, "homepage/homepage.html", {"applications": Application.objects.all()})
