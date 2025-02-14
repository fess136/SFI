
from decimal import Decimal
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import*
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db.models.signals import post_delete
from django.dispatch import receiver

def validacion_identificacion(value):

    if len(str(value)) < 7 or len(str(value)) > 13:

        raise ValidationError("debes ingresar como minimo 7 digitos y maximo 13")
    
def validacion_telefono(value):

    if len(str(value)) != 10:

        raise ValidationError('debes ingresar 10 digitos')
    
def validacion_numeros_negativos(value):

    if value <= 0:

        raise ValidationError("no se puede ingresar solo 0 ni numeros negativos")
    

class ActivoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(estado='activo')

class Tipo_identificador(models.Model):

    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='activo',
        verbose_name="Estado"
    )
    
    # Managers
    objects = models.Manager()  # The default manager
    activos = ActivoManager()  # Our custom manager
    
    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = "Tipo Identificador"
        verbose_name_plural = "Tipos Identificadores"
        db_table = "Tipo_identificador"

class Tipo(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    nombre=models.CharField(max_length=150, verbose_name="Nombre", unique=True, null=True)
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='Activo',
        verbose_name="Estado"
    )
    
    # Managers
    objects = models.Manager()  # The default manager
    activos = ActivoManager()  # Our custom manager    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        db_table = "Tipo"


class Presentacion(models.Model):

    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    
    descripcion = models.CharField(max_length=150, verbose_name="Descripcion")
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='Activo',
        verbose_name="Estado"
    )
    
    # Managers
    objects = models.Manager()  # The default manager
    activos = ActivoManager()  # Our custom manager

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = "Presentación"
        verbose_name_plural = "Presentaciones"
        db_table = "Presentacion"


class Marcas(models.Model):

    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='activo',
        verbose_name="Estado"
    )
    
    # Managers
    objects = models.Manager()  # The default manager
    activos = ActivoManager()  # Our custom manager
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        db_table = "Marca"


class Unidad_Medida(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    descripcion = models.CharField(max_length=50, verbose_name="Descripcion")
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='activo',
        verbose_name="Estado"
    )
    
    # Managers
    objects = models.Manager()  # The default manager
    activos = ActivoManager()  # Our custom manager
    
    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medida"
        db_table = "Unidad_Medida"


class Proveedores(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    tipo_identicador = models.ForeignKey(Tipo_identificador, on_delete=models.PROTECT, null=True, verbose_name = "Tipo de Identificación")
    nit = models.CharField(max_length = 20, unique = True, verbose_name = "Numero de identificación", validators=[validacion_identificacion])
    ubicacion = models.CharField(max_length = 255, verbose_name = "Ubicacion")
    telefono = models.PositiveIntegerField( verbose_name = "Telefono", validators=[validacion_telefono])
    correo_electronico = models.EmailField(max_length=100, verbose_name = "Correo Electronico")
    
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        db_table = "Proveedores"

    



        
class Administradores(models.Model):

        

    # def validar_numero_documento(value):
    #     if value < 10000000 or value > 9999999999:
    #         raise ValidationError("El número de documento debe tener entre 8 y 10 dígitos")

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='administrador')
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo_documento = models.ForeignKey(Tipo_identificador,on_delete=models.PROTECT, verbose_name="Tipo de identificación")
    numero_documento = models.PositiveIntegerField(verbose_name="Número de documento", unique=True, validators=[validacion_identificacion])
    telefono = models.PositiveIntegerField(verbose_name="Teléfono", validators=[validacion_telefono])
    contrasena = models.CharField(max_length=128, validators=[MinLengthValidator(8)], verbose_name="Contraseña")
    conf_contrasena = models.CharField(max_length=128, verbose_name="Confirmación de contraseña", default="")

    def clean(self):
        super().clean()
        if self.contrasena != self.conf_contrasena:
            raise ValidationError({"conf_contrasena": "Las contraseñas no coinciden"})

    def __str__(self):

        return str(self.user)

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
    nit=models.PositiveBigIntegerField(verbose_name="Numero de Identificacion",unique=True, validators=[validacion_identificacion])
    correo_electronico=models.EmailField(max_length=150,verbose_name="Correo")
    telefono=models.PositiveIntegerField(verbose_name="Telefono", validators=[validacion_telefono])
    Tipo_identificador=models.ForeignKey(Tipo_identificador, on_delete=models.CASCADE,limit_choices_to={'estado': 'activo'})
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural ="Clientes"
        db_table ="Cliente"





