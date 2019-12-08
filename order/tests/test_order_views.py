from django.contrib.auth.models import User, AnonymousUser
from django.test import RequestFactory, TestCase
from order.models import *
from order.serializers import *
from order.views import *
import pytest
import datetime
import json

@pytest.mark.django_db
class Test_order_views(TestCase):
    '''Тестирование Order view'''

    @classmethod
    def setUpClass(cls):
        '''Заполнение тестовой бд'''
        super(Test_order_views, cls).setUpClass()
        product = Product.objects.create(
            name = "Холодильник",
            description = "Описание холодильника",
            price = 10000.80
        )
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

    def test_order_view_get_200(self):
        '''Тестирование функции get() при верном запросе'''
        request = RequestFactory().get('/order/?id='+ datetime.datetime.now().strftime("%Y%m%d")  + str(1))
        order_view = OrderView()
        response = order_view.get(request = request)
        assert response.status_code == 200

    def test_order_view_get_404(self):
        '''Тестирование функции get() при запросе заказа, которого не существует'''
        request = RequestFactory().get('/order/?id='+ datetime.datetime.now().strftime("%Y%m%d")  + str(2))
        order_view = OrderView()
        response = order_view.get(request = request)
        assert response.status_code == 404

    def test_order_view_put_200(self):
        '''Тестирование функции put() при верном запросе'''
        data = json.dumps({
            "client": {
                "id": 1
            },
            "ordered_products": [{
                "quantity": 3,
                "product": {
                    "id": 1
                }
            }]
        })
        request = RequestFactory().put(
            path = '/order/',
            data = data,
            content_type = 'application/json')
        user = User.objects.get(id = 1)
        request.user = user
        order_view = OrderView()
        response = order_view.put(request = request)
        assert response.status_code == 201

    def test_order_view_put_401(self):
        '''Тестирование функции get() если пользоватль не авторизирован'''
        data = json.dumps({
            "client": {
                "id": 1
            },
            "ordered_products": [{
                "quantity": 3,
                "product": {
                    "id": 1
                }
            }]
        })
        request = RequestFactory().put(
            path = '/order/',
            data = data,
            content_type = 'application/json')
        request.user = AnonymousUser()
        order_view = OrderView()
        response = order_view.put(request = request)
        assert response.status_code == 401

    def test_order_view_put_400(self):
        '''Тестирование функции get() при невереном запросе'''
        data = json.dumps({
            "client": {
                "id": 1
            },
            "ordered_products": [{
                "quantity": 3,
                "product": {
                    "id": 1
                }
            }]
        })
        request = RequestFactory().put(
            path = '/order/',
            data = data,
            content_type = 'application/json')
        order_view = OrderView()
        response = order_view.put(request = request)
        assert response.status_code == 400