# gsl_cargo/utils.py
import os
from django.db import models
from gsl_clientes.models import GSLClientes

# Funciones para construir rutas de almacenamiento
def papeleria_upload_to(instance, filename):
    return os.path.join('papeleria_cargos', str(instance.id_cliente.id), filename)

def gastos_upload_to(instance, filename):
    return os.path.join('gastos_cargos', str(instance.id_cliente.id), filename)

def client_directory_path(instance, filename):
    return f'clientes/{instance.id_cliente.nombre}/{instance.tipo_papeleria}/{filename}'
