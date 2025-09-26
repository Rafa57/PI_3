from django.contrib import admin
from django.urls import path
from medics.views import medics
from exams.views import exams
from patients.views import patients

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", medics),
    path("", exams),
    path("", patients),
]
