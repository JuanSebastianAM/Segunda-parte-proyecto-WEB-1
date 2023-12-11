from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    """
    Formulario para facilitar la creación y edición de notas.
    """
   
    class Meta: 
        model = Cita

        fields = [
            'Titulo',
            'Nombre_Paciente',
            'Codigocita',  
            'fecha',
            'Nombre_Odontologo',
          
        ]

        labels = {
            'Titulo': 'Titulo',
            'Nombre_Paciente': 'Paciente',
            'fecha': 'Fecha de cita',  
            'Codigocita':'Codigo',
            'Nombre_Odontologo': 'Odontologo'
        }

        widgets = {
            
            'Titulo':forms.TextInput(attrs={'class': 'form-control'}),
            'Nombre_Paciente':forms.TextInput(attrs={'class': 'form-control'}),
            'Codigocita':forms.NumberInput(attrs={'class':'form-control'}),  
            'fecha':forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Nombre_Odontologo': forms.Select(attrs={'class': 'form-control'})
          
        }

    def __init__(self, *args, **kwargs):
        super(  CitaForm, self).__init__(*args, **kwargs)
        self.fields['Titulo'].error_messages = {'required': 'custom required message'}

        # Asegúrate de que el campo fecha esté incluido en la lista de campos
        for field in self.fields.values():
            field.error_messages = {'required': f'El campo {field.label} es obligatorio'}