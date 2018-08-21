from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework.authtoken.views import obtain_auth_token

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

    url(r'^compra/$', views.PurchaseView.as_view(), name="compra"),

    url(r'^compra/nuevo/$', views.CreatePurchaseView.as_view(), name="crear_nuevo_compra"),

    url(r'^compra/detalle/(?P<pk>[0-9]+)/$', views.DetailsPurchaseView.as_view(), name="modificar_compra"),

    url(r'^cliente/$', views.ClientView.as_view(), name="cliente"),

    url(r'^cliente/nuevo/$', views.CreateClientView.as_view(), name="crear_nuevo_cliente"),

    url(r'^cliente/detalle/(?P<pk>[0-9]+)/$', views.DetailsClientView.as_view(), name="modificar_cliente"),

    url(r'^pedido/$', views.OrderView.as_view(), name="pedido"),

    url(r'^pedido/nuevo/$', views.CreateOrderView.as_view(), name="crear_nuevo_pedido"),

    url(r'^pedido/detalle/(?P<pk>[0-9]+)/$', views.DetailsOrderView.as_view(), name="modificar_pedido"),

    url(r'^venta/$', views.SaleView.as_view(), name="venta"),

    url(r'^venta/nuevo/$', views.CreateSaleView.as_view(), name="crear_nuevo_venta"),

    url(r'^venta/detalle/(?P<pk>[0-9]+)/$', views.DetailsSaleView.as_view(), name="modificar_venta"),

    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)