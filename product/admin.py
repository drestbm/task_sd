from django.contrib import admin
from .models import *

class Product_admin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "price",
    )

admin.site.register(Product, Product_admin)
