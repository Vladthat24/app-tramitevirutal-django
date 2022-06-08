from django.contrib import admin
from anexo.models import Anexo


# Register your models here.
@admin.register(Anexo)
class AnexoAdmin(admin.ModelAdmin):
    list_display = ('idanexo','num_anexo','direc_ip','marctelf','model','estado','fechinstal','fechcambio','observ','fechreg')
    list_filter = ('num_anexo','direc_ip','estado','marctelf')
    search_fields = ('num_anexo','direc_ip','marctelf','model')
