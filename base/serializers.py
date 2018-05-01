from rest_framework import serializers
from .models import Feature, Product, Client, Order, Movement, Supply, Supplier, Repuesto, Auto

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('id', 'nombre', 'tipo', 'precio', 'cantidad')

class SupplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Supply
        fields = ('id', 'nombre', 'marca', 'tipo', 'precio_unitario', 'saldo', 'unidad')

class ProductSerializer(serializers.ModelSerializer):
    feat = FeatureSerializer(many=True, read_only=True)
    sup = SupplySerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'nombre', 'caracteristicas', 'ingredientes', 'feat', 'sup')

class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = ('id', 'nombre', 'direccion', 'telefono', 'mail', 'pedido')

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'fecha', 'descripcion', 'ocasion', 'ingredientes_utilizados', 'producto')

class MovementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movement
        fields = ('id', 'fecha', 'tipo', 'supply', 'cantidad', 'precio_unitario', 'suplier', 'client', 'orden', 'producto')

class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ('id', 'nombre', 'direccion', 'telefono', 'contacto')

# class PurchaseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Purchase
#         fields = ('id', 'cantidad', 'supplier', 'supply', 'precio_unitario', 'fecha')

class RepuestoSerializer(serializers.ModelSerializer):
    # autos = serializers.PrimaryKeyRelatedField(many=True, read_only=True, allow_empty=False)

    class Meta:
        model= Repuesto
        fields=('id', 'nombre', 'auto_nombre')

class AutoSerializer(serializers.ModelSerializer):
    repu = RepuestoSerializer(many=True, read_only=True)
    class Meta:
        model= Auto
        fields= ('id', 'nombre', 'repuestos', 'repu')
 
