from dataclasses import fields
from importlib.abc import ExecutionLoader
from pyexpat import model
from tabnanny import verbose
from django import forms
from django.forms import ValidationError
from templateApp.models import reserva
from templateApp import models

class FormReserva(forms.ModelForm):

    idReserva = forms.CharField(label="ID Reserva",max_length=50,required=True)
    nombreSolicitante = forms.CharField(label="Nombre Solicitante",max_length=50,required=True)
    fono = forms.CharField(max_length=20,required=True)
    fecha = forms.DateField(required=True)
    hora = forms.TimeField(required=True)
    estado = forms.CharField(widget=forms.Select(choices=models.estado_choices))
    cantidadPersonas = forms.IntegerField(label="Cantidad de Personas",required=True,min_value=1,max_value=15)
    observacion = forms.CharField(max_length=200,required=False)

        

    class Meta:
        model = reserva
        fields = '__all__'
    
