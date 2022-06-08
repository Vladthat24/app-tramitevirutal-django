from django.contrib import admin

# Register your models here.
from unidorg.models import UnidOrg

@admin.register(UnidOrg)
class UnidOrgAdmin(admin.ModelAdmin):
    list_display = ('uorgccod','uorgtdescrip')