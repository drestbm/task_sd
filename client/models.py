from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Client(models.Model):
    '''Модель клиента'''
    user = models.OneToOneField(User, verbose_name = "Пользователь", related_name = "client", on_delete=models.CASCADE) #Связь с втроенной моделью User
    patronymic = models.CharField(verbose_name = "Отчество", max_length=50)                                             #Отчество
    phone = PhoneNumberField(verbose_name = "Телефон", null=False, blank=False, unique=True)                            #Номер телефона в виде +7##########
    address = models.TextField(verbose_name = "Адрес")                                                                  #Адрес - просто текст(в дальнейшем можно стандартизировать)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
