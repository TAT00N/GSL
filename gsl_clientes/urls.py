from django.urls import path
from .views import lista_clientes, detalle_cliente, editar_cliente, agregar_cliente

urlpatterns = [
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('agregar_cliente/', agregar_cliente, name='agregar_cliente'),
    path('cliente/<int:cliente_id>/', detalle_cliente, name='detalle_cliente'),
    path('cliente/<int:cliente_id>/editar/', editar_cliente, name='editar_cliente'),
]
