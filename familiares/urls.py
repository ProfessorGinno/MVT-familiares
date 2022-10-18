from django.urls import path
from .views import mostrar_familiares

urlpatterns = [
    path('', mostrar_familiares),
]
