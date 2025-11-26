from django.shortcuts import render, get_list_or_404, redirect
from datetime import datetime, date
import re

from .models import Medics

# Create your views here.
def medics_list(request, crm=None):
    if crm:
        medics = [get_list_or_404(Medics, crm=crm)]
    else:
        medics = Medics.objects.all().prefetch_related("exams")
        
    return render(request, "medics/medics_list.html", {"medics": medics})

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
        return "O campo deve conter somente letras e espaços"
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





# if status:
#         status_list = [
#             "ocupado",
#             "disponivel",
#             "indisponivel",
#             "aguardando"
#         ]
#         if status not in status_list:
#             return "Status inválido"