from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
import re

from .models import Exams, Patients, Medics

def exams_list(request):
    exams = Exams.objects.select_related("patient", "medic").all()

    return render(request, "exams/exams_list.html", {"exams": exams})

def get_exam(request, id):
    exam = get_object_or_404(Exams.objects.select_related("patient", "medic"), id=id)

    return render(request, "exams/exam_info.html", {
        "exam": exam
    })

def verify_form(exam_type, patient, medic, scheduled_exam, exam_status, exam_value, pay_status):

    if not exam_type not in dict(Exams.EXAM_TYPES):
        return "Tipo de exame inválido ou não fazemos esse tipo de exame."
    
    if not Patients.objects.filter(id=patient.id).exists():
        return "Paciente inválido"
    
    if not Medics.objects.filter(id=medic.id).exists():
        return "Médico inválido"
    
    if not isinstance(scheduled_exam, datetime):
        return "Data agendada inválida"
    
    now = datetime.now()
    if scheduled_exam < now:
        return "A data agendada não pode estar no passado"
    
    if exam_status not in dict(Exams.STATUS_CHOICES):
        return "Status inválido"
    
    try:
        exam_value = float(exam_value)
        if exam_value < 0:
            return "O valor não pode ser negativo"
    except:
        return "Valor do exame inválido"
    
    if pay_status not in dict(Exams.PAYMENT_STATUS):
        return "Status de pagamento inválido."
    
    return None

def add_exam(request):
    success = False
    error = None

    if request.method == 'POST':
        e_type = request.POST.get("e_type")
        patient = request.POST.get("patient")
        medic = request.POST.get("medic")
        scdl = request.POST.get("scdl")
        e_status = request.POST.get("e_status")
        e_value = request.POST.get("e_value")
        pay_status = request.POST.get("pay_status")

        error = verify_form(e_type, patient, medic, scdl, e_status, e_value, pay_status)    
        
        if not error:
            Exams.create_exam(e_type, patient, medic, scdl, e_status, e_value, pay_status)
            success = True

    return render(request, "exams/add_exam.html", {
        "error": error, "success": success
    })
