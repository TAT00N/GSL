# gsl_cargo/forms.py
from django import forms
from .models import GSLGastosCargo, GSLPapeleriaCargo, GSLCargo

class GastoForm(forms.ModelForm):
    class Meta:
        model = GSLGastosCargo
        fields = ['nombre_gasto', 'total_gasto', 'moneda', 'archivo']
        widgets = {
            'archivo': forms.ClearableFileInput(attrs={'accept': '.pdf, .doc, .docx, .jpg, .jpeg, .png'}),
        }

class PapeleriaForm(forms.ModelForm):
    class Meta:
        model = GSLPapeleriaCargo
        fields = ['tipo_papeleria', 'archivo']
        widgets = {
            'archivo': forms.ClearableFileInput(attrs={'accept': '.pdf, .doc, .docx, .jpg, .jpeg, .png'}),
        }
        
class GSLCargoForm(forms.ModelForm):
    class Meta:
        model = GSLCargo
        fields = ['nombre_cliente', 'tipo_carga', 'actividad_carga', 'fecha_arribo', 'vencimiento_almacenaje', 'estado_actual', 'bl_guia', 'naviera', 'demora']

    widgets = {
        'fecha_arribo': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        'vencimiento_almacenaje': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
