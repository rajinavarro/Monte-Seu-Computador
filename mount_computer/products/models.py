from django.db import models


# Create your models here.

class Cpu(models.Model):
    
    name = models.CharField(max_length=60)
    enterprise = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name

class Motherboard(models.Model):
    name = models.CharField(max_length=80)
    supported_cpu = models.CharField(max_length=20)
    ram_slots = models.IntegerField()
    supported_ram_size = models.IntegerField()
    integrated_video = models.BooleanField()

    def __str__(self):
        return self.name

class RamMemory(models.Model):
    name = 'Hiper X'
    ram_size = models.IntegerField()

    def __str__(self):
        return self.name

class VideoCard(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name