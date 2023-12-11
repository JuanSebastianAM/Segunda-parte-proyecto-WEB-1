from django.db import models

class Odontologo(models.Model):
    odontologo = models.CharField(max_length=200)
    
    def __str__(self):
        return self.odontologo
