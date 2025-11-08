from django.db import models
from patients.models import Patients
from medics.models import Medics

# Create your models here.

class Exams(models.Model):
    EXAM_TYPES = [
        ("ultrassonografia", "Ultrassonografia"),
        ("ressonância magnética", "Ressonancia magnética"),
        ("radiografia", "Radiografia"),
        ("hemograma", "exame de sangue"),
        ("glicemia em jejum", "Glicemia em jejum")
    ]

    STATUS_CHOICES = [
        ("agendado", "Agendado"),
        ("pendente", "Pendente"),
        ("concluido", "Concluido"),
        ("cancelado", "Cancelado")
    ]

    PAYMENT_STATUS = [
        ("pendente", "Pendente"),
        ("em_andamento", "Em andamento"),
        ("pago", "Pago")
    ]

    exam_type = models.CharField(max_length=100, choices=EXAM_TYPES, null=False, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    scheduled_exam = models.DateTimeField(null=False, blank=False)
    exam_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pendente")
    exam_value = models.FloatField(null=False, blank=False, default=0.0)
    pay_status = models.CharField(max_length=50, choices=PAYMENT_STATUS,  default="Pendente")

    patient = models.ForeignKey(
        Patients,
        on_delete=models.CASCADE,
        related_name="exams",
        null=True,
        blank=True
    )

    medic = models.ForeignKey(
        Medics,
        on_delete=models.CASCADE,
        related_name="exams"
    )

    @classmethod
    def create_exam(cls, exam_type, patient, medic, created_date, scheduled_date, exam_status, exam_value, pay_status):

        new_exam = cls.objects.create(
            exam_type=exam_type,
            patient=patient,
            medic=medic,
            created_date=created_date,
            scheduled_date=scheduled_date,
            exam_status=exam_status,
            exam_value=exam_value,
            pay_status=pay_status
        )
        
        new_exam.save()
        return f"Exame '{exam_type}' para o paciente {patient.name} criado com sucesso!"

    
def __str__(self):
    return f"Tipo: {self.exam_type} | Paciente: {self.patient.name} | Médico: {self.medic.name}"