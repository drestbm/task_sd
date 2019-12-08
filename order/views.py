from django.http import JsonResponse, HttpResponse
from django.views import View

from .serializers import *
from .models import *

import json

class OrderView(View):

    def get(self, request):
        '''Получение заказа'''
        try:
            order = Order.objects.get(id = request.GET["id"])
            return JsonResponse(data = Order_serializer.get(order), status = 200)
        except:
            return HttpResponse(status = 404)


    def put(self, request):
        '''Создание/изменение зааказа'''
        try:
            if request.user.is_authenticated:
                data = json.loads(request.body)
                if "id" not in data:
                    order = Order_serializer.create(data)
                else:
                    order = Order_serializer.update(data)
                return JsonResponse(data = Order_serializer.get(order), status = 201)
            return HttpResponse(status = 401)
        except:
            return HttpResponse(status = 400)