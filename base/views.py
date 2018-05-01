from django.shortcuts import render
from django.shortcuts import get_object_or_404

from decimal import Decimal

from rest_framework import generics

import json

from .serializers import (
ProductSerializer,
FeatureSerializer,
SupplierSerializer,
SupplySerializer,
MovementSerializer,
ClientSerializer,
OrderSerializer,
AutoSerializer,
RepuestoSerializer)

from .models import (Product, Feature, Supplier,
 Supply, Movement, Client, Order, Auto, 
 Repuesto, Features, Supplies)

# PRODUCTOS
# url(r'^producto/$'
class ProductView(generics.ListAPIView):
    """Vista que muestra el queryset de los productos."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# url(r'^producto/nuevo/$'
class CreateProductView(generics.ListCreateAPIView):
    """Esta clase maneja los requests GET y POST."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """Guarda la info al crear un nuevo producto."""
        serializer.save()
        # -para obtener el id del producto recien guardado. Fui a consola de depuraciony puse serializer, enter
        id_producto= serializer.instance.id
        post = self.request.POST
        # json.loads transforma la lista en formato string a formato lista de python
        lista_caracteristicas = json.loads(post.get('caracteristicas'))
        lista_ingredientes = json.loads(post.get('ingredientes'))
        
        for caract in lista_caracteristicas:
            Features.objects.create(product=serializer.instance,
            feature=Feature.objects.get(pk=caract['id']), cantidad =caract['cantidad'])

        for ingr in lista_ingredientes:
            Supplies.objects.create(product=serializer.instance,
            supply=Supply.objects.get(pk=ingr['id']), cantidad = ingr['cantidad'])
        # caracts= get_object_or_404(Feature, pk=self.request.data['caracteristicas'])

# url(r'^producto/detalle/(?P<pk>[0-9]+)/$'
class DetailsProductView(generics.RetrieveUpdateDestroyAPIView):
    """Esta clase maneja los requests GET, PUT, PATCH y DELETE ."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



# FEATURES
# url(r'^feature/$',
class FeatureView(generics.ListAPIView):
    """Vista que muestra el queryset de las features."""
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

# url(r'^feature/nuevo/$'
class CreateFeatureView(generics.ListCreateAPIView):
    """Esta clase maneja los requests GET y POST."""
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

    def perform_create(self, serializer):
        """Guarda la info al crear una nueva feature."""
        serializer.save()

# url(r'^feature/detalle/(?P<pk>[0-9]+)/$'
class DetailsFeatureView(generics.RetrieveUpdateDestroyAPIView):
    """Esta clase maneja los requests GET, PUT, PATCH y DELETE ."""
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer



# PROVEEDORES (SUPPLIER)
# url(r'^proveedor/$'
class SupplierView(generics.ListAPIView):
    """Vista que muestra el queryset de los proveedores."""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

# url(r'^proveedor/nuevo/$'
class CreateSupplierView(generics.ListCreateAPIView):
    """Esta clase maneja los requests GET y POST."""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def perform_create(self, serializer):
        """Guarda la info al crear una nueva."""
        serializer.save()

# url(r'^proveedor/detalle/(?P<pk>[0-9]+)/$'
class DetailsSupplierView(generics.RetrieveUpdateDestroyAPIView):
    """Esta clase maneja los requests GET, PUT, PATCH y DELETE ."""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
 


# INGREDIENTES MATERIALES (SUPPLY)
# url(r'^material/$'
class SupplyView(generics.ListAPIView):
    """Vista que muestra el queryset de los materiales."""
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer

# url(r'^material/nuevo/$'
class CreateSupplyView(generics.ListCreateAPIView):
    """Esta clase maneja los requests GET y POST."""
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer

    def perform_create(self, serializer):
        """Guarda la info al crear una nueva."""
        serializer.save()

# url(r'^material/detalle/(?P<pk>[0-9]+)/$'
class DetailsSupplyView(generics.RetrieveUpdateDestroyAPIView):
    """Esta clase maneja los requests GET, PUT, PATCH y DELETE ."""
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer



# MOVIMIENTOS 
class MovementView(generics.ListAPIView):
    """Vista que muestra el queryset de los movimientos de compra y venta."""
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer

