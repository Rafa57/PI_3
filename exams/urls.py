from django.urls import path

from . import views

urlpatterns = [
    path("", views.exams_list, name='exams_list'),
    path("add/", views.add_exam, name='add_exam'),
]