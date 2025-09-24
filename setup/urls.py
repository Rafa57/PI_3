
from django.contrib import admin
from django.urls import path
from db_manage.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
