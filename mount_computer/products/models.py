from django.db import models

class Cpu(models.Model):
    name = models.CharField(max_length=60)
    enterprise = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name

class Motherboard(models.Model):
    name = models.CharField(max_length=80)
    supported_cpu = models.CharField(max_length=100)
    ram_slots = models.IntegerField()
    supported_ram_size = models.IntegerField()
    integrated_video = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class RamMemory(models.Model):
    ram_size = models.IntegerField()
    name = models.CharField(max_length=7,default='Hiper X')

    def __str__(self):
        return self.name + ' ' + str(self.ram_size)

class VideoCard(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

