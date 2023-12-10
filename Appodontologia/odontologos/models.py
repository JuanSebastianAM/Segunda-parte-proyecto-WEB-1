from django.db import models

class Odontologo(models.Model):
    odontologo = models.CharField(max_length=200)
    imagen = models.FileField(upload_to="imagenes_odontologos/")

    def __str__(self):
        return self.odontologo
