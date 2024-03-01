# gsl_cargo/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import GSLCargo, GSLGastosCargo, GSLPapeleriaCargo
from .forms import GastoForm, PapeleriaForm, GSLCargoForm

def lista_cargas(request):
    cargas = GSLCargo.objects.all()
    return render(request, 'gsl_cargo/lista_cargas.html', {'cargas': cargas})


def detalle_carga(request, carga_id):
    carga = GSLCargo.objects.get(pk=carga_id)
    return render(request, 'gsl_cargo/detalle_carga.html', {'carga': carga})

def agregar_gasto(request, carga_id):
    carga = get_object_or_404(GSLCargo, pk=carga_id)

    if request.method == 'POST':
        form = GastoForm(request.POST, request.FILES)  # Asegúrate de incluir request.FILES para manejar archivos
        if form.is_valid():
            print("Formulario válido. Guardando...")
            gasto = form.save(commit=False)
            gasto.id_carga = carga
            gasto.id_cliente = carga.nombre_cliente
            gasto.save()
            return redirect('detalle_carga', carga_id=carga_id)
        else:
            print(form.errors)
    else:
        form = GastoForm()

    return render(request, 'gsl_cargo/agregar_gasto.html', {'form': form, 'carga': carga})


def agregar_papeleria(request, carga_id):
    carga = get_object_or_404(GSLCargo, pk=carga_id)

    if request.method == 'POST':
        form = PapeleriaForm(request.POST, request.FILES)
        if form.is_valid():
            papeleria = form.save(commit=False)
            papeleria.id_carga = carga
            papeleria.id_cliente = carga.nombre_cliente
            papeleria.save()
            return redirect('detalle_carga', carga_id=carga_id)
        else:
            print(form.errors)
    else:
        form = PapeleriaForm()

    return render(request, 'gsl_cargo/agregar_papeleria.html', {'form': form, 'carga': carga})

def agregar_carga(request):
    if request.method == 'POST':
        form = GSLCargoForm(request.POST)
        if form.is_valid():
            form.save()
            # Puedes redirigir a la página de detalles de carga o a donde desees
            return redirect('lista_cargas')
    else:
        form = GSLCargoForm()

    return render(request, 'gsl_cargo/agregar_carga.html', {'form': form})

def editar_carga(request, carga_id):
    carga = get_object_or_404(GSLCargo, pk=carga_id)

    if request.method == 'POST':
        form = GSLCargoForm(request.POST, instance=carga)
        if form.is_valid():
            form.save()
            return redirect('detalle_carga', carga_id=carga_id)
    else:
        form = GSLCargoForm(instance=carga)

    return render(request, 'gsl_cargo/editar_carga.html', {'form': form, 'carga': carga})

def lista_gastos_cargo(request, id_carga):
    carga = get_object_or_404(GSLCargo, id=id_carga)
    gastos_cargo = GSLGastosCargo.objects.filter(id_carga=carga)
    return render(request, 'gsl_cargo/lista_gastos_cargo.html', {'carga': carga, 'gastos_cargo': gastos_cargo})

def lista_papeleria_cargo(request, id_carga):
    carga = get_object_or_404(GSLCargo, id=id_carga)
    papeleria_cargo = GSLPapeleriaCargo.objects.filter(id_carga=carga)
    return render(request, 'gsl_cargo/lista_papeleria_cargo.html', {'carga': carga, 'papeleria_cargo': papeleria_cargo})