from django.shortcuts import render

# Create your views here.
def patients(request):
    return render(request, "patients/home.html")
