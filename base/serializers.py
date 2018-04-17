from rest_framework import serializers
from .models import Feature, Product, Client, Order, Movement, Supply, Supplier

class FeatureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Feature
        fields = ('id', 'nombre', 'cantidad')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'nombre', 'features', 'supply')

class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = ('id', 'nombre', 'direccion', 'telefono', 'mail', 'pedido')

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'fecha', 'descripcion', 'ocasion', 'ingredientes_utilizados')

class MovementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movement
        fields = ('id', 'fecha', 'tipo', 'supply', 'cantidad', 'precio_unitario', 'suplier', 'client', 'orden', 'producto')

class SupplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Supply
        fields = ('id', 'nombre', 'marca', 'tipo', 'precio_unitario', 'saldo', 'unidad')

class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ('id', 'nombre', 'direccion', 'telefono', 'contacto')

# class PurchaseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Purchase
#         fields = ('id', 'cantidad', 'supplier', 'supply', 'precio_unitario', 'fecha')