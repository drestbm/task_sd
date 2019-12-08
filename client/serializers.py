from .models import *

class Client_serializer():
    '''Сериалайзер Client'''
    
    def get(_object):
        '''Получение информации о клиенте в виде словаря'''
        return {
            "id": _object.id,
            "first_name": _object.user.first_name,
            "last_name": _object.user.last_name,
            "email": _object.user.email,
            "patronymic": _object.patronymic,
            "phone": str(_object.phone),
            "address": _object.address,
        }
