from django import forms
from .models import Odontologo

class NotaForm(forms.ModelForm):
    """
    Formulario para facilitar la creación y edición de notas.
    """

    class Meta: 
        model = Odontologo

        fields = [
            'Odontologo',
            'Imagen',
             
        ]

        labels = {
           
            'Odontologo': 'Odontologo',
            'Imagen': 'Imagen',  
        }

        widgets = {
            'Odontologo': forms.TextInput(attrs={'class': 'form-control'}),
            'Imagen': forms.FileInput(attrs={'class':'form-control'})
            
        }

    def __init__(self, *args, **kwargs):
        super(NotaForm, self).__init__(*args, **kwargs)
        self.fields['Odontologo'].error_messages = {'required': 'custom required message'}

        # Asegúrate de que el campo fecha esté incluido en la lista de campos
        for field in self.fields.values():
            field.error_messages = {'required': f'El campo {field.label} es obligatorio'}