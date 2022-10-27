from django.urls import path
from .views import Perfil, crearProyecto, proyecto_detalle, eliminarProyecto,modificarProyecto, modificarPerfil
app_name = 'portfolio'

urlpatterns = [
    path('', Perfil, name='perfil'),
    path('agregarProyecto', crearProyecto, name='agregarProyecto'),
    path('<int:proyecto_id>', proyecto_detalle, name='proyectoDetalle'),
    path('<int:proyecto_id>/delete', eliminarProyecto, name='eliminarProyecto'),
    path('<int:proyecto_id>/modificar', modificarProyecto, name='modificarProyecto'),
    path('<int:user_id>/modificarPerfil', modificarPerfil, name='modificarPerfil')
]