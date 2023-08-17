from django.db import models

# Crear modelo aca
class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    estado = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['estado']
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Profesional(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    dias_atencion = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"
        ordering = ['apellido']
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Consultorio(models.Model):
    nombre = models.CharField(max_length=50)
    profesional = models.CharField(max_length=50)
    dia = models.DateField()
    horario = models.DateTimeField()
    
    class Meta:
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre}"

class Turno(models.Model):
    paciente = models.CharField(max_length=50)
    dia = models.DateField()
    horario = models.DateTimeField()
    profesional = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['dia']
    
    def __str__(self):
        return f"{self.paciente}"