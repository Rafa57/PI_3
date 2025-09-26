from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def patients(request):
    return render(request, "patients/home.html")
