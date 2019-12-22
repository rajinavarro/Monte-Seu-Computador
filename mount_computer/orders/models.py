from django.db import models
from products.models import *
from products.views import *
from .validators import *
# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=120, default='default')
    cpu = models.ManyToManyField(Cpu).name
    motherboard = models.ManyToManyField(Motherboard).name
    videocard = models.ManyToManyField(VideoCard)
    rammemory = models.ManyToManyField(RamMemory)
    '''
    class Meta:
        verbose_name = u'Order'
        verbose_name_plural = u'Orders'
    '''
    def __str__(self):
        return self.name
