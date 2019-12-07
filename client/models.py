from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Client(models.Model):
    user = models.OneToOneField(User, verbose_name = "Пользователь", related_name = "client", on_delete=models.CASCADE)
    patronymic = models.CharField(verbose_name = "Отчество", max_length=50)
    phone = PhoneNumberField(verbose_name = "Телефон", null=False, blank=False, unique=True)
    address = models.TextField(verbose_name = "Адрес")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
