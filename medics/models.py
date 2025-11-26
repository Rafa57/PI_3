from django.db import models
from datetime import date, datetime, time

from patients.models import Patients

class Medics(models.Model):

    MEDIC_STATUS = [
        ("ocupado", "Ocupado"),
        ("disponivel", "Disponivel"),
        ("indisponivel", "Indisponivel"),
        ("aguardando", "Aguardando")
    ]

    crm = models.CharField(
        primary_key = True,
        unique = True,
        max_length = 20,
        null = False,
        blank = False,
        default = "0000000000"
    )
    name = models.CharField(
        max_length = 100,
        null = False,
        blank = False,
        default = "-"
    )
    spec = models.CharField(
        max_length = 100,
        default= 'Não informado'
    )
    hire_date = models.DateField(

    )
    status = models.CharField(
        max_length = 20,
        choices = MEDIC_STATUS,
        default = 'aguardando'
    )

    @classmethod
    def create_medic(cls, crm, name, spec, hire_date):
        medic = cls(
            crm = crm,
            name = name,
            spec = spec,
            hire_date = hire_date,
        )
        medic.save()
        
        return f"O médico{medic.name} foi adicionado com sucesso!"
    
    def update_status(self):
        now = datetime.now().date()

        if self.exams.filter(scheduled_date=now, status="agendado").exists():
            self.status = "ocupado"
        elif self.exams.filter(status="em_progresso").exists():
            self.status = "ocupado"
        elif hasattr(self, "unavailable") and self.unavailable:
            self.status = "indisponivel"
        else:
            self.status = "disponivel"
        
        self.save()