from django.db import models
from patients.models import Patients

class Medics(models.Model):

    MEDIC_STATUS = [
        ("ocupado", "Ocupado"),
        ("disponivel", "Disponivel"),
        ("indisponivel", "Indisponivel"),
        ("aguardando", "Aguardando")
    ]

    crm = models.CharField(primary_key=True, unique=True, max_length=20, null=False, blank=False, default="0000")
    name = models.CharField(max_length=100, null=False, blank=False, default="-")
    especialization = models.CharField(max_length=100, null=False, blank=False, default='-')
    hire_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default="Aguardando")