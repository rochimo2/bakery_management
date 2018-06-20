from rest_framework import serializers
from .models import Feature, Product, Client, Order, Purchase, Supply, Supplier, Sale

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('id', 'nombre', 'tipo', 'precio', 'cantidad', 'imagen')

class SupplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Supply
        fields = ('id', 'nombre', 'marca', 'tipo', 'precio_unitario', 'saldo', 'unidad')

class ProductSerializer(serializers.ModelSerializer):
    feat = FeatureSerializer(many=True, read_only=True)
    sup = SupplySerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'nombre', 'caracteristicas', 'ingredientes', 'imagen', 'feat', 'sup')

class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = ('id', 'nombre', 'direccion', 'telefono', 'mail', 'ordenes')

class OrderSerializer(serializers.ModelSerializer):
    prod = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'fecha', 'descripcion', 'ocasion', 'producto', 'cliente', 'costo_total', 'precio_sugerido', 'prod')


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ('id', 'nombre', 'direccion', 'telefono', 'contacto')

class PurchaseSerializer(serializers.ModelSerializer):
    sply = SupplySerializer(many=True, read_only=True)
    class Meta:
        model = Purchase
        fields = ('id', 'fecha', 'supply', 'supplier', 'sply')

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id', 'fecha', 'orden', 'cliente')


 
