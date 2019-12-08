from product.models import Product
from product.serializers import Product_serializer
from django.test import TestCase
import pytest

@pytest.mark.django_db
class Test_product_serializers(TestCase):
    '''Тестирование сериалайзер Product'''

    @classmethod
    def setUpClass(cls):
        '''Заполнение тестовой бд'''
        super(Test_product_serializers, cls).setUpClass()
        product = Product.objects.create(
            name = "Холодильник",
            description = "Описание холодильника",
            price = 10000.80
        )

    def test_product_serializer_get(self):
        '''Тестирование функции get()'''
        product = Product.objects.get(id = 1)
        assert Product_serializer.get(product) == {
            "id": 1,
            "name": "Холодильник",
            "description": "Описание холодильника",
            "price": 10000.80
        }