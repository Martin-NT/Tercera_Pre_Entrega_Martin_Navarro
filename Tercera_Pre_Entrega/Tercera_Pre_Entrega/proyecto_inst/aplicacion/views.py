from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.timezone import make_aware
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Paciente, Profesional, Turno, Consultorio
from .forms import TurnoForm, PacienteForm, ProfesionalForm, ConsultorioForm

# Create your views here.
def home(request):
    return render(request, 'aplicacion/home.html')

def acerca_de(request):
    return render(request, 'aplicacion/acerca_de.html')

def pacientes(request):
    contexto = {'pacientes': Paciente.objects.all(), 'titulo': 'listado de pacientes'}
    return render(request, 'aplicacion/pacientes.html', contexto)

def profesionales(request):
    contexto = {'profesionales': Profesional.objects.all(), 'titulo': 'listado de profesionales'}
    return render(request, 'aplicacion/profesionales.html', contexto)

def turnos(request):
    contexto = {'turnos': Turno.objects.all(), 'titulo': 'listado de turnos'}
    return render(request, 'aplicacion/turnos.html', contexto)

def consultorios(request):
    contexto = {'consultorios': Consultorio.objects.all(), 'titulo': 'listado de consultorios'}
    return render(request, 'aplicacion/consultorios.html', contexto)

def agregar(request):
    return render(request, 'aplicacion/agregar.html')

def buscar(request):
    return render(request, 'aplicacion/buscar.html')

def buscarTurno(request):
    return render(request, 'aplicacion/buscarTurno.html')

def buscarPaciente(request):
    return render(request, 'aplicacion/buscarPaciente.html')

def buscarProfesional(request):
    return render(request, 'aplicacion/buscarProfesional.html')

def buscarConsultorio(request):
    return render(request, 'aplicacion/buscarConsultorio.html')

#Buscar Turnos
def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        turnos = Turno.objects.filter(paciente__icontains=patron)
        contexto = {'turnos': turnos,  'titulo': f'listado de turnos que tiene como patron "{patron}"'}
        return render(request, "aplicacion/turnos.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

#Buscar Pacientes
def buscar3(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        pacientes = Paciente.objects.filter(nombre__icontains=patron)
        contexto = {'pacientes': pacientes,'titulo': f'listado de pacientes que tiene como patron "{patron}"'}
        return render(request, "aplicacion/pacientes.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

#Buscar Profesionales
def buscar4(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        profesionales = Profesional.objects.filter(nombre__icontains=patron)
        contexto = {'profesionales': profesionales,'titulo': f'listado de profesionales que tiene como patron "{patron}"'}
        return render(request, "aplicacion/profesionales.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

#Buscar Consultorios
def buscar5(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        consultorios = Consultorio.objects.filter(nombre__icontains=patron)
        contexto = {'consultorios': consultorios, 'titulo': f'listado de consultorios que tiene como patron "{patron}"'}
        return render(request, "aplicacion/consultorios.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")
    

#Agregar Turnos
def turnoForm(request):
    if request.method == "POST":
        miForm = TurnoForm(request.POST)
        if miForm.is_valid():
            turno_paciente = miForm.cleaned_data.get('paciente').title()
            turno_dia = miForm.cleaned_data.get('dia')
            turno_horario = miForm.cleaned_data.get('horario')
            turno_profesional = miForm.cleaned_data.get(
                'profesional') 
            turno_fecha_hora = make_aware(
                datetime.combine(turno_dia, turno_horario))

            if turno_fecha_hora.date() < datetime.now().date():
                messages.success(
                    request, "No se puede seleccionar un dia pasado")
            else:
                turno = Turno(
                    paciente=turno_paciente,
                    dia=turno_fecha_hora.date(),
                    horario=turno_fecha_hora,
                    profesional=turno_profesional
                )
                turno.save()
                messages.success(request, 'Turno agregado exitosamente.')
            return redirect(reverse_lazy('turno_form'))
    else:
        miForm = TurnoForm()

    return render(request, "aplicacion/turnoForm.html", {"form":miForm})
#Agregar Consultorios
def consultorioForm(request):
    if request.method == "POST":
        miForm = ConsultorioForm(request.POST)
        if miForm.is_valid():
            consultorio_nombre = miForm.cleaned_data.get('nombre').title()
            consultorio_profesional = miForm.cleaned_data.get('profesional').title()
            consultorio_dia = miForm.cleaned_data.get('dia')
            consultorio_horario = miForm.cleaned_data.get('horario')
            
            # Combinar el día y la hora para crear un objeto DateTime
            consultorio_fecha_hora = make_aware(datetime.combine(consultorio_dia, consultorio_horario))
            
            # Verificar si el día ingresado es menor al día actual
            if consultorio_fecha_hora.date() < datetime.now().date():
                messages.success(request, "No se puede seleccionar un dia pasado")
            else:
                consultorio = Consultorio(nombre=consultorio_nombre,
                        dia=consultorio_fecha_hora.date(),
                        horario=consultorio_fecha_hora,
                        profesional=consultorio_profesional,)
                consultorio.save()
                messages.success(request, 'Consultorio agregado exitosamente.')
            return redirect(reverse_lazy('consultorio_form')) # Redirige a la vista deseada después de guardar

    else:
        miForm = ConsultorioForm()

    return render(request, "aplicacion/consultorioForm.html", {"form":miForm})

#Agregar Pacientes
def pacienteForm(request):
    if request.method == "POST":
        miForm = PacienteForm(request.POST)
        if miForm.is_valid():
            paciente_nombre = miForm.cleaned_data.get('nombre').title()
            paciente_apellido = miForm.cleaned_data.get('apellido').title()
            paciente_edad = miForm.cleaned_data.get('edad')
            paciente_estado = miForm.cleaned_data.get('estado')
            paciente = Paciente(nombre=paciente_nombre,
                        apellido=paciente_apellido,
                        edad=paciente_edad,
                        estado=paciente_estado)
            paciente.save()
            
            messages.success(request, 'Paciente agregado exitosamente.')
            return redirect(reverse_lazy('paciente_form')) # Redirige a la vista deseada después de guardar
    else:
        miForm = PacienteForm()

    return render(request, "aplicacion/pacienteForm.html", {"form": miForm})

#Agregar Profesionales
def profesionalForm(request):
    if request.method == "POST":
        miForm = ProfesionalForm(request.POST)
        if miForm.is_valid():
            profesional_nombre = miForm.cleaned_data.get('nombre').title()
            profesional_apellido = miForm.cleaned_data.get('apellido').title()
            profesional_profesion = miForm.cleaned_data.get('profesion').title()
            profesional_dias_atencion = ', '.join(miForm.cleaned_data.get('dias_atencion'))
            profesional = Profesional(
                nombre=profesional_nombre,
                apellido=profesional_apellido,
                profesion=profesional_profesion,
                dias_atencion=profesional_dias_atencion
            )
            profesional.save()

            messages.success(request, 'Profesional agregado exitosamente.')
            return redirect(reverse_lazy('profesional_form')) # Redirige a la vista deseada después de guardar
    else:
        miForm = ProfesionalForm()

    return render(request, "aplicacion/profesionalForm.html", {"form": miForm})
