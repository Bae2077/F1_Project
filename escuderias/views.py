from django.shortcuts import render
from django.db.models import Q
from .models import Escuderia
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .forms import EscuderiaForm
from usuarios.decorators import permiso_requerido

# Vistas de la app escuderias

def inicio(request):
    return render(request, 'escuderias/inicio.html')


def listado(request):
    escuderias = Escuderia.objects.all()

    busqueda = request.GET.get("q", "").strip()

    if busqueda:
        escuderias = escuderias.filter(
            Q(nombre__icontains=busqueda) |
            Q(pais__icontains=busqueda)
        )

    return render(request, 'escuderias/listado.html', {
        'escuderias': escuderias,
        'busqueda': busqueda
    })

@permiso_requerido('escuderias.view_escuderia')
def administrar_escuderias(request):
    escuderias = Escuderia.objects.all()

    busqueda = request.GET.get('q', '').strip()

    if busqueda:
        escuderias = escuderias.filter(
            Q(nombre__icontains=busqueda) |
            Q(pais__icontains=busqueda)
        )

    return render(request, 'escuderias/administrar_escuderias.html', {
        'escuderias': escuderias,
        'busqueda': busqueda
    })


@permiso_requerido('escuderias.add_escuderia')
def crear_escuderia(request):
    if request.method == 'POST':
        form = EscuderiaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Escudería creada correctamente.')
            return redirect('administrar_escuderias')
    else:
        form = EscuderiaForm()

    return render(request, 'escuderias/formulario_escuderia.html', {
        'form': form,
        'titulo': 'Registrar escudería'
    })


@permiso_requerido('escuderias.change_escuderia')
def editar_escuderia(request, id):
    escuderia = get_object_or_404(Escuderia, id=id)

    if request.method == 'POST':
        form = EscuderiaForm(request.POST, instance=escuderia)

        if form.is_valid():
            form.save()
            messages.success(request, 'Escudería actualizada correctamente.')
            return redirect('administrar_escuderias')
    else:
        form = EscuderiaForm(instance=escuderia)

    return render(request, 'escuderias/formulario_escuderia.html', {
        'form': form,
        'titulo': 'Editar escudería'
    })


@permiso_requerido('escuderias.delete_escuderia')
def eliminar_escuderia(request, id):
    escuderia = get_object_or_404(Escuderia, id=id)

    if request.method == 'POST':
        escuderia.delete()
        messages.success(request, 'Escudería eliminada correctamente.')

    return redirect('administrar_escuderias')