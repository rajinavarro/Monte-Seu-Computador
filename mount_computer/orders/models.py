from django.db import models
from products.models import *
from products.views import *
from .validators import *
# Create your models here.

class Order(models.Model):
    user = models.CharField(max_length=120)
    cpu = models.ManyToManyField(Cpu, validators=[validate_cpu])
    motherboard = models.ManyToManyField(Motherboard)
    videocard = models.ManyToManyField(VideoCard)
    rammemory = models.ManyToManyField(RamMemory)
    class Meta:
        verbose_name = u'Order'
        verbose_name_plural = u'Orders'
    def __str__(self):
        return self.user
