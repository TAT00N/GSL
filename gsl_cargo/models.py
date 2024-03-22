# gsl_cargo/models.py
from django.db import models
from gsl_clientes.models import GSLClientes
from .utils import papeleria_upload_to, gastos_upload_to, client_directory_path

class GSLCargo(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    nombre_cliente = models.ForeignKey(GSLClientes, on_delete=models.CASCADE)
    tipo_carga = models.CharField(max_length=255, choices=[('Importacion', 'Importacion'), ('Exportacion', 'Exportacion')])
    actividad_carga = models.CharField(max_length=255, choices=[('Marítimo','Marítimo'), ('Aéreo','Aéreo'), ('Terrestre','Terrestre')])
    fecha_arribo = models.DateTimeField(blank=True, null=True)  # Permite que esté en blanco
    vencimiento_almacenaje = models.DateTimeField(blank=True, null=True)  # Permite que esté en blanco
    estado_actual = models.CharField(max_length=255, choices=[('Notificada','Notificada'), ('En proceso','En proceso'), ('Entregada','Entregada'), ('Cobrada','Cobrada')])
    bl_guia = models.CharField(max_length=255, blank=True, null=True)
    naviera = models.CharField(max_length=200, blank=True, null=True)
    demora = models.DateTimeField(blank=True, null=True)

class GSLPapeleriaCargo(models.Model):
    id_carga = models.ForeignKey(GSLCargo, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(GSLClientes, on_delete=models.CASCADE)
    tipo_papeleria = models.CharField(max_length=255)
    archivo = models.FileField(upload_to=papeleria_upload_to, null=True, blank=True)

class GSLGastosCargo(models.Model):
    id_carga = models.ForeignKey(GSLCargo, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(GSLClientes, on_delete=models.CASCADE)
    nombre_gasto = models.CharField(max_length=255)
    total_gasto = models.DecimalField(max_digits=10, decimal_places=2)
    moneda = models.CharField(max_length=3, choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GTQ', 'GTQ')])
    archivo = models.FileField(upload_to=gastos_upload_to)