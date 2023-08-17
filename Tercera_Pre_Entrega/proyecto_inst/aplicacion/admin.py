from django.contrib import admin
from .models import *

# Registrar modelos aqui
admin.site.register(Profesional)
admin.site.register(Paciente)
admin.site.register(Turno)
admin.site.register(Consultorio)
