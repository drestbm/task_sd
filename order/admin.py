from django.contrib import admin
from .models import *

class Order_admin(admin.ModelAdmin):
    list_display = (
        "id",
        "date_create",
        "date_update",
        "client",
        "total_price"
    )

admin.site.register(Order, Order_admin)

class Ordered_product_admin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "product",
        "price",
        "quantity"
    )

admin.site.register(Ordered_product, Ordered_product_admin)