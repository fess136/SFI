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


class Presentacion(models.Model):
    descripcion = models.CharField(max_length=150, verbose_name="Descripcion")
    
    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = "Presentación"
        verbose_name_plural = "Presentaciones"
        db_table = "Presentacion"


class Marcas(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    estado = models.BooleanField(default = True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        db_table = "Marca"


class Unidad_Medida(models.Model):
    descripcion = models.CharField(max_length=50, verbose_name="Descripcion")
    
    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medida"
        db_table = "Unidad_Medida"


class Proveedores(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    nit = models.CharField(max_length = 20, unique = True, verbose_name = "NIT")
    ubicacion = models.CharField(max_length = 255, verbose_name = "Ubicacion")
    telefono = models.CharField(max_length = 20, verbose_name = "Telefono")
    correo_electronico = models.EmailField(max_length=100, verbose_name = "Correo Electronico")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        db_table = "Proveedores"