from django.contrib import admin
from .models import *

class Client_admin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "phone",
    )

admin.site.register(Client, Client_admin)
