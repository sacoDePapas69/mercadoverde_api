from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Category, Product


class ProductForm(forms.ModelForm):

    class Meta: 
        model= Product
        fields = ['name', 'price', 'description', 'image', 'category']
        labels ={
            'name':'Nombre',
            'price':'Precio',
            'description': 'Descripción',
            'image':'Imagen',
            'category':'Categoría',
        }
        widgets={
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese precio', 
                    'id': 'precio'
                }
            ), 
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese descripción', 
                    'id': 'descripcion'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese descripción', 
                    'id': 'imagen'
                }
            ), 
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria'
                }
            )

        }

 
    
     

