from django.db import models
from odontologos.models import Odontologo  

class Cita(models.Model):
    Titulo = models.CharField(max_length=100)
    Nombre_Paciente = models.CharField(max_length=200)
    Codigocita = models.PositiveSmallIntegerField()
    fecha = models.DateTimeField(null=True, blank=True)
    Nombre_Odontologo = models.ForeignKey(Odontologo, on_delete=models.CASCADE, related_name='citas')

    def __str__(self):
        return self.Titulo
