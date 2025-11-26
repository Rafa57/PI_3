from django.urls import path

from . import views

urlpatterns = [
    path("", views.medics_list, name='medics_list'),
    path("add_medic/", views.add_medic, name='add_medic'),
    path("update/<str:crm>/", views.update_medic, name='update_medic'),
    path("<str:crm>/", views.get_medic, name='get_medic'),
]