from django.contrib import admin
from django.urls import path, include


from exams.views import exams_list
from medics.views import medics_list
from patients import views
from home.views import home


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include('home.urls')),
    path("medics/", include('medics.urls')),
    path("patients/", include('patients.urls')),
    path("exams/", include('exams.urls')),

    # path("exams/", exams_list),
    # path("patients/", patients_list, name="patients_list"),
    # path("patients/add/", add_patient, name="add_patient"),
    # path("patients/update/<str:cpf>/", update_patient, name="update_patient"),
    # path("patients/<str:cpf>/", get_patient, name="get_patient"),
    # path("patients/delete/<str:cpf>/", rmv_patient, name="remove_patient"),
]