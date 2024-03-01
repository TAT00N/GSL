from django.contrib import admin
from .models import GSLCargo, GSLPapeleriaCargo, GSLGastosCargo

class GSLPapeleriaCargoInline(admin.TabularInline):
    model = GSLPapeleriaCargo
    extra = 1

class GSLGastosCargoInline(admin.TabularInline):
    model = GSLGastosCargo
    extra = 1

class GSLCargoAdmin(admin.ModelAdmin):
    inlines = [GSLPapeleriaCargoInline, GSLGastosCargoInline]
    list_display = ('nombre_cliente', 'tipo_carga', 'actividad_carga', 'fecha_arribo', 'vencimiento_almacenaje', 'estado_actual')
    list_filter = ('nombre_cliente', 'tipo_carga', 'actividad_carga', 'estado_actual')
    search_fields = ('nombre_cliente__nombre', 'estado_actual')

class GSLPapeleriaCargoAdmin(admin.ModelAdmin):
    list_display = ('id_carga', 'id_cliente', 'tipo_papeleria')
    list_filter = ('id_cliente', 'tipo_papeleria')
    search_fields = ('id_cliente__nombre', 'tipo_papeleria')

class GSLGastosCargoAdmin(admin.ModelAdmin):
    list_display = ('id_carga', 'id_cliente', 'nombre_gasto', 'total_gasto')
    list_filter = ('id_cliente', 'nombre_gasto')
    search_fields = ('id_cliente__nombre', 'nombre_gasto')

admin.site.register(GSLCargo, GSLCargoAdmin)
admin.site.register(GSLPapeleriaCargo, GSLPapeleriaCargoAdmin)
admin.site.register(GSLGastosCargo, GSLGastosCargoAdmin)
