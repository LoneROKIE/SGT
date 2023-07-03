# modulo de las urls de la aplicacion
from django.urls import path
from . import views

urlpatterns = [
    path('crearTarea/', views.crear_tarea, name='crearTarea'),
    path('', views.ver_tareas, name='ver_tareas'),
    path('editarTarea/<int:tarea_id>/', views.editar_tareas, name='editarTarea'),
]