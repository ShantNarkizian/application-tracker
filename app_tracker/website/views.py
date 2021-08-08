from django.shortcuts import render, redirect
from applications.models import Application, Interview
from django.forms import modelform_factory


def website(request):
    return render(request, "website/homepage.html", {"applications": Application.objects.all(),
                                                      "interviews": Interview.objects.all()})


ApplicationForm = modelform_factory(Application, exclude=[])


def new_application(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("website")
    else:
        form = ApplicationForm()
    return render(request, "applications/newApplication.html", {"form": form})

