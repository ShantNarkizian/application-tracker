from django.shortcuts import render, get_object_or_404
from .models import Application

# Create your views here.


def details(request, company):
    app = get_object_or_404(Application, pk=company)
    return render(request, "applications/appDetails.html", {"application": app})

