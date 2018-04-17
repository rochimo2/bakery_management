from django.shortcuts import render
from django.shortcuts import get_object_or_404

from decimal import Decimal

from rest_framework import generics

from .serializers import (
ProductSerializer,
FeatureSerializer,
SupplierSerializer,
SupplySerializer,
MovementSerializer,
ClientSerializer,
OrderSerializer)

from .models import Product, Feature, Supplier, Supply, Movement, Client, Order

# PRODUCTOS
class ProductView(generics.ListAPIView):
    """Vista que muestra el queryset de los productos."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CreateProductView(generics.ListCreateAPIView):
    """Esta clase maneja los requests GET y POST."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """Guarda la info al crear un nuevo producto."""
        serializer.save()

class DetailsProductView(generics.RetrieveUpdateDestroyAPIView):
    """Esta clase maneja los requests GET, PUT, PATCH y DELETE ."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



# FEATURES
class FeatureView(generics.ListAPIView):
    """Vista que muestra el queryset de las features."""
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class CreateFeatureView(generics.ListCreateAPIView):
    """Esta clase maneja los requests GET y POST."""
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

    def perform_create(self, serializer):
        """Guarda la info al crear una nueva feature."""
        serializer.save()

class DetailsFeatureView(generics.RetrieveUpdateDestroyAPIView):
    """Esta clase maneja los requests GET, PUT, PATCH y DELETE ."""
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer



# PROVEEDORES (SUPPLIER)
class SupplierView(generics.ListAPIView):
    """Vista que muestra el queryset de los proveedores."""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class CreateSupplierView(generics.ListCreateAPIView):
    """Esta clase maneja los requests GET y POST."""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def perform_create(self, serializer):
        """Guarda la info al crear una nueva."""
        serializer.save()

class DetailsSupplierView(generics.RetrieveUpdateDestroyAPIView):
    """Esta clase maneja los requests GET, PUT, PATCH y DELETE ."""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer



# INGREDIENTES MATERIALES (SUPPLY)
class SupplyView(generics.ListAPIView):
    """Vista que muestra el queryset de los materiales."""
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer

class CreateSupplyView(generics.ListCreateAPIView):
    """Esta clase maneja los requests GET y POST."""
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer

    def perform_create(self, serializer):
        """Guarda la info al crear una nueva."""
        serializer.save()

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
class ClientView(generics.ListAPIView):
    """Vista que muestra el querysetde los clientes."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CreateClientView(generics.ListCreateAPIView):
    """Esta clase maneja los requests GET y POST."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        """Guarda la info al crear una nueva."""
        serializer.save()

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