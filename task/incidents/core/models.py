from django.db import models


# Create your models here.
class Incident(models.Model):
    time_creation = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey('core.IncidentName', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    cve_number = models.CharField(max_length=255)
    object = models.CharField(max_length=255)


class IncidentName(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True, primary_key=True)
