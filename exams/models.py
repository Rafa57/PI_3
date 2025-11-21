from django.db import models
from patients.models import Patients
from medics.models import Medics

# Create your models here.

class Exams(models.Model):
    EXAM_TYPES = [
        ("ultrassom", "Ultrassonografia"),
        ("ressonancia_magnetica", "Ressonância magnética"),
        ("radiografia", "Radiografia"),
        ("hemograma", "Exame de sangue"),
        ("glicemia_jejum", "Glicemia em jejum")
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

    exam_type = models.CharField(max_length=100, choices=EXAM_TYPES)
    creation_date = models.DateTimeField(auto_now_add=True)
    scheduled_exam = models.DateTimeField(null=False, blank=False)
    exam_status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    exam_value = models.FloatField(null=False, blank=False, default=0.0)
    pay_status = models.CharField(max_length=50, choices=PAYMENT_STATUS,  default="pendente")

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
    def create_exam(cls, exam_type, patient, medic, scheduled_exam, exam_status, exam_value, pay_status):

        new_exam = cls.objects.create( # objects.create - salva automaticamente ( não precisa do new_exam.save(). )
            exam_type = exam_type,
            patient = patient,
            medic = medic,
            scheduled_exam = scheduled_exam,
            exam_status = exam_status,
            exam_value = exam_value,
            pay_status = pay_status
        )
        
        new_exam.save()
        return f"Exame '{new_exam.exam_type}' para o paciente {patient.name} criado com sucesso!"

    
    def __str__(self):
        return f"Tipo: {self.exam_type} | Paciente: {self.patient.name} | Médico: {self.medic.name}"