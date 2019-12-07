from django.contrib.auth.models import User
from client.models import Client
from client.serializers import Client_serializer
import pytest

@pytest.mark.django_db
class Test_client_serializers:

    def test_client_serializer_get(self):
        user = User.objects.create(
            first_name = "Дмитрий",
            last_name = "Хван",
            email = "drestbm@yandex.ru"
        )
        client = Client.objects.create(
            user = user,
            patronymic = "Максимович",
            phone = "+79134776995",
            address = "г.Новосибирск, ул.Хилокская"
        )
        assert Client_serializer.get(client) == {
            "id": 1,
            "first_name": "Дмитрий",
            "last_name": "Хван",
            "email": "drestbm@yandex.ru",
            "patronymic": "Максимович",
            "phone": "+79134776995",
            "address": "г.Новосибирск, ул.Хилокская"
        }