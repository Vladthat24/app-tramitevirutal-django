from django.contrib import admin

from acceso.models import Acceso
# Register your models here.
@admin.register(Acceso)
class AccesoAdmin(admin.ModelAdmin):
    list_display = ('usrccod','usrtlogin','usrccodper')
    list_filter = ('usrtestad',)
    search_fields = ('usrtlogin',)