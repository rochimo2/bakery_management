from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = {

    url(r'^producto/$', views.ProductView.as_view(), name="productos"),

    url(r'^producto/nuevo/$', views.CreateProductView.as_view(), name="crear_nuevo_producto"),

    url(r'^producto/detalle/(?P<pk>[0-9]+)/$', views.DetailsProductView.as_view(), name="modificar_producto"),

    url(r'^feature/$', views.FeatureView.as_view(), name="feature"),

    url(r'^feature/nuevo/$', views.CreateFeatureView.as_view(), name="crear_nuevo_feature"),

    url(r'^feature/detalle/(?P<pk>[0-9]+)/$', views.DetailsFeatureView.as_view(), name="modificar_feature"),

    url(r'^proveedor/$', views.SupplierView.as_view(), name="proveedor"),

    url(r'^proveedor/nuevo/$', views.CreateSupplierView.as_view(), name="crear_nuevo_proveedor"),

    url(r'^proveedor/detalle/(?P<pk>[0-9]+)/$', views.DetailsSupplierView.as_view(), name="modificar_proveedor"),

    url(r'^material/$', views.SupplyView.as_view(), name="material"),

    url(r'^material/nuevo/$', views.CreateSupplyView.as_view(), name="crear_nuevo_material"),

    url(r'^material/detalle/(?P<pk>[0-9]+)/$', views.DetailsSupplyView.as_view(), name="modificar_material"),

    url(r'^movimiento/$', views.MovementView.as_view(), name="movimiento"),

    url(r'^movimiento/nuevo/$', views.CreateMovementView.as_view(), name="crear_nuevo_movimiento"),

    url(r'^movimiento/detalle/(?P<pk>[0-9]+)/$', views.DetailsMovementView.as_view(), name="modificar_movimiento"),

    url(r'^cliente/$', views.ProductView.as_view(), name="cliente"),

    url(r'^cliente/nuevo/$', views.CreateProductView.as_view(), name="crear_nuevo_cliente"),

    url(r'^cliente/detalle/(?P<pk>[0-9]+)/$', views.DetailsProductView.as_view(), name="modificar_cliente"),

    url(r'^pedido/$', views.OrderView.as_view(), name="pedido"),

    url(r'^pedido/nuevo/$', views.CreateOrderView.as_view(), name="crear_nuevo_pedido"),

    url(r'^pedido/detalle/(?P<pk>[0-9]+)/$', views.DetailsOrderView.as_view(), name="modificar_pedido"),

#     url(r'^compra/$', views.PurchaseView.as_view(), name="compra"),

#     url(r'^compra/nuevo/$', views.CreatePurchaseView.as_view(), name="crear_nuevo_compra"),

#     url(r'^compra/detalle/(?P<pk>[0-9]+)/$', views.DetailsPurchaseView.as_view(), name="modificar_compra"),
}

urlpatterns = format_suffix_patterns(urlpatterns)