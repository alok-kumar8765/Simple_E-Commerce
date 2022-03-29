from django.conf.urls import url
from . import views

app_name = "shop"

urlpatterns = [
    url(r"^$", views.product_list, name="product_list"),
    url(
        r"^(?P<category_slug>[-\w]+)/$",
        views.product_list,
        name="product_list_by_category",
    ),
    url(
        r"^(?P<id>\d+)/(?P<slug>[-\w]+)/$", views.product_detail, name="product_detail"
    ),
    url(
        r"^create_category",views.create_category, name="create_category"
    ),
    url(
        r"^create_product",views.create_product, name="create_product"
    ),
]
