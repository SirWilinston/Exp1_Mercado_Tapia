from importlib.resources import path
from django.shortcuts import render

# Create your views here.

def principal(request):
    return render(request, 'principal.html')

def causa(request):
    return render(request, 'causa.html')

def imagenes(request):
    return render(request, 'imagenes.html')

def adopcion(request):
    return render(request, 'adopcion.html')

def formulario(request):
    return render(request, 'formulario.html')