from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime

from .models import Exams

def exams_list(request):
    exams = Exams.objects.select_related("patient", "medic").all()

    return render(request, "exams/exams_list.html", {"exams": exams})

def get_exam(request, id):
    exam = get_object_or_404(Exams.objects.select_related("patient", "medic"), id=id)

    return render(request, "exams/exam_info.html", {
        "exam": exam
    })

def add_exam(request):
    succes = False
    error = None

    if request.method == 'POST':
        e_type = request.POST.get("e_type")
        patient = request.POST.get("patient")
        medic = request.POST.get("medic")
        schl_e = request.POST.get("")

