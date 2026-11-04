from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.iniciar_sesion, name='usuarios_login'),
    path('logout/', views.cerrar_sesion, name='usuarios_logout'),
    path('dashboard/', views.dashboard, name='usuarios_dashboard'),
]