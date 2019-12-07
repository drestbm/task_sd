from .models import *

class Client_serializer():
    def get(_object):
        return {
            "id": _object.id,
            "first_name": _object.user.first_name,
            "last_name": _object.user.last_name,
            "email": _object.user.email,
            "patronymic": _object.patronymic,
            "phone": str(_object.phone),
            "address": _object.address,
        }

    # def create(data):


    # def update(objects, data):
