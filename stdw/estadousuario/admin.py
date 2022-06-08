from django.contrib import admin

# Register your models here.
from estadousuario.models import EstadoUsuario

@admin.register(EstadoUsuario)
class EstadoUsuarioAdmin(admin.ModelAdmin):
    pass