from django.db import models


class Familiares(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha = models.DateField()
    correo = models.EmailField()

    def __str__(self):
        return f'nombre: {self.nombre}, edad: {self.edad}, fecha: {self.fecha}, correo: {self.correo}'