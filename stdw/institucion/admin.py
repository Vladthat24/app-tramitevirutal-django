from django.contrib import admin

# Register your models here.
from institucion.models import Institucion

@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
    pass
