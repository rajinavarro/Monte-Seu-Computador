from django.db import models
from products.models import *
from products.views import *
# Create your models here.

class Order(models.Model):
    
    cpu = models.ManyToManyField(Cpu)
    motherboard = models.ManyToManyField(Motherboard)
    videocard = models.ManyToManyField(VideoCard)
    rammemory = models.ManyToManyField(RamMemory)
    class Meta:
        verbose_name = u'Order'
        verbose_name_plural = u'Orders'
