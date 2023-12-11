from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.CitasIndex, name='CitasIndex'),
    path('gestion/',views.gestionCitas, name='gestionCitas'),
    path('crear/',views.crearCitas, name='crearCitas'),
    path('detalle/<id>/',views.detalleCitas, name='detalleCitas'),
    path('editar/<id>/',views.editarCitas, name='editarCitas'),
    path('borrar/<id>/',views.eliminarCitas, name='eliminarCitas'),
    path('ver/<int:cita_id>/', views.verCitas, name='verCitas'),
]