# SE MODIFICO EL TIPO DE DATO DE PRECIO PARA QUE SE LE PUDIERA DAR FORMATO      
class Productos(models.Model):
    
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    precio = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Precio", validators=[validacion_numeros_negativos])
    marcas = models.ForeignKey(Marcas,on_delete=models.CASCADE,limit_choices_to={'estado': 'activo'})
    tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE,limit_choices_to={'estado': 'activo'})
    presentacion= models.ForeignKey(Presentacion,on_delete=models.CASCADE,limit_choices_to={'estado': 'activo'})
    unidad_medida=models.ForeignKey(Unidad_Medida,on_delete=models.CASCADE,limit_choices_to={'estado': 'activo'})
    
    def __str__(self):
        return f"id: {self.id} - {self.nombre} - {self.tipo} - {self.unidad_medida} - {self.marcas} "
    
    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
        db_table = "Producto"
        
class Metodo_Pago(models.Model):

    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    nombre = models.CharField(max_length=150, verbose_name="Nombre", unique=True)
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='activo',
        verbose_name="Estado"
    )

    # Managers
    objects = models.Manager()  # The default manager
    activos = ActivoManager()  # Our custom manager

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name ="Metodo de pago"
        verbose_name_plural ="Metodos de pagos"
        db_table ="Metodo de pago"




class Compras(models.Model):
    fecha_compra =models.DateField(verbose_name="Fecha De Compra",auto_now=True)
    metodo_pago =models.ForeignKey(Metodo_Pago,on_delete=models.PROTECT,limit_choices_to={'estado': 'activo'})
    proveedor = models.ForeignKey(Proveedores,on_delete=models.PROTECT)
    usuario = models.CharField(max_length=100, verbose_name='Usuario', null = True)
    finalizado = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name ="Compra"
        verbose_name_plural ="Compras"
        db_table ="Compra"

class DetalleCompra(models.Model):

    compra = models.ForeignKey(Compras, on_delete=models.PROTECT, default=1)
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad", validators=[validacion_numeros_negativos], null=True)
    precio_unitario = models.PositiveIntegerField(verbose_name='Precio unitario', null=True)
    producto = models.ForeignKey(Productos,on_delete=models.PROTECT)

    def __str__(self):

        return f"Detalle de Compra: #{self.id}"
    

    def Total(self):

        if str(Productos.objects.get(id = self.producto.id).tipo) == "Construcción":

            return (self.precio_unitario + Decimal((19 * int(self.precio_unitario)) / 100)) * self.cantidad
        
        return self.Subtotal()
    
    def Subtotal(self):

        return self.precio_unitario * self.cantidad
    
    def Iva(self):

        if str(Productos.objects.get(id = self.producto.id).tipo) == "Construcción":

            return Decimal((19 * self.Subtotal()) / 100)
        
        
        return 0

class Ventas(models.Model):
    fecha_venta=models.DateTimeField(verbose_name="Fecha De Venta",auto_now=True)
    usuario = models.CharField(max_length=100, verbose_name='Usuario', null=True)
    cliente = models.ForeignKey(Clientes,on_delete=models.PROTECT)
    metodo_pago = models.ForeignKey(Metodo_Pago, on_delete=models.PROTECT, null=True, verbose_name="Metodo de Pago",limit_choices_to={'estado': 'activo'})
    finalizado = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name ="Venta"
        verbose_name_plural ="Ventas"
        db_table ="Venta"

class DetalleVenta(models.Model):

    venta = models.ForeignKey(Ventas, on_delete=models.PROTECT)
    producto = models.ForeignKey(Productos, on_delete=models.PROTECT)
    precio_unitario = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Precio unitario', null=True)
    cantidad = models.PositiveIntegerField(validators=[validacion_numeros_negativos], verbose_name="Cantidad")

    def __str__(self):

        return f'Detalle de venta #{self.id}'
    

    def Total(self):

        if str(Productos.objects.get(id = self.producto.id).tipo) == "Construcción":

            return (self.precio_unitario + Decimal((19 * int(self.precio_unitario)) / 100)) * self.cantidad
        
        return self.Subtotal()
    
    def Subtotal(self):

        return self.precio_unitario * self.cantidad
    
    def Iva(self):

        if str(Productos.objects.get(id = self.producto.id).tipo) == "Construcción":

            return Decimal((19 * self.Subtotal()) / 100)
        
        
        return 0
