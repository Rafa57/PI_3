from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
cpf_validator = RegexValidator(
    regex=r'^\d{11}$',
    message="CPF deve conter 11 dígitos numéricos",
    code="invalid CPF"
    )

class Patients(models.Model):
    cpf = models.CharField(
        primary_key=True,
        max_length=11,
        unique=True,
        validators=[cpf_validator],
        null=False,
        blank=False,
        verbose_name="CPF",
        # serialize=True, #já vem True por padrão
    )
    name = models.CharField(null=False, blank=False, max_length=50)
    age = models.SmallIntegerField(null=False, blank=False)
    addres = models.CharField(null=False, blank=False, max_length=100)
    phone = models.IntegerField(null=False, blank=False)