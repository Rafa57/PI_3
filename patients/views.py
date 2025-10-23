from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from .models import Patients

def patients_list(request, cpf=None):
    if cpf:
        patients = [get_object_or_404(Patients, cpf=cpf)]
    else:
        patients = Patients.objects.all().prefetch_related("exams")
        
    return render(request, "patients/patients_list.html", {"pacientes": patients})

def get_patient(request, cpf):
    patient = get_object_or_404(Patients, cpf=cpf)
    return render(request, "patients/patient_info.html", {"patient": patient})

def add_patient(request):
    if request.method == "POST":
        cpf = request.POST.get("cpf")
        name = request.POST.get("name")
        age = request.POST.get("age")
        addres = request.POST.get("addres")
        phone = request.POST.get("phone")
        
        Patients.create_patient(cpf, name, age, addres, phone)
        return redirect("/patients/")

    return render(request, "patients/add_patient.html")

def update_patient(request, cpf):
    patient = get_object_or_404(Patients, cpf=cpf)
    success = False

    if request.method == "PUT":
        patient.name = request.PUT.get("name")
        patient.age = request.PUT.get("age")
        patient.addres = request.PUT.get("addres")
        patient.phone = request.PUT.get("phone")
        patient.save()
        success = True

    return render(request, "patients/update_patient.html", {"patient": patient, "success": success})