from django.contrib import admin

# Register your models here.
from segpersonal.models import SegPersonal
@admin.register(SegPersonal)
class SegPersonalAdmin(admin.ModelAdmin):
    list_display = ('perccod','pertdescrip','percnumdoc','pertestad','perccoduorg','perttipo')#visualizar en el panel
    list_filter = ('perttipo','pertestad','perccoduorg') #filtrar data
    search_fields = ('percnumdoc', 'pertnombre','pertapepat','pertapemat',)#buscar informacion en una caja de texto