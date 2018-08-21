import json
from decimal import Decimal
from base.models import Product

# def precio_total_sugerido(precio_hora_trabajada, horas_trabajadas):
#     """bla"""
#     lista_producto = json.loads(post.get('productos'))
    
#     serializer.instance.precio_sugerido = (costo_total_orden(post)*3)+(precio_hora_trabajada*horas_trabajadas)

def costo_total_orden(post):
    """Calcula el costo total de los productos de la orden"""
    lista_producto = json.loads(post.get('productos'))

    costo_total = 0
    for prod in lista_producto:
        producto = Product.objects.get(pk=prod['id'])
        costo_total += producto.costo*Decimal(prod['cantidad'])

    return costo_total

def costo_producto(id_producto):
    """Calcula el costo total del producto"""
    prod = Product.objects.get(id=id_producto)

    costo_ingredientes = 0
    for ingr in prod.ingredientes.all():
        prec = Decimal(ingr.precio_unitario)
        cantidad = Decimal(prod.supplies_set.get(supply=ingr).cantidad)
        costo_ingredientes += prec*cantidad

    costo_features = 0
    for feature in prod.caracteristicas.all():
        prec = Decimal(feature.precio)
        cantidad = Decimal(prod.features_set.get(feature=feature).cantidad)
        costo_features += prec*cantidad

    return costo_ingredientes + costo_features
