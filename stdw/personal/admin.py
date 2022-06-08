from django.contrib import admin

# Register your models here.
from personal.models import Personal

@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('perccod','pertdescrip','percnumdoc','pertestad','perccoduorg')#visualizar en el panel
    list_filter = ('pertestad','perccoduorg') #filtrar data
    search_fields = ('percnumdoc', 'pertnombre','pertapepat','pertapemat',)#buscar informacion en una caja de texto