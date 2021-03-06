from django.shortcuts import render, get_object_or_404, redirect

import website.views
from .models import Application, Interview
from django.forms import modelform_factory

# Create your views here.


def details(request, company):
    app = get_object_or_404(Application, pk=company)
    if request.method == "POST":
        #app.delete()
        app.archived = True
        app.save()
        return website.views.website(request)

    return render(request, "applications/appDetails.html", {"application": app})


def interview_details(request, company):
    interview = get_object_or_404(Interview, pk=company)
    return render(request, "applications/interviewDetails.html", {"intv": interview})


ApplicationForm = modelform_factory(Interview, exclude=[])


def new_interview(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("website")
    else:
        form = ApplicationForm()
    return render(request, "applications/addInterview.html", {"form": form})

   # return render(request, "applications/addInterview.html")




