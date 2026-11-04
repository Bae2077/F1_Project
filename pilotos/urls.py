from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='pilotos_inicio'),
    path('listado/', views.listado, name='pilotos_listado'),
    path('temporadas/', views.temporadas, name='temporadas'),
    path('temporadas/<int:anio>/', views.detalle_temporada, name='detalle_temporada'),

    # Mantenedor de pilotos
    path('administrar/', views.administrar_pilotos, name='administrar_pilotos'),
    path('administrar/crear/', views.crear_piloto, name='crear_piloto'),
    path('administrar/editar/<int:id>/', views.editar_piloto, name='editar_piloto'),
    path('administrar/eliminar/<int:id>/', views.eliminar_piloto, name='eliminar_piloto'),

    # Transacción: participaciones de pilotos
    path('participaciones/', views.administrar_participaciones, name='administrar_participaciones'),
    path('participaciones/crear/', views.crear_participacion, name='crear_participacion'),
]