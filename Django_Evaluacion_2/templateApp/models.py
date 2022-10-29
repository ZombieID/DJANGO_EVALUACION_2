from email.policy import default
from random import choices
from django.db import models

# Create your models here.
#Lista de elecciones disponibles a ingresar
estado_choices =(
    ("RESERVADO","RESERVADO"),
    ("COMPLETADA","COMPLETADA"),
    ("ANULADA","ANULADA"),
    ("NO ASISTEN","NO ASISTEN"),
)

cantidad_choices =(
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("7","7"),
    ("8","8"),
    ("9","9"),
    ("10","10"),
    ("11","11"),
    ("12","12"),
    ("13","13"),
    ("14","14"),
    ("15","15"),
)

class reserva(models.Model):
    idReserva = models.CharField(verbose_name="ID Reserva",max_length=50,blank=False)
    nombreSolicitante = models.CharField(verbose_name="Nombre Solicitante",max_length=50,blank=False)
    fono = models.CharField(max_length=20)
    fecha = models.DateField(blank=False)
    hora = models.TimeField(blank=False)
    estado = models.CharField(max_length=10,blank=False,choices=estado_choices,default="RESERVADO")
    cantidadPersonas = models.CharField(verbose_name="Cantidad de Personas",blank=False,max_length=2,choices=cantidad_choices,default="15")
    observacion = models.CharField(max_length=200,blank=True)