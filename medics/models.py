from django.db import models


class Medics(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    especialization = models.CharField(max_length=50, null=False, blank=False)
    hire_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    fired_date = models.DateTimeField(null=True)
