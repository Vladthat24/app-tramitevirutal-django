from django.contrib import admin

# Register your models here.
from tipodocpersonal.models import TipoDocPersonal

@admin.register(TipoDocPersonal)
class TipoDocPersonalAdmin(admin.ModelAdmin):
    pass