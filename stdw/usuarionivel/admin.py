from django.contrib import admin

# Register your models here.
from usuarionivel.models import UsuarioNivel

@admin.register(UsuarioNivel)
class UsuarioNivelAdmin(admin.ModelAdmin):
    pass