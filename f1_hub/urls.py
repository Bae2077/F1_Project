from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('pilotos_inicio')),
    path('pilotos/', include('pilotos.urls')),
    path('escuderias/', include('escuderias.urls')),
    path('usuarios/', include('usuarios.urls')),
]