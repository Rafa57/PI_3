from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Patients(models.Model):

    cpf = models.CharField(primary_key=True, unique=True, max_length=11, null=False, blank=False)
    name = models.CharField(null=False, blank=False, max_length=100)
    age = models.SmallIntegerField(null=False, blank=False)
    addres = models.CharField(null=False, blank=False, max_length=200)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} ({self.cpf})"

    @classmethod
    def create_patient(cls, cpf, name, age, addres, phone):
        patient = cls(cpf=cpf, name=name, age=age, addres=addres, phone=phone)
        patient.save()
        return f"O usuário {patient.name} foi adicinado com sucesso"










# cpf_validator = RegexValidator(
#     regex=r'^\d{11}$',
#     message="CPF deve conter 11 dígitos numéricos",
#     code="invalid CPF"
#     )

# cpf = models.CharField(
#     primary_key=True,
#     unique=True,
#     max_length=11,
#     validators=[cpf_validator],
#     null=False,
#     blank=False,
#     verbose_name="CPF",
#     # serialize=True, #já vem True por padrão
# )