from django.db import models

class Product(models.Model):
    '''Модель товара'''
    name = models.CharField(verbose_name = "Название", max_length=50)                       #Название
    description = models.TextField(verbose_name = "Описание")                               #Описание
    price = models.DecimalField(verbose_name = "Цена", max_digits = 8, decimal_places = 2)  #Цена одной единицы товара

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
