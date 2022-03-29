from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ["product"]


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "email",
        "city",
        "street",
        "house_number",
        "apartment_number",
        "paid",
        Order.get_total_cost,
        "created",
    ]
    list_filter = ["paid", "created", "updated", "city"]
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
