from django.shortcuts import render
from .models import Medics

# Create your views here.
def medics_list(request):
    medics = Medics.objects.all()
    return render(request, "medics/medics_list.html", {"medicos": medics})
