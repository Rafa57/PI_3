from django.db import models

# Create your models here.


class Exams(models.Model):
    exam_type = models.CharField(max_length=100, null=False, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    scheduled_exam = models.DateTimeField(null=False, blank=False)
    status = models.CharField(null=True, default="Agendado")

    patient = models.ForeignKey(
        "patients.Patients",
        on_delete=models.CASCADE,
        related_name="exams",
        null=True,
        blank=True
    )

def __str__(self):
    return f"{self.type} - {self.patient.name}"
