from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from datetime import datetime
from django.core.exceptions import ValidationError

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

def verify_form(cpf, age, phone):

    if not cpf.isdigit():
        return "O CPF deve conter somente números"
    
    if len(cpf) != 11:
        return "O CPF deve conter exatamente 11 dígitos"
    
    if Patients.objects.filter(cpf=cpf).exists():
        return "O CPF já está cadastrado"
    
    if age > 130 or age <= 0:
        return "Idade inválida"
    
    if phone:
        clean_phone = phone.replace("-", "").replace(" ", "")
        
        if Patients.objects.filter(phone=clean_phone).exists():
            return "Este telefone já está cadastrado."
        if not clean_phone.isdigit():
            return "O telefone deve conter apenas números."
        if len(clean_phone) < 8 or len(clean_phone) > 11:
            return "Número de telefone inválido."
    
    return None  

def add_patient(request):
    error = None
    success = False
    
    if request.method == "POST":
        cpf = request.POST.get("cpf")
        name = request.POST.get("name")
        age = int(request.POST.get("age"))
        addres = request.POST.get("addres")
        phone = request.POST.get("phone")

        error = verify_form(cpf, age, phone)

        if not error:
            Patients.create_patient(cpf, name, age, addres, phone)
            success = True

    return render(request, "patients/add_patient.html", {"error": error, "success":success})

def update_patient(request, cpf):
    patient = get_object_or_404(Patients, cpf=cpf)
    success = False
    error = None

    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        addres = request.POST.get("addres")
        phone = request.POST.get("phone")

        age = int(age)
        if age <= 0 or age > 130:
            error = "Idade inválida"

        clean_phone = phone.replace(' ', '').replace('-', '')

        if not error and clean_phone and not clean_phone.isdigit():
            error = "O telefone deve conter apenas números."
        
        if not error and clean_phone:
            if len(clean_phone) < 8 or len(clean_phone) > 11:
                error = "Número inválido."
        
        exist_patient = Patients.objects.filter(phone=phone).exclude(cpf=cpf).exists()
        if not error and exist_patient:
            error = "O número de telefone já está cadastrado"

        if not error:
            patient.name = name
            patient.age = age
            patient.addres = addres
            patient.phone = phone
            patient.save()
            success = True

    return render(request, "patients/update_patient.html", {"patient": patient, "error": error, "success": success})

def rmv_patient(request, cpf):
    patient = get_object_or_404(Patients, cpf=cpf)
    
    if request.method == "POST":

        if request.POST.get("confirm") == "1":
            return render(
                request,
                "patients/patient_info.html",
                {"patient": patient, "confirm_delete": True}
            )

        if request.POST.get("confirmed") == "yes":
            patient.delete()
            messages.success(request, "Paciente removido com sucesso!")
            return redirect('patients_list')

    return render("patients/patient_info.html", {"patient": patient})