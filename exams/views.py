from django.shortcuts import render

from .models import Exams

def exams_list(request):
    exams = Exams.objects.all
    return render(request, "exams/exams_list.html", {"exames": exams})