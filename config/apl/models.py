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
    
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Tipo Identificador"
        verbose_name_plural = "Tipos Identificadores"
        db_table = "Tipo_identificador"
        
        
class Administradores(models.Model):
    
    nombre=models.CharField(max_length=150, verbose_name="Nombre")
    apellido=models.CharField(max_length=150, verbose_name="Apellido")
    edad=models.IntegerField(max_length=150,verbose_name="Edad")
    cedula=models.BigIntegerField(max_length=15,verbose_name="Cedula",unique=True)
    correo_electronico=models.CharField(max_length=150,verbose_name="Email")
    
    def __str__(self):
       return self.nombre
    

    class Meta:
        
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
        db_table="Administrador"

        

class clientes(models.Model):
    nombre=models.CharField(max_length=150, verbose_name="Nombre")
    apellido=models.CharField(max_length=150, verbose_name="Apellido")
    nit=models.BigIntegerField(max_length=15,verbose_name="Nit",unique=True)
    correo_electronico=models.CharField(max_length=150,verbose_name="Email")
    telefono=models.IntegerField(max_length=150,verbose_name="Telefono")
    Tipo_identificador=models.ForeignKey(Tipo_identificador, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural ="Clientes"
        db_table ="Cliente"



class Empleados(models.Model):

    nombre=models.CharField(max_length=150, verbose_name="Nombre")
    apellido=models.CharField(max_length=150, verbose_name="Apellido")
    edad=models.IntegerField(max_length=150,verbose_name="Edad")
    cedula=models.BigIntegerField(max_length=15,verbose_name="Cedula",unique=True)
    correo_electronico=models.CharField(max_length=150,verbose_name="Email")

    def __str__(self):
       return self.nombre
    
    
    class Meta:
        
        verbose_name = "Empleados"
        verbose_name_plural = "Empleados"
        db_table="Empleados"


        


    

