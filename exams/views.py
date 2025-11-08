from django.shortcuts import render, get_list_or_404, redirect

from .models import Exams

def exams_list(request):
    exams = Exams.objects.all
    return render(request, "exams/exams_list.html", {"exames": exams})