import datetime

from .models import *
from client.serializers import Client_serializer
from product.serializers import Product_serializer

class Order_serializer():
    def get(_object):
        return {
            "id": _object.id,
            "date_create": _object.date_create,
            "date_update": _object.date_update,
            "client": Client_serializer.get(_object.client),
            "total_price": _object.total_price,
        }

    def create(data):
        date_now = datetime.datetime.now()
        _id = date_now.strftime("%Y%m%d") + str(len(Order.objects.filter(date_create = date_now)) + 1)
        client = Client.objects.get(id = data.pop("client")["id"])
        return Order.objects.create(
            id = _id,
            client = client,
            total_price = data["total_price"]
        )

    def update(data):
        _id = data.pop("id")
        return Order.objects.update_or_create(id= _id, defaults = data)[0]

class Ordered_product_serilizer():
    def get(_object):
        return {
            "order": Order_serializer.get(_object.order),
            "product": Product_serializer.get(_object.product),
            "price": _object.price,
            "quntity": _object.quntity,
        }

