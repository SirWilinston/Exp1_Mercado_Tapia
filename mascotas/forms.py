from django import forms
from django.forms import widgets
from .models import Asociado, Producto
from django.contrib.auth.forms import UserCreationForm

class RegistroUserForm(UserCreationForm):
    pass

class AsociadoForm(forms.ModelForm):
    class Meta: 
        model = Asociado
        fields = [ 'nombre', 'rutAsociado', 'tipoAsociado', 'correo','edad','telefono','comuna']
        labels = {
            'nombre': 'Nombre:',
            'rutAsociado' : 'Rut (sin puntos con guión):',
            'tipoAsociado' : 'Tipo de asociado:',
            'correo' : 'Correo:',
            'edad' : 'Edad:',
            'telefono' : 'Telefono:',
            'comuna' : 'Comuna:'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese su nombre...',
                    'id': 'nombre',
                    'class': 'form-control'
                }
            ),
            'rutAsociado': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su rut...',
                    'id': 'rutAsociado',
                    'class': 'form-control'
                }
            ),
            'tipoAsociado': forms.Select(
                attrs={
                    'id': 'tipoAsociado',
                    'class': 'form-control'
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su correo...',
                    'id': 'correo',
                    'class': 'form-control'
                }
            ),
            'edad': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su edad...',
                    'id': 'edad',
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su teléfono...',
                    'id': 'telefono',
                    'class': 'form-control'
                }
            ),
            'comuna': forms.Select(
                attrs={
                    'id': 'comuna',
                    'class': 'form-control'
                }
            ),
           
        }
class ProductoForm(forms.ModelForm):
    class Meta: 
        model = Producto
        fields = [ 'id', 'nombre', 'precio', 'foto']
        labels = {
            'id': 'ID:',
            'nombre' : 'Nombre:',
            'precio' : 'Precio:',
            'foto' : 'Foto:',
        }
        widgets = {
            'id': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese id de producto...',
                    'id': 'id',
                    'class': 'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre del producto...',
                    'id': 'nombre',
                    'class': 'form-control'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese precio del producto...',
                    'id': 'precio',
                    'class': 'form-control'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'placeholder': 'Ingrese foto del producto...',
                    'id': 'foto',
                    'class': 'form-control'
                }
            )
           
        }
