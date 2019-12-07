from django.db import models
from client.models import Client
from product.models import Product

class Order(models.Model):
    id = models.PositiveIntegerField(verbose_name = "Идентификатор", primary_key = True)
    date_create = models.DateField(verbose_name = "Дата создания", auto_now_add = True)
    date_update = models.DateField(verbose_name = "Дата изменения", auto_now = True)
    client = models.ForeignKey(Client, verbose_name = "Клиент", on_delete = models.CASCADE)
    total_price = models.DecimalField(verbose_name = "Сумма", max_digits = 11, decimal_places = 2)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class Ordered_product(models.Model):
    order = models.ForeignKey(Order, verbose_name = "Заказ", on_delete = models.CASCADE)
    product = models.ForeignKey(Product, verbose_name = "Товар", on_delete = models.CASCADE)
    price = models.DecimalField(verbose_name = "Цена", max_digits = 11, decimal_places = 2)
    quantity = models.PositiveIntegerField(verbose_name = "Количество")

    class Meta:
        verbose_name = "Заказанный товар"
        verbose_name_plural = "Заказанные товары"


