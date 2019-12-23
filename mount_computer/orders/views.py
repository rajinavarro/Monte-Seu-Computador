from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from .models import Order
from .serializers import OrderSerializer
from products.views import *
from products.models import *
from .forms import *


def orders_list(request, *args, **kwargs):
    obj = Order.objects.all()
    print('obj = ',obj)
    context = {
        'name': obj
        }
    return render(request, 'orders/orders.html', context)


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    '''
    def get_queryset(self):
        queryset = Order.objects.all()
        user = self.request.query_params.get('user',None)
        if user:
            queryset = Order.objects.filter(user=user)
        return queryset
    '''
def add_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = OrderForm()
        
    context = {
        'form':form
    }
    
    return render(request, "orders/order-add.html", context)

