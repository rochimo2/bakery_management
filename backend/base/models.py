from django.db import models
import random
import os


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename)


class Feature(models.Model):
    """Esta clase representa el modelo de las características que puede tener cada producto."""
    nombre = models.CharField(max_length=70)
    tipo = models.CharField(max_length=70)
    precio = models.DecimalField('$', max_digits=10, decimal_places=2, default=0)
    imagen = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    
    def __str__(self):
        """Devuelve una representación legible de la instancia del modelo."""
        return "{}".format(self.nombre)
# Notas del modelo: no mostrar al cliente el precio mientras selecciona 
# (se le manda por mail). Mostrar al cliente
# las categorias, por ejemplo Molde y sus opciones,
# decoracion y opciones.No todas juntas.



class Supply(models.Model):
    """Clase que representa el control de stock"""
    KILO = 'KG'
    UNIDAD = 'UN'
    LITRO = 'LT'
    METRO = 'MT'
    TIPO_CHOICES = ((KILO, 'Kilo'), (UNIDAD, 'Unidad'), (LITRO, 'Litro'), (METRO, 'Metro'))
    nombre = models.CharField(max_length = 70)
    marca = models.CharField(max_length = 70)
    tipo = models.CharField(max_length = 70)
    unidad = models.CharField(max_length = 2, choices = TIPO_CHOICES, default = KILO)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, null= True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    saldo_minimo = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        """Devuelve una representación legible de la instancia del modelo."""
        return "{}".format(self.nombre)


class SystemParameters(models.Model):
    precio_hora_trabajada = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_pasteleria = models.CharField(max_length = 70)


class Product(models.Model):
    """Esta clase representa el modelo para los productos terminados seleccionados por el cliente para ser cotizado."""
    nombre = models.CharField(max_length = 70, blank = False)
    caracteristicas = models.ManyToManyField(Feature, related_name="caracteristicas",
                                            through_fields=('product', 'feature'),
                                            through='Features')
    ingredientes = models.ManyToManyField(Supply, related_name="ingredientes",
                                            through_fields=('product', 'supply'),
                                            through='Supplies')
    costo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    imagen = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    horas_trabajadas = models.DecimalField(max_digits=10, decimal_places=2, default=0)



    def __str__(self):
            """Devuelve una representación legible de la instancia del modelo."""
            return "{}".format(self.nombre)
# Mostrar al cliente para que confirme el producto a cotizar. Mostrar al pastelero toda la tabla con el costo
# mas el costo final para fijar el precio.

# Modelo para m2m Product
class Supplies(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    supply   = models.ForeignKey(Supply, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

# Modelo para m2m Product
class Features(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature  = models.ForeignKey(Feature, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)



class Supplier(models.Model):
    "Clase que representa los proveedores"
    nombre    = models.CharField(max_length = 70)
    direccion = models.CharField (max_length = 100)
    telefono  = models.CharField ( max_length = 20)
    contacto  = models.CharField(max_length = 70, blank = True)

    def __str__(self):
        """Devuelve una representación legible de la instancia del modelo."""
        return "{}".format(self.nombre)



class Client(models.Model):
    """Clase que registra a los clientes"""
    nombre = models.CharField(max_length = 70)
    direccion = models.CharField (max_length = 100)
    telefono = models.CharField ( max_length = 20)
    mail = models.EmailField(max_length= 50, blank=True)

    # ESTADO del pago, de la seña, deuda, fecha de pago, historial de pago
    def __str__(self):
        """Devuelve una representación legible de la instancia del modelo."""
        return "{}".format(self.nombre)



class Order(models.Model):
    """Clase que registra los pedidos de los clientes"""
    fecha = models.DateField('Fecha de pedido')
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    ocasion = models.CharField(max_length = 50)
    descripcion = models.TextField(max_length=140, null=True)
    producto = models.ManyToManyField(Product, related_name="productos",
                                            through_fields=('order', 'product'),
                                            through='Products')
    precio_sugerido = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        """Devuelve una representación legible de la instancia del modelo."""
        return "{}".format(self.ocasion)
# Ocasion: tipo de fieste (cumpleaños, bautismo, etc)
# Modelo parecido a Product. Con mas detalle, link a cliente que hace el pedido.
#  Pr es para comunicacion con cliente

# Modelo m2m para Order
class Products(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits= 10, decimal_places=1, default =0)



class Purchase(models.Model):
    """Clase que registra los movimientos de compra"""
    fecha = models.DateField('Fecha de la operación', auto_now=False, null=True)
    supply = models.ManyToManyField(Supply, related_name='suplies',
                                        through_fields=('purchase', 'supply'),
                                        through='SuppliesPurchase')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)

    def __str__(self):
        """Devuelve una representación legible de la instancia del modelo."""
        return "{}".format(self.fecha)

# Modelo para m2m Purchase
class SuppliesPurchase(models.Model):
    purchase  = models.ForeignKey(Purchase, on_delete=models.CASCADE, null=True)
    supply   = models.ForeignKey(Supply, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits= 10, decimal_places=2, default=0)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, null= True)



class Sale(models.Model):
    fecha = models.DateField('Fecha de venta')
    orden = models.ForeignKey(Order, on_delete=models.CASCADE, blank = True)
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE, blank = True)
    precio_final = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        """Devuelve una representación legible de la instancia del modelo."""
        return "{}".format(self.orden)


# Modelo para "contabilidad": las ventas$ menos las compras!

