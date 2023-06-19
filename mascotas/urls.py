from django.urls import path
from .views import principal, causa, formulario, adopcion, imagenes, registro, ingreso_productos, modificar, mostrar_productos, eliminar, mostrar_asociados

urlpatterns=[
    path('', principal, name="principal"),
    path('causa/', causa, name="causa"),
    path('formulario/', formulario, name="formulario"),
    path('adopcion/', adopcion, name="adopcion"),
    path('imagenes/', imagenes, name="imagenes"),
    path('registro-usuario/', registro, name="registro"),
    path('ingreso-productos/', ingreso_productos, name="ingreso_productos"),
    path('modificar-producto/<id>', modificar, name= "modificar_productos"),
    path('mostrar-productos/', mostrar_productos, name= "mostrar_productos"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('mostrar-asociados/', mostrar_asociados, name= "mostrar_asociados"),

]