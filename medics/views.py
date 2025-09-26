from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def medics(request):
    return render(request, "medics/home.html")
