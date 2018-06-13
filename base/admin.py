from django.contrib import admin
from .models import (Product, Feature, Purchase, Supplier, 
Supply, Order, Client, Supplies, Features, SuppliesPurchase, Sale, SystemParameters)


class FeatureAdmin(admin.ModelAdmin):
    model = Feature
admin.site.register(Feature, FeatureAdmin)

class SupplyInline(admin.TabularInline):
    model= Supplies
    extra = 1

class FeatureInline(admin.TabularInline):
    model = Features
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = (SupplyInline, FeatureInline,)
admin.site.register(Product, ProductAdmin)

class SupplyAdmin(admin.ModelAdmin):
    model = Supply
admin.site.register(Supply,SupplyAdmin)

class SupplierAdmin(admin.ModelAdmin):
    model = Supplier
admin.site.register(Supplier,SupplierAdmin)

class SupplyPurchaseInline(admin.TabularInline):
    model = SuppliesPurchase
    extra = 1

class PurchaseAdmin(admin.ModelAdmin):
    model = Purchase
    inlines = (SupplyPurchaseInline,)
admin.site.register(Purchase, PurchaseAdmin)

class OrderAdmin(admin.ModelAdmin):
    model = Order
admin.site.register(Order, OrderAdmin)

class ClientAdmin(admin.ModelAdmin):
    model = Client
admin.site.register(Client, ClientAdmin)


class SaleAdmin(admin.ModelAdmin):
    model = Sale
admin.site.register(Sale, SaleAdmin)

class SystemParametersAdmin(admin.ModelAdmin):
    model = SystemParameters
admin.site.register(SystemParameters, SystemParametersAdmin)
