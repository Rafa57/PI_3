from django.contrib import admin
from django.urls import path

from exams.views import exams_list
from medics.views import medics_list
from patients.views import patients_list, get_patient, add_patient
from home.views import home


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("exams/", exams_list),
    path("medics/", medics_list),
    path("patients/", patients_list),
    path("patients/add/", add_patient, name="add_patient"),
    path("patients/<str:cpf>/", get_patient, name="get_patient"),
]