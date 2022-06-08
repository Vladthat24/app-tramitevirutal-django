from django.contrib import admin

# Register your models here.
from proceinstitucion.models import ProceInstitucion

@admin.register(ProceInstitucion)
class ProceInstitucion(admin.ModelAdmin):
    pass
