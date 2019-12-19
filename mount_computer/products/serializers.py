from rest_framework import serializers
from .models import * 

class CpuSerializer(serializers.Serializer):
    class Meta:
        model = Cpu
        fields = '__all__'

class MotherboardSerializer(serializers.Serializer):
    class Meta:
        model = Motherboard
        fields = '__all__'

class RamMemorySerializer(serializers.Serializer):
    class Meta:
        model = RamMemory
        fields = '__all__'

class VideoCardSerializer(serializers.Serializer):
    class Meta:
        model = VideoCard
        fields = '__all__'