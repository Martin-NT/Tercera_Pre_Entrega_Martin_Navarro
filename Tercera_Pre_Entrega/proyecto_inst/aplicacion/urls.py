from django.urls import path, include
from .views import *
urlpatterns = [ 
    #Rutas propias de la aplicacion
    path('', home, name="home"),
    path('pacientes/', pacientes, name="pacientes"),
    path('profesionales/', profesionales, name="profesionales"),
    path('turnos/', turnos , name="turnos"),
    path('consultorios/', consultorios, name="consultorios"),
    path('acerca_de/', acerca_de, name="acerca_de"),
    path('buscar/', buscar, name="buscar"),
    path('agregar/', agregar, name="agregar"),
    
    path('buscar2/', buscar2, name="buscar2"),
    path('buscar3/', buscar3, name="buscar3"),
    path('buscar4/', buscar4, name="buscar4"), #PARA BUSCAR A LOS PROFESIONALES
    path('buscar5/', buscar5, name="buscar5"),
    
    path('buscar_turno/', buscarTurno, name="buscar_turno"),
    path('buscar_paciente/', buscarPaciente, name="buscar_paciente"),
    path('buscar_profesional/', buscarProfesional, name="buscar_profesional"),
    path('buscar_consultorio/', buscarConsultorio, name="buscar_consultorio"),
    
    path('turno_form/', turnoForm, name="turno_form"),
    path('paciente_form/', pacienteForm, name="paciente_form"),
    path('profesional_form/', profesionalForm, name="profesional_form"),
    path('consultorio_form/', consultorioForm, name="consultorio_form"),
]