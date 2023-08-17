from django import forms 
from django.forms.widgets import DateInput
from .models import *

class TurnoForm(forms.Form):
    paciente = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Nombre del Paciente'
        })
    )
    dia = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control mb-3'
        }),
        required=True,
        label='Fecha del Turno'
    )
    horario = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control mb-3'
        }),
        required=True,
        label='Horario del Turno'
    )
    profesional = forms.ModelChoiceField(
        queryset=Profesional.objects.all(),
        label="Profesión Elegida",
        required=True,
        widget=forms.Select(attrs={'class': 'form-select mb-3'})
    )

class PacienteForm(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre del Paciente'})
    )
    apellido = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Apellido del Paciente'})
    )
    edad = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Edad del Paciente'})
    )
    ESTADOS = (
        ("En Tratamiento", "En Tratamiento"),
        ("Dado de Alta", "Dado de Alta"),
        ("Dado de Baja", "Dado de Baja")
    )
    estado = forms.ChoiceField(
        label="Estado Elegido",
        choices=ESTADOS,
        required=True,
        widget=forms.Select(attrs={'class': 'form-select mb-3'})
    )

class ProfesionalForm(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre del Profesional'})
    )
    apellido = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Apellido del Profesional'})
    )
    profesion = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Profesión del Profesional'})
    )
    DIAS = (
        ("Lunes", "Lunes"),
        ("Martes", "Martes"),
        ("Miércoles", "Miércoles"),
        ("Jueves", "Jueves"),
        ("Viernes", "Viernes"),
        ("Sábado", "Sábado")
    )
    dias_atencion = forms.MultipleChoiceField(
        label="Días de Atención",
        choices=DIAS,
        required=True,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'list-unstyled'})
    )


class ConsultorioForm(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre del Consultorio'})
    )
    profesional = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Profesional del Consultorio'})
    )
    dia = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control mb-3'
        }),
        required=True,
        label='Fecha del Turno'
    )
    horario = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control mb-3'
        }),
        required=True,
        label='Horario del Turno'
    )

