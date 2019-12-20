from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Cpu, VideoCard, RamMemory, Motherboard
from .serializers import CpuSerializer, MotherboardSerializer, VideoCardSerializer, RamMemorySerializer

# Create your views here.

class CpuViewSet(ModelViewSet):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer
    #http_method_names = ['get']


class MotherboardViewSet(ModelViewSet):
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer
    #http_method_names = ['get']

class RamMemoryViewSet(ModelViewSet):
    queryset = RamMemory.objects.all()
    serializer_class = RamMemorySerializer
    #http_method_names = ['get']

class VideoCardViewSet(ModelViewSet):
    queryset = VideoCard.objects.all()
    serializer_class = VideoCardSerializer
    #http_method_names = ['get']

