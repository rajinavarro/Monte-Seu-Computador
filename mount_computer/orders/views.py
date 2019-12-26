from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from .models import Order
from .serializers import OrderSerializer
from products.views import *
from products.models import *
from .models import Order
from .forms import *

class OrderViewSet(ModelViewSet):
    
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

def add_order(request):
    form = OrderForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = OrderForm()
        
        
    context = {
        'form':form
    }
    
    
    return render(request, "orders/order-add.html", context)



    
