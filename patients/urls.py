from django.urls import path

from . import views

urlpatterns = [
    path("", views.patients_list, name='patients_list'),

    path("add/", views.add_patient, name="add_patient"),
    path("tbl-info/", views.tbl_info, name='tbl_info'),

    path("update/<str:cpf>/", views.update_patient, name="update_patient"),
    path("delete/<str:cpf>/", views.rmv_patient, name="remove_patient"),
    
    path("<str:cpf>/", views.get_patient, name="get_patient"),
]