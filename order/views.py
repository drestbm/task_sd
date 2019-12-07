from django.http import JsonResponse, HttpResponse
from django.views import View

from .serializers import *
from .models import *

import json

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class OrderView(View):
    #Получение заказа
    def get(self, request):
        try:
            order = Order.objects.get(id = request.GET["id"])
            print(order.ordered_product.all()[0])
            return JsonResponse(data = Order_serializer.get(order), status = 200)
        except DoesNotExist:
            return HttpResponse(data = "Пользователь не найден", status = 404)

    #Создание/изменение зааказа
    def put(self, request):
        try:
            if request.user.is_authenticated:
                data = json.loads(request.body)
                if "id" not in data:
                    order = Order_serializer.create(data)
                else:
                    order = Order_serializer.update(data)
                return JsonResponse(data = Order_serializer.get(order), status = 201)
            return HttpResponse(status = 401)
        except DoesNotExist:
            return HttpResponse(status = 410)
        except:
            return HttpResponse(status = 400)