from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


def get_queryset(self):
    queryset = Order.objects.all()
    id = self.request.query_params.get('id',None)
    if user:
        queryset = Order.objects.filter(id=id)
    return queryset


class CpuViewSet(ModelViewSet):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer

class MotherboardViewSet(ModelViewSet):
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer

class RamMemoryViewSet(ModelViewSet):
    queryset = RamMemory.objects.all()
    serializer_class = RamMemorySerializer

class VideoCardViewSet(ModelViewSet):
    queryset = VideoCard.objects.all()
    serializer_class = VideoCardSerializer