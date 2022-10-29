from contextvars import Context
from email import message
from django.shortcuts import render, redirect
from templateApp.forms import FormReserva
from templateApp.models import reserva
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listadoReservas(request):
    reservas = reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservas.html', data)

def eliminarReserva(request, id):
    reser = reserva.objects.get(id = id)
    reser.delete()
    messages.warning(request,'¡Reserva eliminada!')
    return redirect('/reservas')

def agregarReserva(request):
    form = FormReserva()
    titulo= 'AGREGAR RESERVA'
    if request.method == 'POST':
        form = FormReserva(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Reserva agregada con éxito!')
        return redirect('/reservas')
    data = {'form' : form,'titulo':titulo}
    return render(request, 'agregar_reserva.html', data)

def actualizarReserva(request, id):
    reser = reserva.objects.get(id = id)
    form = FormReserva(instance=reser)
    titulo = 'ACTUALIZAR RESERVA'
    if request.method == 'POST':
        form = FormReserva(request.POST, instance=reser)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Reserva actualizada con éxito!')
            return redirect('/reservas')
    data = {'form' : form,'titulo':titulo}
    return render(request, 'agregar_reserva.html', data)
