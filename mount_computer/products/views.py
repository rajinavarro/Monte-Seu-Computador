from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CpuSerializer, MotherboardSerializer, RamMemorySerializer, VideoCardSerializer
from .models import Cpu, Motherboard, RamMemory, VideoCard
# Create your views here.

class CpuViewSet(viewsets.ModelViewSet):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer
    http_method_names = ['get']

class MotherboardViewSet(viewsets.ModelViewSet):
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer
    http_method_names = ['get']

class RamMemoryViewSet(viewsets.ModelViewSet):
    queryset = RamMemory.objects.all()
    serializer_class = RamMemorySerializer
    http_method_names = ['get']

class VideoCardViewSet(viewsets.ModelViewSet):
    queryset = VideoCard.objects.all()
    serializer_class = VideoCardSerializer
    http_method_names = ['get']