from product.models import Product
from product.serializers import Product_serializer
import pytest

@pytest.mark.django_db
class Test_product_serializers:

    def test_product_serializer_get(self):
        product = Product.objects.create(
            name = "Холодильник",
            description = "Описание холодильника",
            price = 10000.80
        )
        assert Product_serializer.get(product) == {
            "id": 1,
            "name": "Холодильник",
            "description": "Описание холодильника",
            "price": 10000.80
        }