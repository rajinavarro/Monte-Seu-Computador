from django.db import models
from products.models import *
from products.views import *
from django.core import validators
class Order(models.Model):
    name = models.CharField(max_length=120, default='default')
    cpu = models.ManyToManyField(Cpu)
    motherboard = models.ManyToManyField(Motherboard)
    videocard = models.ManyToManyField(VideoCard)
    rammemory = models.ManyToManyField(RamMemory)


    def __str__(self):
        return self.name