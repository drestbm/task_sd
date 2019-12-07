import datetime

from .models import *
from client.serializers import Client_serializer
from product.serializers import Product_serializer

class Ordered_product_serilizer():
    def get(_object):
        return {
            "id":_object.id,
            "price": _object.price,
            "quantity": _object.quantity,
            "product": Product_serializer.get(_object.product)
        }

    def create(data, order):
        product = Product.objects.get(id = data["product"]["id"])
        quantity = data["quantity"]
        price = product.price * quantity
        return Ordered_product.objects.create(
            product = product,
            price = price,
            quantity = quantity,
            order = order
        )

class Order_serializer():
    def get(_object):
        ord_products = _object.ordered_product.all()
        ord_products_mas = [Ordered_product_serilizer.get(item) for item in ord_products]
        return {
            "id": _object.id,
            "date_create": _object.date_create,
            "date_update": _object.date_update,
            "client": Client_serializer.get(_object.client),
            "total_price": _object.total_price,
            "ordered_products": ord_products_mas
        }

    def create(data):
        date_now = datetime.datetime.now()
        _id = date_now.strftime("%Y%m%d") + str(len(Order.objects.filter(date_create = date_now)) + 1)
        client = Client.objects.get(id = data.pop("client")["id"])
        ord_products = data.pop("ordered_products")
        order = Order.objects.create(
            id = _id,
            client = client,
            total_price = 0
        )
        sum = 0
        for item in ord_products:
            ord_product = Ordered_product_serilizer.create(item, order)
            sum += ord_product.price
        order.total_price = sum
        order.save()
        return order

    def update(data):
        _id = data.pop("id")
        order = Order.objects.get(id = _id)
        if "client" in data:
            data.pop("client")
        if "ordered_products" in data:
            ordered_products = data.pop("ordered_products")
            order.ordered_product.all().delete()
            sum = 0
            for item in ordered_products:
                ord_product = Ordered_product_serilizer.create(item, order)
                sum += ord_product.price
        data["total_price"] = sum
        for key in data:
            setattr(order, key, data[key])
        order.save()
        return order



