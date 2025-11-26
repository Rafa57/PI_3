from django.urls import path

from . import views

urlpatterns = [
    path("", views.medics_list, name='medics'),
    path("add_medic/", views.add_medic, name='add_medic'),
]