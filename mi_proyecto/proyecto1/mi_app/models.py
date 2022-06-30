from django.db import models
# Create your models here.

class Persona(models.Model):
    rut = models.CharField(max_length=9)
    nombre = models.CharField(max_length=20)
    appaterno = models.CharField(max_length=20)
    apmaterno = models.CharField(max_length=20)
    edad = models.IntegerField(max_length=3)
    nom_vacuna = models.CharField(max_length=20)
    fecha = models.DateField