from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UsuarioForm
from usuarios.decorators import permiso_requerido

def obtener_perfil(usuario):
    if usuario.groups.filter(name='Administrador').exists():
        return 'Administrador'

    elif usuario.groups.filter(name='Supervisor').exists():
        return 'Supervisor'

    elif usuario.groups.filter(name='Administrativo').exists():
        return 'Administrativo'

    return 'Usuario'


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('usuarios_dashboard')

        messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'usuarios/login.html')


@login_required
def cerrar_sesion(request):
    if request.method == 'POST':
        logout(request)
        return redirect('pilotos_inicio')

    return redirect('usuarios_dashboard')


@login_required
def dashboard(request):
    perfil = obtener_perfil(request.user)

    return render(request, 'usuarios/dashboard.html', {
        'perfil': perfil
    })

@permiso_requerido('auth.add_user')
def crear_usuario(request):

    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado correctamente.')
            return redirect('crear_usuario')

    else:
        form = UsuarioForm()

    return render(request, 'usuarios/crear_usuario.html', {
        'form': form
    })