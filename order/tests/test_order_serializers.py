from django.contrib.auth.models import User
from order.models import *
from order.serializers import *
import pytest
import datetime

@pytest.mark.django_db
class Test_ordered_product_serilizer():
    def test_ordered_product_serializer_get(self):
        product = Product.objects.create(
            name = "Холодильник",
            description = "Описание холодильника",
            price = 10000.80
        )
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
        order = Order.objects.create(id = 1, client = client, total_price = 10000.80)
        ordered_product = Ordered_product.objects.create(
            order = order,
            price = 10000.80,
            quantity = 1,
            product = product
        )
        assert Ordered_product_serilizer.get(ordered_product) == {
            "id": 1,
            "price": 10000.80,
            "quantity": 1,
            "product": {
                "id": 1,
                "name": "Холодильник",
                "description": "Описание холодильника",
                "price": 10000.80
            }
        }

    def test_ordered_product_serializer_create(self):
        product = Product.objects.create(
            name = "Холодильник",
            description = "Описание холодильника",
            price = 10000.8
        )
        data = {
            "quantity": 3,
            "product": {
                "id": 1
            }
        }
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
        order = Order.objects.create(id = 1, client = client, total_price = 10000.80)
        ordered_product = Ordered_product_serilizer.create(data,order)
        assert Ordered_product_serilizer.get(ordered_product) == {
            "id": 1,
            "price": 30002.4,
            "quantity": 3,
            "product": {
                "id": 1,
                "name": "Холодильник",
                "description": "Описание холодильника",
                "price": 10000.8
            }
        }


@pytest.mark.django_db
class Test_order_serializers:

    def test_order_serializer_get(self):
        product = Product.objects.create(
            name = "Холодильник",
            description = "Описание холодильника",
            price = 10000.80
        )
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
        order = Order.objects.create(id = 1, client = client, total_price = 10000.80)
        ordered_product = Ordered_product.objects.create(
            order = order,
            price = 10000.80,
            quantity = 1,
            product = product
        )
        assert Order_serializer.get(order) == {
            "id": 1,
            "date_create": datetime.datetime.now().date(),
            "date_update": datetime.datetime.now().date(),
            "client": {
                "id": 1,
                "first_name": "Дмитрий",
                "last_name": "Хван",
                "email": "drestbm@yandex.ru",
                "patronymic": "Максимович",
                "phone": "+79134776995",
                "address": "г.Новосибирск, ул.Хилокская"
            },
            "total_price": 10000.80,
            "ordered_products": [{
                "id": 1,
                "price": 10000.80,
                "quantity": 1,
                "product": {
                    "id": 1,
                    "name": "Холодильник",
                    "description": "Описание холодильника",
                    "price": 10000.80
                }
            }]
        }

    def test_order_serializer_create(self):
        product = Product.objects.create(
            name = "Холодильник",
            description = "Описание холодильника",
            price = 10000.80
        )
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
        order = Order_serializer.create({
            "client": {
                "id": 1,
            },
            "ordered_products": [{
                "quantity": 3,
                "product": {
                    "id": 1,
                }
            }]
        })
        assert Order_serializer.get(order) == {
            "id": int(datetime.datetime.now().strftime("%Y%m%d")  + str(1)),
            "date_create": datetime.datetime.now().date(),
            "date_update": datetime.datetime.now().date(),
            "client": {
                "id": 1,
                "first_name": "Дмитрий",
                "last_name": "Хван",
                "email": "drestbm@yandex.ru",
                "patronymic": "Максимович",
                "phone": "+79134776995",
                "address": "г.Новосибирск, ул.Хилокская"
            },
            "total_price": 30002.40,
            "ordered_products": [{
                "id": 1,
                "price": 30002.40,
                "quantity": 3,
                "product": {
                    "id": 1,
                    "name": "Холодильник",
                    "description": "Описание холодильника",
                    "price": 10000.80
                }
            }]
        }

    def test_order_serializer_update(self):
        product1 = Product.objects.create(
            name = "Холодильник",
            description = "Описание холодильника",
            price = 10000.80
        )
        product2 = Product.objects.create(
            name = "Телевизор",
            description = "Описание телевизора",
            price = 13000.00
        )
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
        order = Order_serializer.create({
            "client": {
                "id": 1,
            },
            "ordered_products": [{
                "quantity": 3,
                "product": {
                    "id": 1,
                }
            }]
        })
        order = Order_serializer.update({
            "id": int(datetime.datetime.now().strftime("%Y%m%d")  + str(1)),
            "ordered_products": [{
                "quantity": 3,
                "product": {
                    "id": 1,
                }
            },
            {
                "quantity": 1,
                "product": {
                    "id": 2,
                }
            }]
        })
        assert Order_serializer.get(order) == {
            "id": int(datetime.datetime.now().strftime("%Y%m%d")  + str(1)),
            "date_create": datetime.datetime.now().date(),
            "date_update": datetime.datetime.now().date(),
            "client": {
                "id": 1,
                "first_name": "Дмитрий",
                "last_name": "Хван",
                "email": "drestbm@yandex.ru",
                "patronymic": "Максимович",
                "phone": "+79134776995",
                "address": "г.Новосибирск, ул.Хилокская"
            },
            "total_price": 43002.4,
            "ordered_products": [{
                "id": 2,
                "price": 30002.40,
                "quantity": 3,
                "product": {
                    "id": 1,
                    "name": "Холодильник",
                    "description": "Описание холодильника",
                    "price": 10000.80
                }
            },
            {
                "id": 1,
                "price": 13000.00,
                "quantity": 1,
                "product": {
                    "id": 2,
                    "name": "Телевизор",
                    "description": "Описание телевизора",
                    "price": 13000.00
                }
            }]
        }

{'ordered_products': [{'id': 2, 'price': 30002.4, 'product': {'description': 'Описание холодильника', 'id': 1, 'name':....0, 'product': {'description': 'Описание телевизора', 'id': 2, 'name': 'Телевизор', 'price': 13000.0}, 'quantity': 1}]} != 
{'ordered_products': [{'id': 2, 'price': 30002.4, 'product': {'description': 'Описание холодильника', 'id': 1, 'name':....0, 'product': {'description': 'Описание телевизора', 'id': 2, 'name': 'Телевизор', 'price': 13000.0}, 'quantity': 1}]}