from django.db import models
from products.models import Cpu, RamMemory, VideoCard, Motherboard

# Create your models here.

class Order(models.Model):
    
    cpu = models.ManyToManyField(Cpu)
    motherboard = models.ManyToManyField(Motherboard)
    ramMemory = models.ManyToManyField(RamMemory)
    videoCard = models.ManyToManyField(VideoCard)
    

    def __str__(self):
        
        return self.cpu