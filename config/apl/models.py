
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import*
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db.models.signals import post_delete
from django.dispatch import receiver

def validacion_telefono(value):

    if len(str(value)) != 10:

        raise ValidationError("se deben ingresar 10 digitos")

class Tipo(models.Model):
    nombre=models.CharField(max_length=150, verbose_name="Nombre", unique=True, null=True)
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
    class TipoDocumento(models.TextChoices):
        CC = 'CC', 'Cédula de Ciudadanía'
        CE = 'CE', 'Cédula de Extranjería'
       
        

    # def validar_numero_documento(value):
    #     if value < 10000000 or value > 9999999999:
    #         raise ValidationError("El número de documento debe tener entre 8 y 10 dígitos")

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='administrador')
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    numero_documento = models.PositiveIntegerField(verbose_name="Número de documento", unique=True)
    telefono = models.PositiveIntegerField(verbose_name="Teléfono")
    contrasena = models.CharField(max_length=128, validators=[MinLengthValidator(8)], verbose_name="Contraseña")
    conf_contrasena = models.CharField(max_length=128, verbose_name="Confirmación de contraseña", default="")

    def clean(self):
        super().clean()
        if self.contrasena != self.conf_contrasena:
            raise ValidationError({"conf_contrasena": "Las contraseñas no coinciden"})

    def _str_(self):
        return self.nombre

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
        db_table = 'Administrador'

@receiver(post_delete, sender=Administradores)
def eliminar_usuario_relacionado(sender, instance, **kwargs):
    user = instance.user
    if user:
        user.delete()
        

class Clientes(models.Model):
    nombre=models.CharField(max_length=150, verbose_name="Nombre")
    apellido=models.CharField(max_length=150, verbose_name="Apellido")
    nit=models.PositiveBigIntegerField(verbose_name="Numero de Identificacion",unique=True, validators=[validacion_telefono])
    correo_electronico=models.EmailField(max_length=150,verbose_name="Email")
    telefono=models.PositiveIntegerField(verbose_name="Telefono", validators=[validacion_telefono])
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


# SE MODIFICO EL TIPO DE DATO DE PRECIO PARA QUE SE LE PUDIERA DAR FORMATO      
class Productos(models.Model):
    
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    precio = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Precio")
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
    metodo_pago =models.ForeignKey(Metodo_Pago,on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedores,on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.id}"
    
    class Meta:
        verbose_name ="Compra"
        verbose_name_plural ="Compras"
        db_table ="Compra"

class DetalleCompra(models.Model):

    compra = models.ForeignKey(Compras, on_delete=models.PROTECT, default=1)
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad", null=True)
    producto = models.ForeignKey(Productos,on_delete=models.PROTECT)

    def precio(self):

        return Productos.objects.get(id=DetalleCompra.objects.get(id=self.id).producto.id).precio
        


class Ventas(models.Model):
    fecha_venta=models.DateTimeField(verbose_name="Fecha De Venta",auto_now=True)
    producto = models.ForeignKey(Productos,on_delete=models.PROTECT)
    ventas_cantidad= models.PositiveSmallIntegerField(verbose_name="Cantidad")
    empleado= models.ForeignKey(Empleados,on_delete=models.PROTECT,null=True)
    cliente = models.ForeignKey(Clientes,on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.fecha_venta}"
    #EN ESTA FUNCION SE HACE LA OPERACION PARA EL TOTAL 
    def calcular_total(self):
        return self.ventas_cantidad * self.producto.precio
    class Meta:
        verbose_name ="Venta"
        verbose_name_plural ="Ventas"
        db_table ="Venta"
