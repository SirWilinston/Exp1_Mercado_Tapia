from django.urls import path
from .views import principal, causa, formulario, adopcion, imagenes

urlpatterns=[
    path('', principal, name="principal"),
    path('causa/', causa, name="causa"),
    path('formulario/', formulario, name="formulario"),
    path('adopcion/', adopcion, name="adopcion"),
    path('imagenes/', imagenes, name="imagenes")
]