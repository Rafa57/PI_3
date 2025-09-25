from django.db import models


# Create your models here.
class Exams(models.Model):
    tittle = models.CharField(max_length=100, null=False, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    scheduled_exam = models.DateTimeField(null=False, blank=False)
    realized_exam = models.DateTimeField(null=True)
