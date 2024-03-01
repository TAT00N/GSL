# gsl_clientes/forms.py
from django import forms
from .models import GSLClientes

class ClienteForm(forms.ModelForm):
    class Meta:
        model = GSLClientes
        fields = ['nombre', 'correo_electronico', 'telefono']
