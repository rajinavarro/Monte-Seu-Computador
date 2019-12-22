from rest_framework.serializers import ModelSerializer
from orders.models import Order
from products.models import *


class CpuSerializer(ModelSerializer):
    class Meta:
        model = Cpu
        fields = ['name']


class MotherboardSerializer(ModelSerializer):
    class Meta:
        model = Motherboard
        fields = ['name']


class RamMemorySerializer(ModelSerializer):
    class Meta:
        model = RamMemory
        fields = ['name']



class VideoCardSerializer(ModelSerializer):
    class Meta:
        model = VideoCard
        fields = ['name']

class OrderSerializer(ModelSerializer):
    cpu = CpuSerializer(many=True,required=True)
    print(cpu)
    motherboard = MotherboardSerializer(many=True, required=True)
    rammemory = RamMemorySerializer(many=True, required=True)
    videocard = VideoCardSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'

