from .models import *
from client.serializers import Client_serializer

class Product_serializer():
    def get(_object):
        return {
            "id": _object.id,
            "name": _object.name,
            "description": _object.description,
            "price": round(float(_object.price),2),
        }
