from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from datetime import datetime, date
import re

from .models import Medics

# Create your views here.
def medics_list(request, crm=None):
    if crm:
        medics = [get_object_or_404(Medics, crm=crm)]
    else:
        medics = Medics.objects.all().prefetch_related("exams")
        
    return render(request, "medics/medics_list.html", {"medics": medics})

def get_medic(request, crm):
        medic = get_object_or_404(Medics, crm=crm)
        return render(request, "medics/medic_info.html", {"medic": medic})

def verify_form(crm, name, espec, hire_date):

    if not crm.isdigit():
        return "O CRM deve conter somente números"
    if len(crm) != 10:
        return "O CRM deve conter exatamente 10 dígitos"
    if Medics.objects.filter(crm=crm).exists():
        return "Esse CRM já está cadastrado"
    if not re.match(r"^[A-Za-zÀ-ÿ ]+$", name):
        return "O nome deve conter apenas letras"
    if not espec.replace(' ', '').isalpha():
        return "Especialização inválida. Digite somente letras e espaços"
    if hire_date:
        try:
            h_date = datetime.strptime(hire_date, "%Y-%m-%d").date()  
        except ValueError:
            return "Formato de data inválido"
        if h_date > date.today():
            return "A data não pode ser no futuro"
    
    return None

def add_medic(request):
    error = None
    success = False

    if request.method == "POST":
        crm = request.POST.get('crm')
        name = request.POST.get('name')
        spec = request.POST.get('spec')
        hire_date = request.POST.get('hire_date')
        
        error = verify_form(crm, name, spec, hire_date)

        if not error:
            hire_date = datetime.strptime(hire_date, "%Y-%m-%d").date()

            Medics.create_medic(
                crm = crm,
                name = name,
                spec = spec,
                hire_date = hire_date
            )
            
            success = True

    return render(request, "medics/add_medic.html", {"error": error, "success": success})

def update_medic(request, crm):
    medic = get_object_or_404(Medics, crm=crm)
    error = None
    success = False

    if request.method == "POST":
        name = request.POST.get("name")
        spec = request.POST.get("spec")

        if not re.match(r"^[A-Za-zÀ-ÿ ]+$", name):
            error = "O nome deve conter somente letras e espaços."
        if not re.match(r"^[A-Za-zÀ-ÿ ]+$", spec):
            error = "A especialização deve conter somente letras e espaços."
        
        if not error:
            medic.name = name
            medic.spec = spec
            medic.save()
            success = True
    
    return render(request, "medics/update_medics.html", {"medic": medic, "success": success, "error": error})

def rmv_medic(request, crm):
    medic = get_object_or_404(Medics, crm=crm)
    
    if request.method == "POST":
        if request.POST.get("confirm") == "1":
            return render(
                request,
                "medics/medic_info.html", 
                {"medic": medic, "confirm_del": True}
            )
        
        if request.POST.get("confirmed") == "yes":
            medic.delete()
            messages.success(request, "Cadastro removido com sucesso!")
            return redirect('medics_list')
        
    return render(request, "medics/medic_info.html", {"medic": medic})