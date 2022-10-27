from django.contrib import admin
from .models import Proyecto, InformacionUsuario

# Register your models here.
admin.site.register(Proyecto)
admin.site.register(InformacionUsuario)