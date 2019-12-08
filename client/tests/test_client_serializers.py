from django.contrib.auth.models import User
from client.models import Client
from client.serializers import Client_serializer
from django.test import TestCase
import pytest


@pytest.mark.django_db
class Test_client_serializers(TestCase):
    '''Тестирование сериалайзера Client'''

    @classmethod
    def setUpClass(cls):
        '''Заполнение тестовой бд'''
        super(Test_client_serializers, cls).setUpClass()
        user = User.objects.create_user(
            username = "admin",
            first_name = "Дмитрий",
            last_name = "Хван",
            email = "drestbm@yandex.ru",
            password = "password"
        )
        client = Client.objects.create(
            user = user,
            patronymic = "Максимович",
            phone = "+79134776995",
            address = "г.Новосибирск, ул.Хилокская"
        )

    def test_client_serializer_get(self):
        '''Тестирование функции get()'''
        client = Client.objects.get(id = 1)
        assert Client_serializer.get(client) == {
            "id": 1,
            "first_name": "Дмитрий",
            "last_name": "Хван",
            "email": "drestbm@yandex.ru",
            "patronymic": "Максимович",
            "phone": "+79134776995",
            "address": "г.Новосибирск, ул.Хилокская"
        }