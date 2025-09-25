from django.contrib import admin
from django.urls import path
from medics.views import medics
from exams.views import exams

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", medics),
    path("", exams),
]
