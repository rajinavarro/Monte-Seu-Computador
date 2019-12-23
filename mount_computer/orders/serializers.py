from rest_framework.serializers import ModelSerializer
from orders.models import Order
from products.models import *
from products.serializers import *
from rest_framework import serializers

class OrderSerializer(ModelSerializer):
    cpu = CpuSerializer(many=True, read_only=True)
    motherboard = MotherboardSerializer(many=True)
    videocard = VideoCardSerializer(many=True, required=False)
    rammemory = RamMemorySerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

