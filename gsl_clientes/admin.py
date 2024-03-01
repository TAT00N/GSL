from django.contrib import admin
from .models import GSLClientes

class GSLClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo_electronico', 'telefono', 'fecha_creacion')
    search_fields = ('nombre', 'correo_electronico', 'telefono')

admin.site.register(GSLClientes, GSLClientesAdmin)
