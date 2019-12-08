from django.db import models
from client.models import Client
from product.models import Product

class Order(models.Model):
    '''Модель заказа'''
    id = models.PositiveIntegerField(verbose_name = "Идентификатор", primary_key = True)            #Идентификатор (собирается в методе create сериалайзера)
    date_create = models.DateField(verbose_name = "Дата создания", auto_now_add = True)             #Дата создания проставляется автоматически
    date_update = models.DateField(verbose_name = "Дата изменения", auto_now = True)                #Дата изменения проставляется автоматически
    client = models.ForeignKey(Client, verbose_name = "Клиент", on_delete = models.CASCADE)         #Клиент, который создал заказ
    total_price = models.DecimalField(verbose_name = "Сумма", max_digits = 11, decimal_places = 2)  #Сумма заказа

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class Ordered_product(models.Model):
    '''Модель заказанного товара, для связи товаров с заказом, учета количества и общей цены'''
    order = models.ForeignKey(Order, verbose_name = "Заказ", related_name = "ordered_product", on_delete = models.CASCADE)      #Связь с заказом
    product = models.ForeignKey(Product, verbose_name = "Товар", related_name = "ordered_product", on_delete = models.CASCADE)  #Связь с товаром
    price = models.DecimalField(verbose_name = "Цена", max_digits = 11, decimal_places = 2)                                     #Цена за все количество товарра
    quantity = models.PositiveIntegerField(verbose_name = "Количество")                                                         #Количество товара

    class Meta:
        verbose_name = "Заказанный товар"
        verbose_name_plural = "Заказанные товары"


