from importlib.resources import path
from django.shortcuts import render, redirect
from .forms import AsociadoForm, RegistroUserForm, ProductoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Asociado, Producto


# Create your views here.

def principal(request):
    return render(request, 'principal.html')

def causa(request):
    return render(request, 'causa.html')

def imagenes(request):
    return render(request, 'imagenes.html')

def adopcion(request):
    return render(request, 'adopcion.html')

def registro(request):
    data={
        'form': RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente!")
            return redirect('principal')
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def formulario(request):
    if request.method=="POST":    
        asociadoform = AsociadoForm(request.POST)    #creamos un objeto de tipo Formulario
        if asociadoform.is_valid():
            asociadoform.save()      #similar al insert de sql en función 
            return redirect('formulario')
    else: 
        asociadoform=AsociadoForm()
    return render(request, 'formulario.html', {'asociado_form':asociadoform})

@login_required
def ingreso_productos(request):
    if request.method=="POST":    
        productoform = ProductoForm(request.POST, request.FILES)    #creamos un objeto de tipo Formulario
        if productoform.is_valid():
            productoform.save()      #similar al insert de sql en función 
            return redirect('mostrar_productos')
    else: 
        productoform=ProductoForm()
    return render(request, 'ingreso_productos.html', {'producto_form':productoform})

@login_required    
def modificar(request, id):
    producto = Producto.objects.get(id=id)
    datos = {
        'form': ProductoForm(instance=producto) #devuelve el objeto instanciado de acuerdo a la patente
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar_productos')
    return render(request, 'modificar_producto.html', datos)    


def mostrar_productos(request):
    productos=Producto.objects.all()
    datos={
        'productos':productos
    }
    return render(request, 'mostrar_productos.html' , datos)

def mostrar_asociados(request):
    asociados=Asociado.objects.all()
    datos={
        'asociados':asociados
    }
    return render(request, 'mostrar_asociados.html' , datos)

def eliminar(request, id):
    productoEliminado = Producto.objects.get(id=id)
    productoEliminado.delete()
    return redirect ('mostrar_productos')