from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='escuderias_inicio'),
    path('listado/', views.listado, name='escuderias_listado'),

    # Mantenedor de escuderías
    path('administrar/', views.administrar_escuderias, name='administrar_escuderias'),
    path('administrar/crear/', views.crear_escuderia, name='crear_escuderia'),
    path('administrar/editar/<int:id>/', views.editar_escuderia, name='editar_escuderia'),
    path('administrar/eliminar/<int:id>/', views.eliminar_escuderia, name='eliminar_escuderia'),
]