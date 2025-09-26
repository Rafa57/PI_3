from django.contrib import admin
from django.urls import path

from exams.views import exams_list
from medics.views import medics
from patients.views import patients

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", exams_list),
    path("medics", medics),
    path("patients", patients),
]