# gsl_cargo/urls.py
from django.urls import path
from .views import lista_cargas, detalle_carga, agregar_gasto, agregar_papeleria, editar_carga, agregar_carga, lista_gastos_cargo, lista_papeleria_cargo

urlpatterns = [
    path('cargas/', lista_cargas, name='lista_cargas'),
    path('agregar_carga/', agregar_carga, name='agregar_carga'),
    path('carga/<int:carga_id>/', detalle_carga, name='detalle_carga'),
    path('carga/<int:carga_id>/editar/', editar_carga, name='editar_carga'),
    path('carga/<int:carga_id>/agregar_gasto/', agregar_gasto, name='agregar_gasto'),
    path('carga/<int:carga_id>/agregar_papeleria/', agregar_papeleria, name='agregar_papeleria'),
    path('carga/<int:id_carga>/lista_gastos_cargo/', lista_gastos_cargo, name='lista_gastos_cargo'),
    path('carga/<int:id_carga>/lista_papeleria_cargo/', lista_papeleria_cargo, name='lista_papeleria_cargo'),
]

