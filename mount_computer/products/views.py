from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from .forms import * 


def products_list(request, *args, **kwargs):
    obj = Cpu.objects.all()
    context = {
        'cpu': 'http://127.0.0.1:8000/products/cpu-list/',

        'motherboard': 'http://127.0.0.1:8000/products/motherboard-list/',
        
        'videocard': 'http://127.0.0.1:8000/products/videocard-list/',
        
        'rammemory': 'http://127.0.0.1:8000/products/rammemory-list/'
    }
    return render(request, 'products/products.html', context)


def add_cpu(request):
    form = CpuForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CpuForm()
    context = {
        'form':form
    }
    return render(request, "products/cpu-add.html", context)

def add_motherboard(request):
    form = MotherBoardForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MotherBoardForm()
    context = {
        'form':form
    }
    return render(request, "products/motherboard-add.html", context)

def add_videocard(request):
    form = VideocardForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = VideocardForm()
    context = {
        'form':form
    }
    return render(request, "products/videocard-add.html", context)

def add_rammemory(request):
    form = RamMemoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RamMemoryForm()
    context = {
        'form':form
    }
    return render(request, "products/rammemory-add.html", context)

def motherboard_list(request, *args, **kwargs):
    obj = Motherboard.objects.all()
    context = {
        'name': obj
    }
    return render(request, 'products/motherboard-list.html', context)

def videocard_list(request, *args, **kwargs):
    obj = VideoCard.objects.all()
    context = {
        'name': obj
    }
    return render(request, 'products/videocard-list.html', context)
    
def rammemory_list(request, *args, **kwargs):
    obj = RamMemory.objects.all()
    context = {
        'name': obj
    }
    return render(request, 'products/rammemory-list.html', context)
    
def cpu_list(request, *args, **kwargs):
    obj = Cpu.objects.all()
    context = {
        'name': obj,
        'enterprise': obj
    }
    return render(request, 'products/cpu-list.html', context)

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