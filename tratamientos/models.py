from email.headerregistry import ContentDispositionHeader
from ssl import create_default_context
from django.db import models

# Create your models here.

class Tratamiento(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='tratamiento'
        verbose_name_plural='tratamientos'

def __str__(self):
    return self.titulo