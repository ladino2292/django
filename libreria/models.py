from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Estudiante(models.Model):

    codigo = models.IntegerField(default=None,)
    nombre = models.CharField(default=None,max_length=100)
    apellido = models.CharField(default=None,max_length=100)
    numeroDocumento = models.CharField(default=None,max_length=10)
    numeroTelefono = models.CharField(default=None,max_length=10)
    fecha = models.DateField()
    foto = models.ImageField(upload_to='imagenes/',null=True)
    semestre = models.IntegerField(default=None,validators=[MinValueValidator(1),MaxValueValidator(10)])
    promedio = models.FloatField(default=None,validators=[MinValueValidator(0.00),MaxValueValidator(5.00)])
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        fila = "apellido: "+ self.apellido + " - " + "numero documento: " +self.numeroDocumento
        return fila

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.imagen.name)
        super().delete()

class Salas(models.Model):

    edificio =models.IntegerField(default=None,validators=[MinValueValidator(10),MaxValueValidator(20)])
    salas_numero=models.IntegerField(default=None,validators=[MinValueValidator(100),MaxValueValidator(500)])
    monitor=models.CharField(default=None,max_length=100)
    fecha= models.DateField(default=None,)
    hora=models.TimeField(default=None,)
    codigo_monitor = models.IntegerField(default=None,validators=[MinValueValidator(10),MaxValueValidator(11)])
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo