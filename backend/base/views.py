from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from decimal import Decimal

from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status

import json

from modules.calculus_helper import *

from .serializers import (ProductSerializer, FeatureSerializer, SupplierSerializer,
SupplySerializer, ClientSerializer, OrderSerializer, PurchaseSerializer, SaleSerializer)

from .models import (Product, Feature, Supplier, Supply, Purchase, Sale,
Client, Order, Features, Supplies, SuppliesPurchase, Products, SystemParameters)



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
        """Guarda la info al crear un nuevo producto. Calcula el COSTO del producto. Crea FEATURES y SUPPLIES y la relación m2m"""
        serializer.save()
        id_producto= serializer.instance.id
        # Para obtener el id del producto recien guardado. Fui a consola de depuraciony puse serializer, enter
        post = self.request.POST
        # json.loads transforma la lista en formato string a formato lista de python
        lista_caracteristicas = json.loads(post.get('caracteristicas'))
        lista_ingredientes = json.loads(post.get('ingredientes'))

        for caract in lista_caracteristicas:
            if caract.get('id') == None:
                nueva_feature= Feature.objects.create(nombre=caract['nombre'], tipo=caract['tipo'],
                precio=caract['precio'], imagen=caract['imagen'])

                Features.objects.create(product=serializer.instance,
                feature= nueva_feature, cantidad =caract['cantidad'])

            else:
                Features.objects.create(product=serializer.instance,
                feature=Feature.objects.get(pk=caract['id']), cantidad =caract['cantidad'])

# TODO: agregar saldo_minimo, horas trabajadas donde vaya!
        for ingr in lista_ingredientes:
            if ingr.get('id') == None:
                nuevo_supply = Supply.objects.create(nombre=ingr['nombre'], marca=ingr['marca'],
                tipo=ingr['tipo'], precio_unitario=ingr['precio_unitario'], saldo=ingr['saldo'],
                unidad=ingr['unidad'], saldo_minimo=ingr['saldo_minimo'])

                Supplies.objects.create(product=serializer.instance,
                supply= nuevo_supply, cantidad = ingr['cantidad'])

            else:
                Supplies.objects.create(product=serializer.instance,
                supply=Supply.objects.get(pk=ingr['id']), cantidad = ingr['cantidad'])

        prod = Product.objects.get(id=id_producto)
        prod.costo = costo_producto(id_producto)
        prod.save()



# url(r'^producto/detalle/(?P<pk>[0-9]+)/$'
class DetailsProductView(generics.RetrieveUpdateDestroyAPIView):
    """Esta clase maneja los requests GET, PUT, PATCH y DELETE ."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        serializer.save()
        post = self.request.POST
        lista_caracteristicas = json.loads(post.get('caracteristicas'))
        lista_ingredientes = json.loads(post.get('ingredientes'))

        id_post = serializer.data['id']

        Product(id_post).caracteristicas.clear()
        for caract in lista_caracteristicas:
            if caract.get('id') == None:
                nueva_feature= Feature.objects.create(nombre=caract['nombre'], tipo=caract['tipo'],
                precio=caract['precio'], imagen=caract['imagen'])

                Features.objects.create(product=serializer.instance,
                feature= nueva_feature, cantidad =caract['cantidad'])

            else:
                Features.objects.create(product=serializer.instance,
                feature=Feature.objects.get(pk=caract['id']), cantidad =caract['cantidad'])

        Product(id_post).ingredientes.clear()
        for ingr in lista_ingredientes:
            if ingr.get('id') == None:
                nuevo_supply = Supply.objects.create(nombre=ingr['nombre'], marca=ingr['marca'],
                tipo=ingr['tipo'], precio_unitario=ingr['precio_unitario'], saldo=ingr['saldo'],
                 unidad=ingr['unidad'], saldo_minimo=ingr['saldo_minimo'])

                Supplies.objects.create(product=serializer.instance,
                supply= nuevo_supply, cantidad = ingr['cantidad'])

            else:
                Supplies.objects.create(product=serializer.instance,
                supply=Supply.objects.get(pk=ingr['id']), cantidad = ingr['cantidad'])

        prod = Product.objects.get(id=id_post)
        prod.costo = costo_producto(id_post)
        prod.save()



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

    def perform_update(self, serializer):
        serializer.save()

        feature = Features.objects.get(feature=serializer.data['id'])
        producto = feature.product
        producto.costo = costo_producto(id_producto=feature.product.id)
        producto.save()


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



# PURCHASE
# url(r'^compra/$'
class PurchaseView(generics.ListAPIView):
    """Vista que muestra el queryset de los movimientos de compra."""
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

# url(r'^compra/nuevo/$'
class CreatePurchaseView(generics.ListCreateAPIView):
    """Esta clase maneja los requests GET y POST."""
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def perform_create(self, serializer):
        """Guarda la info al crear una nueva COMPRA. Suma al stock de SUPPLY. Crea nuevo SUPPLY si no existe.
        Crea relación m2m """
        serializer.save()
        post = self.request.POST
        lista_supplies = json.loads(post.get('supply'))
#TODO: hacer tambien la lista de caracteristicas, secompran tambien

        for sup in lista_supplies:
            if sup.get('id') == None:
                nuevo_supply = Supply.objects.create(nombre=sup['nombre'], marca=sup['marca'],
                tipo=sup['tipo'], precio_unitario=sup['precio_unitario'], saldo=sup['saldo'],
                unidad=sup['unidad'], saldo_minimo=ingr['saldo_minimo'])

                SuppliesPurchase.objects.create(purchase=serializer.instance,
                supply= nuevo_supply, cantidad=sup['cantidad'], precio_unitario=sup['precio_unitario'])

                lista_supply = json.loads(post.get('supply'))
                item= get_object_or_404(Supply, pk=nuevo_supply['id'])
                for supl in lista_supply:
                    cant = supl['cantidad']
                    precio = supl['precio_unitario']

                    item.saldo += Decimal(cant)
                    item.precio_unitario = Decimal(precio)
                    item.save()

            else:
                SuppliesPurchase.objects.create(purchase=serializer.instance,
                supply=Supply.objects.get(pk=sup['id']), cantidad=sup['cantidad'],
                precio_unitario=sup['precio_unitario'])

                lista_supply = json.loads(post.get('supply'))
                supply_item= get_object_or_404(Supply, pk=sup['id'])
                for supl in lista_supply:
                    cant = supl['cantidad']
                    precio = supl['precio_unitario']
                    supply_item.saldo += Decimal(cant)
                    supply_item.precio_unitario = Decimal(precio)
                    supply_item.save()

            supply = Supplies.objects.get(supply=sup['id'])
            producto = supply.product
            producto.costo = costo_producto(id_producto=supply.product.id)
            producto.save()



# url(r'^compra/detalle/(?P<pk>[0-9]+)/$'
class DetailsPurchaseView(generics.RetrieveUpdateDestroyAPIView):
    """Esta clase maneja los requests GET, PUT, PATCH y DELETE ."""
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def perform_update(self, serializer):
        """Guarda la info al crear una nueva COMPRA. Suma al stock de SUPPLY. Crea nuevo SUPPLY si no existe.
        Crea relación m2m """
        serializer.save()
        post = self.request.POST
        lista_supplies = json.loads(post.get('supply'))

        id_post = serializer.data['id']

        Purchase(id_post).supply.clear()
        for sup in lista_supplies:
            if sup.get('id') == None:
                nuevo_supply = Supply.objects.create(nombre=sup['nombre'], marca=sup['marca'],
                tipo=sup['tipo'], precio_unitario=sup['precio_unitario'], saldo=sup['saldo'],
                unidad=sup['unidad'], saldo_minimo=ingr['saldo_minimo'])

                SuppliesPurchase.objects.create(purchase=serializer.instance,
                supply= nuevo_supply, cantidad=sup['cantidad'], precio_unitario=sup['precio_unitario'])

                lista_supply = json.loads(post.get('supply'))
                item= get_object_or_404(Supply, pk=nuevo_supply['id'])
                for supl in lista_supply:
                    cant = supl['cantidad']
                    precio = supl['precio_unitario']

                    item.saldo += Decimal(cant)
                    item.precio_unitario = Decimal(precio)
                    item.save()

            else:
                SuppliesPurchase.objects.create(purchase=serializer.instance,
                supply=Supply.objects.get(pk=sup['id']), cantidad=sup['cantidad'],
                precio_unitario=sup['precio_unitario'])

                lista_supply = json.loads(post.get('supply'))
                supply_item= get_object_or_404(Supply, pk=sup['id'])
                for supl in lista_supply:
                    cant = supl['cantidad']
                    precio = supl['precio_unitario']
                    supply_item.saldo += Decimal(cant)
                    supply_item.precio_unitario = Decimal(precio)
                    supply_item.save()

            supply = Supplies.objects.get(supply=sup['id'])
            producto = supply.product
            producto.costo = costo_producto(id_producto=supply.product.id)
            producto.save()



# VENTAS (SALE)
# url(r'^venta/$'
class SaleView(generics.ListAPIView):
    """Vista que muestra el queryset de los movimientos de Venta."""
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class CreateSaleView(generics.ListCreateAPIView):
    """Esta clase maneja los requests GET y POST."""
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    # Hacer un FOR para cada cantidad de cada ingrediente de la lista.
#     momo=Product.objects.get(nombre='Momo Keeki')
# >>> momo
# <Product: Momo Keeki>
# >>> momo.ingredientes
# <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x0000027222119C88>
# >>> momo.ingredientes.all()
# <QuerySet [<Supply: Harina>, <Supply: durazno>]>
# >>> momo.supplies_set
# <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x0000027222138470>
# >>> momo.supplies_set.get(supply=momo.ingredientes.first())
# <Supplies: Supplies object (11)>
# >>> momo.supplies_set.get(supply=momo.ingredientes.first()).cantidad
# Decimal('3.00')

    def perform_create(self, serializer):
        """Guarda la info al crear una nueva feature."""
        serializer.save()

class DetailsSaleView(generics.RetrieveUpdateDestroyAPIView):
    """Esta clase maneja los requests GET, PUT, PATCH y DELETE ."""
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    def perform_update(self, serializer):
        """Actualiza una venta"""
        serializer.save()



# CLIENTES(CLIENT)
# url(r'^cliente/$
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
# url(r'^pedido/$' 
class OrderView(generics.ListAPIView):
    """Vista que muestra el queryset de los pedidos."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderHelper():

    def save_order(self, lista_productos, serializer, precio_hora_trabajada, alerta):

        horas_trabajadas_total = 0
        for prod in lista_productos:
            producto = Product.objects.get(pk=prod['id'])
            Products.objects.create(order=serializer.instance,
                                    product=producto, cantidad=prod['cantidad'])
            for ingred in producto.supplies_set.all():
                cantidad_por_ingrediente = producto.supplies_set.get(supply=ingred.supply_id).cantidad
                ingrediente = ingred.supply
                ingrediente.saldo -= cantidad_por_ingrediente*Decimal(prod['cantidad'])
                ingrediente.save()
                if ingrediente.saldo <= ingrediente.saldo_minimo:
                    alerta['Titulo']='Alerta de Stock'
                    alerta['Mensaje'] = 'El stock del ingrediente {} llegó a su mínimo: {}. '.format(ingrediente.nombre, ingrediente.saldo_minimo)
                    # alerta = {'Alerta' : {'Titulo' : 'Alerta de Stock', 'Mensaje': 'El stock del ingrediente {} llegó a su mínimo: {}. '.format(ingrediente.nombre, ingrediente.saldo_minimo)}}
            horas_trabajadas_total += producto.horas_trabajadas

        serializer.instance.precio_sugerido = (serializer.instance.costo_total*3)+(precio_hora_trabajada*horas_trabajadas_total)
        serializer.instance.save()


# url(r'^pedido/nuevo/$'
class CreateOrderView(generics.ListCreateAPIView, OrderHelper):
    """Esta clase maneja los requests GET y POST."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


    def create(self, request, *args, **kwargs):
        """
        Guarda la info al crear una nueva ORDEN. RESTA del stock.
        Controla el saldo mínimo.Devuelve el precio sugerido.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        alerta = {}
        post = self.request.POST
        lista_productos = json.loads(post.get('productos'))
        precio_hora_trabajada = SystemParameters.objects.get(id=1).precio_hora_trabajada

        serializer.instance.costo_total = costo_total_orden(post)

        self.save_order(lista_productos, serializer, precio_hora_trabajada, alerta)

        headers = self.get_success_headers(serializer.data)
        return Response({'orden': serializer.data, 'alerta': alerta}, status=status.HTTP_201_CREATED, headers=headers)


# url(r'^pedido/detalle/(?P<pk>[0-9]+)/$'
class DetailsOrderView(generics.RetrieveUpdateDestroyAPIView, OrderHelper):
    """Esta clase maneja los requests GET, PUT, PATCH y DELETE ."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        
        post = self.request.POST
        lista_productos = json.loads(post.get('productos'))
        precio_hora_trabajada = SystemParameters.objects.get(id=1).precio_hora_trabajada
        id_post = serializer.data['id']
        alerta = {}

        serializer.instance.costo_total = costo_total_orden(post)

        Order(id_post).producto.clear()
        self.save_order(lista_productos, serializer, precio_hora_trabajada, alerta)

        return Response({'orden': serializer.data, 'alerta': alerta})
