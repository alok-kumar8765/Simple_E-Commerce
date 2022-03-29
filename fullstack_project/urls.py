from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    path("cart/", include("cart.urls")),
    path("orders/", include("orders.urls")),
    path("shop/", include("shop.urls")),
    # path("accounts/", include("django.contrib.auth.urls")),
    # path("accounts/", include("accounts.urls")),
    path("admin/", admin.site.urls),
    # path("", include("homepage.urls")),
    path("", RedirectView.as_view(url="/shop/", permanent=False), name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
