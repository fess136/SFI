from django.db import models
from django.utils import*
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
    estado = models.BooleanField(default = True)
    
    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medida"
        db_table = "Unidad_Medida"


class Proveedores(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    nit = models.CharField(max_length = 20, unique = True, verbose_name = "Nit/Cedula")
    ubicacion = models.CharField(max_length = 255, verbose_name = "Ubicacion")
    telefono = models.PositiveIntegerField( verbose_name = "Telefono")
    correo_electronico = models.EmailField(max_length=100, verbose_name = "Correo Electronico")
    
    
    def __str__(self):
        return self.apellido
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        db_table = "Proveedores"

    
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
    edad=models.PositiveIntegerField(verbose_name="Edad")
    cedula=models.PositiveBigIntegerField(verbose_name="Cedula",unique=True)
    correo_electronico=models.EmailField(verbose_name="Email", blank = False)
    
    def __str__(self):
        return self.nombre
    

    class Meta:
        
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
        db_table="Administrador"

        

class Clientes(models.Model):
    nombre=models.CharField(max_length=150, verbose_name="Nombre")
    apellido=models.CharField(max_length=150, verbose_name="Apellido")
    nit=models.PositiveBigIntegerField(verbose_name="Nit",unique=True)
    correo_electronico=models.EmailField(max_length=150,verbose_name="Email")
    telefono=models.PositiveIntegerField(verbose_name="Telefono")
    Tipo_identificador=models.ForeignKey(Tipo_identificador, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural ="Clientes"
        db_table ="Cliente"



class Empleados(models.Model):

    nombre=models.CharField(max_length=100, verbose_name="Nombre")
    apellido=models.CharField(max_length=100, verbose_name="Apellido")
    edad=models.PositiveIntegerField(verbose_name="Edad")
    cedula=models.PositiveBigIntegerField(verbose_name="Cedula",unique=True)
    correo_electronico=models.CharField(max_length=100,verbose_name="Email")

    def __str__(self):
        return self.nombre
    
    
    class Meta:
        
        verbose_name = "Empleados"
        verbose_name_plural = "Empleados"
        db_table="Empleados"


        
class Productos(models.Model):
    
    nombre = models.CharField(max_length=100,verbose_name="Productos")
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    precio = models.FloatField(verbose_name="Precio")
    marcas = models.ForeignKey(Marcas,on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)
    presentacion= models.ForeignKey(Presentacion,on_delete=models.CASCADE)
    unidad_medida=models.ForeignKey(Unidad_Medida,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
        db_table = "Producto"
        
class Metodo_Pago(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name ="Metodo de pago"
        verbose_name_plural ="Metodos de pagos"
        db_table ="Metodo de pago"




class Compras(models.Model):
    fecha_compra =models.DateField(verbose_name="Fecha De Compra",auto_now=True)
    metodo_pago =models.ForeignKey(Metodo_Pago,on_delete=models.PROTECT.)
    producto = models.ForeignKey(Productos,on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedores,on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.fecha_compra}"
    
    class Meta:
        verbose_name ="Compra"
        verbose_name_plural ="Compras"
        db_table ="Compra"
        
class Ventas(models.Model):
    fecha_venta=models.DateTimeField(verbose_name="Fecha De Venta",auto_now=True)
    producto = models.ForeignKey(Productos,on_delete=models.PROTECT)
    empleado= models.ForeignKey(Empleados,on_delete=models.PROTECT,null=True)
    cliente = models.ForeignKey(Clientes,on_delete=models.PROTECT)
    administrador = models.ForeignKey(Administradores,on_delete=models.PROTECT ,default="no")
    
    def __str__(self):
        return f"{self.fecha_venta}"
    
    class Meta:
        verbose_name ="Venta"
        verbose_name_plural ="Ventas"
        db_table ="Venta"


# class Detalle_venta(models.Model):
    