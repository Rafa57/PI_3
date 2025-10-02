from django.db import models
from patients.models import Patients

class Medics(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    especialization = models.CharField(max_length=50, null=False, blank=False)
    hire_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    status = models.DateTimeField(null=True)
    exams = models.ForeignKey(Patients, on_delete=models.CASCADE, null=True, blank=True)