from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Patients

def patients_list(request):
    patients = Patients.objects.all().prefetch_related("exams")
    return render(request, "patients/patients_list.html", {"pacientes": patients})

# def get_patient(request, cpf):
#     patient = get_object_or_404(Patients, cpf=cpf)
#     return render(request, "patients/patients_list.html", {"paciente": [patient]})