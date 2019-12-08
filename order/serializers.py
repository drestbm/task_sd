import datetime

from .models import *
from client.serializers import Client_serializer
from product.serializers import Product_serializer

class Ordered_product_serilizer():
    '''Сериалайзер Ordered product'''

    def get(_object):
        '''Получение информации о заказанном товаре в виде словаря'''
        return {
            "id":_object.id,
            "price": round(float(_object.price),2),
            "quantity": _object.quantity,
            "product": Product_serializer.get(_object.product)
        }

    def create(data, order):
        '''Создание заказанного товара'''
        product = Product.objects.get(id = data["product"]["id"])
        quantity = data["quantity"]
        price =  product.price * quantity
        return Ordered_product.objects.create(
            product = product,
            price = price,
            quantity = quantity,
            order = order
        )

    def update(data, order):
        '''Изменение заказанного товара'''
        _id = data.pop("id")
        ordered_product = Ordered_product.objects.get(id = _id)
        product = data.pop("product")
        if ordered_product.product.id != product["id"]:
            new_product = Product.objects.get(id = product["id"])
            ordered_product.product = new_product
        ordered_product.order = order
        for key in data:
            setattr(ordered_product, key, data[key])
        ordered_product.save()
        ordered_product.price = ordered_product.product.price * ordered_product.quantity
        ordered_product.save()
        return ordered_product

class Order_serializer():
    '''Сериалайзер Order'''

    def get(_object):
        '''Получение информации о заказе в виде словаря'''
        ord_products = _object.ordered_product.all()
        ord_products_mas = [Ordered_product_serilizer.get(item) for item in ord_products]
        return {
            "id": _object.id,
            "date_create": _object.date_create,
            "date_update": _object.date_update,
            "client": Client_serializer.get(_object.client),
            "total_price": round(float(_object.total_price),2),
            "ordered_products": ord_products_mas
        }

    def create(data):
        '''Создание заказа'''
        date_now = datetime.datetime.now()
        last_order = Order.objects.filter(date_create = date_now).order_by("-id")
        if len(last_order) == 0:
            _id = int(date_now.strftime("%Y%m%d")  + str(1))
        else:
             _id = last_order[0].id + 1
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
        '''Изменение заказа'''
        _id = data.pop("id")
        order = Order.objects.get(id = _id)
        if "client" in data:
            data.pop("client")
        if "ordered_products" in data:
            data_ordered_products = data.pop("ordered_products")
            update_list = []
            create_list = []
            for item in data_ordered_products:
                if "id" in item:
                    update_list.append(item)
                else:
                    create_list.append(item)
            ordered_products = order.ordered_product.all()
            sum = 0
            for item in update_list:
                ordered_products = ordered_products.exclude(id = item["id"])
                ord_product = Ordered_product_serilizer.update(item, order)
                sum += ord_product.price
            ordered_products.delete()
            for item in create_list:
                ord_product = Ordered_product_serilizer.create(item, order)
                sum += ord_product.price
        data["total_price"] = sum
        for key in data:
            setattr(order, key, data[key])
        order.save()
        return order



