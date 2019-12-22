from rest_framework.serializers import ModelSerializer
from products.models import *

class CpuSerializer(ModelSerializer):
    class Meta:
        model = Cpu
        fields = '__all__'


class MotherboardSerializer(ModelSerializer):
    class Meta:
        model = Motherboard
        fields = '__all__'


class RamMemorySerializer(ModelSerializer):
    class Meta:
        model = RamMemory
        fields = '__all__'


class VideoCardSerializer(ModelSerializer):
    class Meta:
        model = VideoCard
        fields = '__all__'
