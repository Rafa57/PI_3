from django.contrib import admin
from django.urls import path

from exams.views import exams_list
from medics.views import medics
from patients.views import patients_list, get_patient

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", exams_list),
    path("medics/", medics),
    path("patients/", patients_list),
    path("patients/<str:cpf>/", get_patient, name="get_patient"),
]