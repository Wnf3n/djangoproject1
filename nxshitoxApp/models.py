from django.db import models

# Create your models here.

class Persona(models.Model):
    rut=models.CharField(primary_key=True, max_length=12)
    nombre=models.TextField(max_length=255)
    edad=models.IntegerField(null=True)
    genero=models.CharField(max_length=1)