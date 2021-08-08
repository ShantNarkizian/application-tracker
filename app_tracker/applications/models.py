from django.db import models

# Create your models here.

class Application(models.Model):
    companyName = models.CharField(primary_key=True, max_length=100)
    position = models.CharField(max_length=100)
    jobLink = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"Company: {self.companyName}"
