from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.iniciar_sesion, name='usuarios_login'),
    path('logout/', views.cerrar_sesion, name='usuarios_logout'),
    path('dashboard/', views.dashboard, name='usuarios_dashboard'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('listar/', views.listar_usuarios, name='listar_usuarios'),

    # Recuperación de contraseña
    path(
        'recuperar/',
        auth_views.PasswordResetView.as_view(
            template_name='usuarios/password_reset.html',
            email_template_name='usuarios/password_reset_email.html',
            subject_template_name='usuarios/password_reset_subject.txt',
        ),
        name='password_reset'
    ),
    path(
        'recuperar/enviado/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='usuarios/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'recuperar/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='usuarios/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'recuperar/completado/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='usuarios/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]
