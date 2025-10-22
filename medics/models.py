from django.db import models
from patients.models import Patients

class Medics(models.Model):
    crm = models.CharField(primary_key=True, unique=True, max_length=20, null=False, blank=False, default="0000")
    name = models.CharField(max_length=50, null=False, blank=False)
    especialization = models.CharField(max_length=50, null=False, blank=False)
    hire_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    status = models.DateTimeField(null=True)
    exams = models.ForeignKey(Patients, on_delete=models.CASCADE, null=True, blank=True)