from django.db import models
from .models import Order
from .serializers import OrderSerializer
from products.views import *
from products.models import *

class OrderViewSet(ModelViewSet):

    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        user = self.request.query_params.get('user',None)
        if user:
            queryset = Order.objects.filter(user=user)
        return queryset
