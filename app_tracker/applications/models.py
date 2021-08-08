from django.db import models
from datetime import time

# Create your models here.


class Application(models.Model):
    company_name = models.CharField(primary_key=True, max_length=100)
    position = models.CharField(max_length=100)
    jobLink = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"Company: {self.company_name}"


class Interview(models.Model):
    application = models.OneToOneField(
        Application,
        on_delete=models.CASCADE,
        primary_key=True,
        editable=True,
    )
    interview_date = models.DateField(editable=True)
    start_time = models.TimeField(default=time(9), editable=True)
    duration = models.IntegerField(default=1, editable=True)
    interview_type = models.CharField(max_length=100, editable=True)

    def __str__(self):
        return f"The interview for: {self.application.company_name} on: {self.interview_date}"
