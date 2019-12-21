from rest_framework.serializers import ModelSerializer
from orders.models import Order
from products.serializers import *

class OrderSerializer(ModelSerializer):
    cpu = CpuSerializer(many=True,required=True)
    print(cpu)
    motherboard = MotherboardSerializer(many=True, required=True)
    rammemory = RamMemorySerializer(many=True, required=True)
    videocard = VideoCardSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'