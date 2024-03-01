# gsl_clientes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import GSLClientes
from .forms import ClienteForm

def lista_clientes(request):
    clientes = GSLClientes.objects.all()
    return render(request, 'gsl_clientes/lista_clientes.html', {'clientes': clientes})

def detalle_cliente(request, cliente_id):
    cliente = GSLClientes.objects.get(pk=cliente_id)
    return render(request, 'gsl_clientes/detalle_cliente.html', {'cliente': cliente})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  # Ajusta el nombre de la vista o URL a la que quieras redirigir
    else:
        form = ClienteForm()

    return render(request, 'gsl_clientes/agregar_cliente.html', {'form': form})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(GSLClientes, pk=cliente_id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('detalle_cliente', cliente_id=cliente_id)
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'gsl_clientes/editar_cliente.html', {'form': form, 'cliente': cliente})