from django.contrib import admin
from .models import Product, Feature, Movement, Supplier, Supply, Order, Client


class FeatureAdmin(admin.ModelAdmin):
    model = Feature
admin.site.register(Feature, FeatureAdmin)

class ProductAdmin(admin.ModelAdmin):
    model = Product
admin.site.register(Product, ProductAdmin)

class SupplierAdmin(admin.ModelAdmin):
    model = Supplier
admin.site.register(Supplier,SupplierAdmin)

class SupplyAdmin(admin.ModelAdmin):
    model = Supply
admin.site.register(Supply, SupplyAdmin)

# Error = supply no tiene FK a movement.
# class SupplyInline(admin.TabularInline):
#     model= Supply
#     extra= 10
#     fk_name= 'supply'
# quiero que movement en el administrador me de varios lugares para poner los productos de una sola vez.
class MovementAdmin(admin.ModelAdmin):
    model = Movement
    # inlines = [SupplyInline]
admin.site.register(Movement, MovementAdmin)

class OrderAdmin(admin.ModelAdmin):
    model = Order
admin.site.register(Order, OrderAdmin)

class ClientAdmin(admin.ModelAdmin):
    model = Client
admin.site.register(Client, ClientAdmin)

# class SaleAdmin(admin.ModelAdmin):
#     model = Sale
# admin.site.register(Sale, SaleAdmin)

# class PurchaseAdmin(admin.ModelAdmin):
#     model = Purchase
# admin.site.register(Purchase, PurchaseAdmin)