from django.db import models

# Create your models here.
class Tipo(models.Model):
    nombre=models.CharField(max_length=150, verbose_name="Nombre")
    estado=models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        db_table = "Tipo"
    
class Tipo_identificador(models.Model):
    nombre=models.CharField(max_length=150, verbose_name="Nombre")
    