from django.urls import path
from mascotas.views import *
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

    path('tienda/',tienda, name="tienda"),
    path('tienda/',tienda, name="tienda"),
    path('generarBoleta/', generarBoleta, name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
]