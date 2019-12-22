from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from .models import Order
from .serializers import OrderSerializer
from products.views import *
from products.models import *


def orders_list(request, *args, **kwargs):
    obj = Order.objects.all()

    context = {
        'name': obj
        }
    return render(request, 'orders/orders.html', context)


class OrderViewSet(ModelViewSet):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    '''
    def get_queryset(self):
        queryset = Order.objects.all()
        user = self.request.query_params.get('user',None)
        if user:
            queryset = Order.objects.filter(user=user)
        return queryset
    '''
