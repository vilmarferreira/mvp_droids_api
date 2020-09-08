from django.contrib import admin
from .models import Demanda
from django.utils.html import format_html

# Register your models here.
class DemandaAdmin(admin.ModelAdmin):
    list_display = ('id','descricao','endereco','contato','anunciante','finalizado')

admin.site.register(Demanda,DemandaAdmin)