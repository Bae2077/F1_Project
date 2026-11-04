from django.shortcuts import render, get_object_or_404
from .models import ParticipacionPiloto, Temporada
from django.shortcuts import redirect
from django.contrib import messages
from .models import Piloto
from .forms import PilotoForm
from usuarios.decorators import permiso_requerido
from .forms import PilotoForm, ParticipacionPilotoForm, TemporadaForm

def obtener_participaciones():
    return ParticipacionPiloto.objects.select_related(
        "piloto",
        "escuderia",
        "temporada"
    ).filter(
        temporada__anio=2026
    )


def inicio(request):
    return render(request, 'pilotos/inicio.html')

def listado(request):
    participaciones = obtener_participaciones()

    busqueda = request.GET.get("q", "").strip()

    if busqueda:
        participaciones = participaciones.filter(
            piloto__nombre__icontains=busqueda
        )

    return render(
        request,
        "pilotos/listado.html",
        {
            "participaciones": participaciones,
            "busqueda": busqueda
        }
    )

def temporadas(request):
    temporadas = Temporada.objects.all()

    return render(
        request,
        "pilotos/temporadas.html",
        {
            "temporadas": temporadas
        }
    )


def detalle_temporada(request, anio):
    temporada = get_object_or_404(Temporada, anio=anio)

    participaciones = ParticipacionPiloto.objects.select_related(
        "piloto",
        "escuderia"
    ).filter(
        temporada=temporada
    )

    return render(
        request,
        "pilotos/detalle_temporada.html",
        {
            "temporada": temporada,
            "participaciones": participaciones
        }
    )

@permiso_requerido('pilotos.view_piloto')
def administrar_pilotos(request):
    pilotos = Piloto.objects.all()

    busqueda = request.GET.get('q', '').strip()

    if busqueda:
        pilotos = pilotos.filter(nombre__icontains=busqueda)

    return render(request, 'pilotos/administrar_pilotos.html', {
        'pilotos': pilotos,
        'busqueda': busqueda
    })


@permiso_requerido('pilotos.add_piloto')
def crear_piloto(request):
    if request.method == 'POST':
        form = PilotoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Piloto creado correctamente.')
            return redirect('administrar_pilotos')
    else:
        form = PilotoForm()

    return render(request, 'pilotos/formulario_piloto.html', {
        'form': form,
        'titulo': 'Registrar piloto'
    })


@permiso_requerido('pilotos.change_piloto')
def editar_piloto(request, id):
    piloto = get_object_or_404(Piloto, id=id)

    if request.method == 'POST':
        form = PilotoForm(request.POST, instance=piloto)

        if form.is_valid():
            form.save()
            messages.success(request, 'Piloto actualizado correctamente.')
            return redirect('administrar_pilotos')
    else:
        form = PilotoForm(instance=piloto)

    return render(request, 'pilotos/formulario_piloto.html', {
        'form': form,
        'titulo': 'Editar piloto'
    })


@permiso_requerido('pilotos.delete_piloto')
def eliminar_piloto(request, id):
    piloto = get_object_or_404(Piloto, id=id)

    if request.method == 'POST':
        piloto.delete()
        messages.success(request, 'Piloto eliminado correctamente.')

    return redirect('administrar_pilotos')

@permiso_requerido('pilotos.add_participacionpiloto')
def crear_participacion(request):
    if request.method == 'POST':
        form = ParticipacionPilotoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Participación registrada correctamente.'
            )
            return redirect('administrar_participaciones')
    else:
        form = ParticipacionPilotoForm()

    return render(request, 'pilotos/formulario_participacion.html', {
        'form': form,
        'titulo': 'Registrar participación'
    })

@permiso_requerido('pilotos.view_participacionpiloto')
def administrar_participaciones(request):
    participaciones = ParticipacionPiloto.objects.select_related(
        'piloto',
        'escuderia',
        'temporada'
    ).all()

    return render(
        request,
        'pilotos/administrar_participaciones.html',
        {
            'participaciones': participaciones
        }
    )

@permiso_requerido('pilotos.change_participacionpiloto')
def editar_participacion(request, id):
    participacion = get_object_or_404(ParticipacionPiloto, id=id)

    if request.method == 'POST':
        form = ParticipacionPilotoForm(request.POST, instance=participacion)

        if form.is_valid():
            form.save()
            messages.success(request, 'Participación actualizada correctamente.')
            return redirect('administrar_participaciones')
    else:
        form = ParticipacionPilotoForm(instance=participacion)

    return render(request, 'pilotos/formulario_participacion.html', {
        'form': form,
        'titulo': 'Editar participación'
    })


@permiso_requerido('pilotos.delete_participacionpiloto')
def eliminar_participacion(request, id):
    participacion = get_object_or_404(ParticipacionPiloto, id=id)

    if request.method == 'POST':
        participacion.delete()
        messages.success(request, 'Participación eliminada correctamente.')
        return redirect('administrar_participaciones')

    return render(request, 'pilotos/confirmar_eliminar_participacion.html', {
        'participacion': participacion
    })

@permiso_requerido('pilotos.add_temporada')
def crear_temporada(request):
    if request.method == 'POST':
        form = TemporadaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Temporada creada correctamente.')
            return redirect('temporadas')
    else:
        form = TemporadaForm()

    return render(request, 'pilotos/formulario_temporada.html', {
        'form': form,
        'titulo': 'Registrar temporada'
    })


@permiso_requerido('pilotos.change_temporada')
def editar_temporada(request, id):
    temporada = get_object_or_404(Temporada, id=id)

    if request.method == 'POST':
        form = TemporadaForm(request.POST, instance=temporada)

        if form.is_valid():
            form.save()
            messages.success(request, 'Temporada actualizada correctamente.')
            return redirect('temporadas')
    else:
        form = TemporadaForm(instance=temporada)

    return render(request, 'pilotos/formulario_temporada.html', {
        'form': form,
        'titulo': 'Editar temporada'
    })


@permiso_requerido('pilotos.delete_temporada')
def eliminar_temporada(request, id):
    temporada = get_object_or_404(Temporada, id=id)

    if request.method == 'POST':
        temporada.delete()
        messages.success(request, 'Temporada eliminada correctamente.')
        return redirect('temporadas')

    return render(request, 'pilotos/confirmar_eliminar_temporada.html', {
        'temporada': temporada
    })