class CreateMovementView(generics.ListCreateAPIView):
    """Esta clase maneja los requests GET y POST."""
    queryset = Movement.objects.all()

    serializer_class = MovementSerializer

    def perform_create(self, serializer):
        """Guarda la info al crear un nuevo movimiento."""
        item= get_object_or_404(Supply, pk=self.request.data['supply'])
        if self.request.data['tipo']=='CP':
            item.saldo += Decimal(self.request.data['cantidad'])
            item.precio_unitario = Decimal(self.request.data['precio_unitario'])
        else:
            item.saldo -= Decimal(self.request.data['cantidad'])
        item.save()
        serializer.save()

# item = Supply.objects.get(pk=2)
# item.saldo += 5
# item.save()
# serializer.save()

class DetailsMovementView(generics.RetrieveUpdateDestroyAPIView):
    """Esta clase maneja los requests GET, PUT, PATCH y DELETE ."""
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer




# CLIENTES (CLIENT)
# url(r'^cliente/$'
class ClientView(generics.ListAPIView):
    """Vista que muestra el querysetde los clientes."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# url(r'^cliente/nuevo/$'
class CreateClientView(generics.ListCreateAPIView):
    """Esta clase maneja los requests GET y POST."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        """Guarda la info al crear una nueva."""
        serializer.save()

# url(r'^cliente/detalle/(?P<pk>[0-9]+)/$'
class DetailsClientView(generics.RetrieveUpdateDestroyAPIView):
    """Esta clase maneja los requests GET, PUT, PATCH y DELETE ."""
    queryset = Client.objects.all()
    serializer_class =ClientSerializer



# PEDIDOS (ORDER)
class OrderView(generics.ListAPIView):
    """Vista que muestra el queryset de los pedidos."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CreateOrderView(generics.ListCreateAPIView):
    """Esta clase maneja los requests GET y POST."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        """Guarda la info al crear una nueva."""
        serializer.save()

class DetailsOrderView(generics.RetrieveUpdateDestroyAPIView):
    """Esta clase maneja los requests GET, PUT, PATCH y DELETE ."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer




# Compras (purchase)
# class PurchaseView(generics.ListAPIView):
#     """Vista que muestra el queryset de los pedidos."""
#     queryset = Purchase.objects.all()
#     serializer_class = PurchaseSerializer

# class CreatePurchaseView(generics.ListCreateAPIView):
#     """Esta clase maneja los requests GET y POST."""
#     queryset = Purchase.objects.all()
#     serializer_class = PurchaseSerializer

#     def perform_create(self, serializer):
#         """Guarda la info al crear una nueva."""
#         serializer.save()

# class DetailsPurchaseView(generics.RetrieveUpdateDestroyAPIView):
#     """Esta clase maneja los requests GET, PUT, PATCH y DELETE ."""
#     queryset = Purchase.objects.all()
#     serializer_class = PurchaseSerializer

class AutoView(generics.ListAPIView):
    """Vista que muestra el queryset de los pedidos."""
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

class CreateAutoView(generics.ListCreateAPIView):
    """Esta clase maneja los requests GET y POST."""
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

    def perform_create(self, serializer):
        """Guarda la info al crear un nuevo producto."""
        serializer.save()

class DetailsAutoView(generics.RetrieveUpdateDestroyAPIView):
    """Esta clase maneja los requests GET, PUT, PATCH y DELETE ."""
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer



class RepuestoView(generics.ListAPIView):
    """Vista que muestra el queryset de los pedidos."""
    queryset = Repuesto.objects.all()
    serializer_class = RepuestoSerializer

class CreateRepuestoView(generics.ListCreateAPIView):
    """Esta clase maneja los requests GET y POST."""
    queryset = Repuesto.objects.all()
    serializer_class = RepuestoSerializer

    def perform_create(self, serializer):
        """Guarda la info al crear un nuevo producto."""
        serializer.save()

class DetailsRepuestoView(generics.RetrieveUpdateDestroyAPIView):
    """Esta clase maneja los requests GET, PUT, PATCH y DELETE ."""
    queryset = Repuesto.objects.all()
    serializer_class = RepuestoSerializer