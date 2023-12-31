from django.db import models

# Create your models here.
"""Modelo de la Tabla de tareas"""
class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    fecha_creacion = models.DateField()
    fecha_vencimiento = models.DateField()
    ESTADO_CHOICES = (
    ('completada','Completada'),
    ('incompleta','Incompleta'),
    )
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='incompleta')
    def __str__(self):
        return f"Tarea: \nTitulo: {self.nombre},\nDescripcion: {self.descripcion},\nFecha Creacion: {self.fecha_creacion},\nFecha Vencimiento: {self.fecha_vencimiento},\nEstado: {self.estado}"