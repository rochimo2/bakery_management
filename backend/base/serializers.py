from rest_framework import serializers
from .models import Feature, Product, Client, Order, Purchase, Supply, Supplier, Sale, Products, Features, Supplies


class SupplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Supply
        fields = ('id', 'nombre', 'marca', 'tipo', 'precio_unitario', 'saldo', 'unidad')

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('id', 'nombre', 'tipo', 'precio', 'imagen')

class SuppliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplies
        fields = ('id', 'supply',  'cantidad')
        depth = 2

class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ('id', 'feature', 'cantidad')
        depth = 2


class ProductSerializer(serializers.ModelSerializer):
    feat = FeatureSerializer(many=True, read_only=True)
    sup = SupplySerializer(many=True, read_only=True)
    features = FeaturesSerializer(many=True, read_only=True, source='features_set')
    supplies = SuppliesSerializer(many=True, read_only=True, source='supplies_set')
    class Meta:
        model = Product
        fields = ('id', 'nombre', 'imagen', 'costo', 'horas_trabajadas', 'feat', 'sup', 'features', 'supplies')


class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = ('id', 'nombre', 'direccion', 'telefono', 'mail')

class ProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        fields = ('id', 'product', 'cantidad')
        depth = 2

class OrderSerializer(serializers.ModelSerializer):
    prod = ProductSerializer(many=True, read_only=True)
    productos = ProductsSerializer(many=True, read_only=True, source='products_set')
    class Meta:
        model = Order
        fields = ('id', 'fecha', 'descripcion', 'ocasion',  'cliente', 'costo_total', 'precio_sugerido', 'productos', 'prod')


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
        fields = ('id', 'fecha', 'orden', 'cliente', 'precio_final')


 
