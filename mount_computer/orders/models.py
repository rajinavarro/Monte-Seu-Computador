from django.db import models
from products.models import *
from products.views import *

class Order(models.Model):
    name = models.CharField(max_length=120, default=None, blank=True, null=True)

    cpu = models.CharField(max_length=200, verbose_name='cpu', default=None, blank=True, null=True)
    
    motherboard = models.CharField(max_length=200, verbose_name='motherboard', default = None, blank=True, null=True)
    
    videocard = models.CharField(max_length=200, default=None, blank=True, null=True)
    
    rammemory = models.CharField(max_length=200, default=None, null=True, blank=True)
    
    rammemory2 = models.CharField(max_length=200, default=None, null=True, blank=True)

    rammemory3 = models.CharField(max_length=200, default=None, null=True, blank=True)

    rammemory4 = models.CharField(max_length=200, default=None, null=True, blank=True)

    def __str__(self):    
        return self.name
        
    
   
    