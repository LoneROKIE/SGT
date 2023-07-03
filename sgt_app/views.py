from django.shortcuts import render, redirect
from .models import Tarea

# Create your views here.

# vista para crear una tarea
def crear_tarea(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombreTarea')
        descripcion = request.POST.get('descripcionTarea')
        fecha_inicio = request.POST.get('fechaInicio')
        fecha_vencimiento = request.POST.get('fechaFinalizacion')
        estado = request.POST.get('estado')
        # creamos el objeto
        tarea = Tarea(nombre = nombre, descripcion = descripcion, fecha_creacion = fecha_inicio, fecha_vencimiento = fecha_vencimiento, estado = estado)
        # los guardamos
        tarea.save()
        
    return render(request, 'html/createTask.html')

# vista para ver las tareas, esta va a funcionar como la vista principal
def ver_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'html/viewTasks.html', {'tareas': tareas})

# vista para editar una tarea
# vista para editar una tarea
def editar_tareas(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    
    if request.method == 'POST':
        # Obtén los datos actualizados del formulario
        nombre = request.POST.get('nombreTarea')
        descripcion = request.POST.get('descripcionTarea')
        fecha_inicio = request.POST.get('fechaInicio')
        fecha_vencimiento = request.POST.get('fechaFinalizacion')
        estado = request.POST.get('estado')
        
        # Actualiza los campos de la tarea existente
        tarea.nombre = nombre
        tarea.descripcion = descripcion
        tarea.fecha_creacion = fecha_inicio
        tarea.fecha_vencimiento = fecha_vencimiento
        tarea.estado = estado
        
        # Guarda los cambios
        tarea.save()
        
        # Redirige a la vista de tareas después de la edición
        return redirect('ver_tareas')
    
    # Si el método es GET, renderiza el formulario de edición
    return render(request, 'html/editTask.html', {'tarea': tarea})

    