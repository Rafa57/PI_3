from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def exams(request):
    return render(request, 'exams/home.html')