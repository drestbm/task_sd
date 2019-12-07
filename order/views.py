from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .serializers import *
from .models import *

import json

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class OrderView(View):
    def get(self, request):
        order = Order.objects.get(id = request.GET["id"])
        print(order.ordered_product.all()[0])
        return JsonResponse(Order_serializer.get(order))

    def put(self, request):
        data = json.loads(request.body)
        if "id" not in data:
            order = Order_serializer.create(data)
        else:
            order = Order_serializer.update(data)
        return JsonResponse(Order_serializer.get(order))

    def delete(self, request):
        Order.objects.get(id = request.GET["id"]).delete()
        return JsonResponse({"ok": "ok"})

# class OrderListView(View):
#     def get(self, request):