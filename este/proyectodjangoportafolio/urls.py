from django.contrib import admin
from django.urls import path, include, reverse
from django.conf.urls.static import static
from django.conf import settings
from menu import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('crearCuenta/', views.crearCuenta, name='crearCuenta'),
    path('logout/', views.cerrarSesion, name='logout'),
    path('buscar/', views.buscar, name='search'),
    path('portfolio/', include('portafolio.urls')),
    path('blog/', include('blog.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)