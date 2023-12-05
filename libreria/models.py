from django.db import models


class Estudiante(models.Model):

    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    numeroDocumento = models.CharField(default=None,max_length=30)
    apellido = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo

