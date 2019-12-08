from django.contrib.auth.models import User
from order.models import *
from order.serializers import *
from django.test import TestCase
import pytest
import datetime

@pytest.mark.django_db
class Test_ordered_product_serilizer(TestCase):
    '''Тестирование сериалайзера Ordered product'''

    @classmethod
    def setUpClass(cls):
        '''Заполнение тестовой бд'''
        super(Test_ordered_product_serilizer, cls).setUpClass()
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
        order = Order.objects.create(id = 1, client = client, total_price = 10000.80)
        ordered_product = Ordered_product.objects.create(
            order = order,
            price = 10000.80,
            quantity = 1,
            product = product1
        )

    def test_ordered_product_serializer_get(self):
        '''Тестирование функции get()'''
        ordered_product = Ordered_product.objects.get(id =1)
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
        '''Тестирование функции create()'''
        order = Order.objects.get(id = 1)
        data = {
            "quantity": 3,
            "product": {
                "id": 1
            }
        }
        ordered_product = Ordered_product_serilizer.create(data,order)
        assert Ordered_product_serilizer.get(ordered_product) == {
            "id": 2,
            "price": 30002.4,
            "quantity": 3,
            "product": {
                "id": 1,
                "name": "Холодильник",
                "description": "Описание холодильника",
                "price": 10000.8
            }
        }

    def test_ordered_product_serializer_update(self):
        '''Тестирование функции update()'''
        order = Order.objects.get(id = 1)
        data = {
            "id": 1,
            "quantity": 2,
            "product": {
                "id": 2
            }
        }
        ordered_product = Ordered_product_serilizer.update(data,order)
        assert Ordered_product_serilizer.get(ordered_product) == {
            "id": 1,
            "price": 26000.00,
            "quantity": 2,
            "product": {
                "id": 2,
                "name": "Телевизор",
                "description": "Описание телевизора",
                "price": 13000.00
            }
        }


@pytest.mark.django_db
class Test_order_serializers(TestCase):
    '''Тестирование сериалайзера Order'''

    @classmethod
    def setUpClass(cls):
        '''Заполнение тестовой бд'''
        super(Test_order_serializers, cls).setUpClass()
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
        order = Order.objects.create(id = int(datetime.datetime.now().strftime("%Y%m%d")  + str(1)), client = client, total_price = 10000.80)
        ordered_product = Ordered_product.objects.create(
            order = order,
            price = 10000.80,
            quantity = 1,
            product = product1
        )

    def test_order_serializer_get(self):
        '''Тестирование функции get()'''
        order = Order.objects.get(id = int(datetime.datetime.now().strftime("%Y%m%d")  + str(1)))
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
        '''Тестирование функции create()'''
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
            "id": int(datetime.datetime.now().strftime("%Y%m%d")  + str(2)),
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
                "id": 2,
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
        '''Тестирование функции update()'''
        order = Order_serializer.update({
            "id": int(datetime.datetime.now().strftime("%Y%m%d")  + str(1)),
            "ordered_products": [{
                "id": 1,
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
            "ordered_products": [
            {
                "id": 1,
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
                "id": 2,
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