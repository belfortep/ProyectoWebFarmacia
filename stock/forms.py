from django import forms

class DateInput(forms.DateInput):
    input_type= 'date'

class FormularioFarmacia(forms.Form):
    fecha = forms.DateField(label='Fecha', widget=DateInput)
    cantidad = forms.IntegerField(label='Cantidad')

class FormularioCreacion(forms.Form):
    fecharda = forms.DateField(label='fecharda', widget=DateInput, required=False)
    cantidad = forms.IntegerField(label='cantidad')
    nombreArticulo = forms.CharField(label='nombreArticulo', widget=forms.Textarea)
    
    
    
    