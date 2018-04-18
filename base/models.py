from django.db import models


class Feature(models.Model):
    """Esta clase representa el modelo de las características que puede tener cada producto."""
    nombre   = models.CharField(max_length=70)
    tipo     = models.CharField(max_length=70)
    precio   = models.DecimalField('$', max_digits= 7, decimal_places=2, null= True)
    cantidad = models.IntegerField

    def __str__(self):
            """Devuelve una representación legible de la instancia del modelo."""
            return "{}".format(self.nombre)
# Notas del modelo: no mostrar al cliente el precio mientras selecciona (se le manda por mail). Mostrar al cliente
# las categorias, por ejemplo Molde y sus opciones, decoracion y opciones.No todas juntas.



class Supply(models.Model):
    """Clase que representa el control de stock"""
    KILO = 'KG'
    UNIDAD = 'UN'
    LITRO = 'LT'
    TIPO_CHOICES = ((KILO, 'Kilo'), (UNIDAD, 'Unidad'), (LITRO, 'Litro'))
    nombre = models.CharField(max_length = 70)
    marca = models.CharField(max_length = 70)
    tipo = models.CharField(max_length = 70)
    precio_unitario = models.DecimalField(max_digits=5, decimal_places=2, null= True)
    saldo = models.DecimalField(max_digits=5, decimal_places=2)
    unidad = models.CharField(max_length = 2, choices = TIPO_CHOICES, default = KILO)

    def __str__(self):
        """Devuelve una representación legible de la instancia del modelo."""
        return "{}".format(self.nombre)





class Product(models.Model):
    """Esta clase representa el modelo para los productos terminados seleccionados por el cliente para ser cotizado."""
    nombre = models.CharField(max_length = 70, blank = False)
    features = models.ManyToManyField(Feature, through='ProductFeature')
    supplies = models.ManyToManyField(Supply, through='ProductSupply')

    def __str__(self):
            """Devuelve una representación legible de la instancia del modelo."""
            return "{}".format(self.nombre)
# Mostrar al cliente para que confirme el producto a cotizar. Mostrar al pastelero toda la tabla con el costo
# mas el costo final para fijar el precio.


class ProductSupply(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    supply   = models.ForeignKey(Supply, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=5, decimal_places=2)

class ProductFeature(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature  = models.ForeignKey(Feature, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=5, decimal_places=2)


class Supplier(models.Model):
    "Clase que representa los proveedores"
    nombre    = models.CharField(max_length = 70)
    dirección = models.CharField (max_length = 100)
    telefono  = models.CharField ( max_length = 20)
    contacto  = models.CharField(max_length = 70, blank = True)

    def __str__(self):
        """Devuelve una representación legible de la instancia del modelo."""
        return "{}".format(self.nombre)





class Order(models.Model):
    """Clase que registra los pedidos de los clientes"""
    fecha = models.DateField('Fecha de pedido')
    descripcion = models.TextField
    ocasion = models.CharField(max_length = 50)
    ingredientes_utilizados = models.ForeignKey(Supply, on_delete=models.CASCADE, blank = True)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE, blank = True, null= True)

    def __str__(self):
        """Devuelve una representación legible de la instancia del modelo."""
        return "{}".format(self.ocasion)
# Ocasion: tipo de fieste (cumpleaños, bautismo, etc)
# Modelo parecido a Product. Con mas detalle, link a cliente que hace el pedido.
#  Pr es para comunicacion con cliente



class Client(models.Model):
    """Clase que registra a los clientes"""
    nombre = models.CharField(max_length = 70)
    dirección = models.CharField (max_length = 100)
    telefono = models.CharField ( max_length = 20)
    mail = models.EmailField
    pedido = models.ForeignKey(Order, on_delete=models.CASCADE, blank = True)


    def __str__(self):
        """Devuelve una representación legible de la instancia del modelo."""
        return "{}".format(self.nombre)


# class Purchase(models.Model):
#     supply = models.ForeignKey(Supply, on_delete=models.CASCADE, blank = True, null = True)
#     cantidad = models.DecimalField(max_digits= 7, decimal_places=2)
#     supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank = True, null = True)
#     fecha = models.DateField('fecha de compra', null =True)
#     precio_unitario = models.DecimalField(max_digits=5, decimal_places=2, null= True)

#     def __str__(self):
#         """Devuelve una representación legible de la instancia del modelo."""
#         return "{}".format(self.cantidad)



# class Sale(models.Model):
#     orden = models.ForeignKey(Order, on_delete=models.CASCADE, blank = True)
#     fecha = models.DateField('Fecha de venta')
#     cliente = models.ForeignKey(Client, on_delete=models.CASCADE, blank = True)
#     precio = models.DecimalField(max_digits=5, decimal_places=2)



class Movement(models.Model):
    """Clase que registra los movimientos de compra y venta"""
    VENTA = 'VT'
    COMPRA = 'CP'
    TIPO_CHOICES = ((VENTA, 'Venta'), (COMPRA, 'Compra'),)
    fecha = models.DateField('Fecha de la operación', auto_now=False)
    tipo = models.CharField(max_length = 2, choices = TIPO_CHOICES, default = VENTA)
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE, blank = True,null = True)
    cantidad = models.DecimalField(max_digits= 7, decimal_places=2, default=0)
    precio_unitario = models.DecimalField(max_digits=5, decimal_places=2, null= True)
    suplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank = True,null = True)
    client =  models.ForeignKey(Client, on_delete=models.CASCADE, blank = True,null = True)
    orden = models.ForeignKey(Order, on_delete=models.CASCADE, blank = True, null=True)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE, blank = True, null=True)


    def __str__(self):
        """Devuelve una representación legible de la instancia del modelo."""
        return "{}".format(self.tipo)






