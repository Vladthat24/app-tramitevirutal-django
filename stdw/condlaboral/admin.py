from django.contrib import admin

# Register your models here.
from condlaboral.models import CondLaboral

@admin.register(CondLaboral)
class CondLaboralAdmin(admin.ModelAdmin):
    list_display = ('tipperccod','tippertdescrip','tippertestad')
    list_filter = ('tipperccod','tippertdescrip','tippertestad')