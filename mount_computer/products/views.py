from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CpuSerializer, MotherboardSerializer, RamMemorySerializer, VideoCardSerializer
from .models import Cpu, Motherboard, RamMemory, VideoCard

# Create your views here.

class CpuViewSet(viewsets.ModelViewSet):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer
    http_method_names = ['get']

    def cpu_GetValue(request):
        for cpu in queryset:
            print(choice_1 = cpu.choice.all()[0])
            print(choice_2 = cpu.choice.all()[1])
            print(choice_3 = cpu.choice.all()[2])
            print(choice_4 = cpu.choice.all()[3])



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

