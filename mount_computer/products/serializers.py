from rest_framework import serializers
from .models import Cpu, Motherboard, RamMemory, VideoCard

class CpuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cpu
        fields = '__all__'

class MotherboardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Motherboard
        fields = '__all__'

class RamMemorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RamMemory
        fields = '__all__'

class VideoCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VideoCard
        fields = '__all__'