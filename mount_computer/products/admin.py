from django.contrib import admin
from .models import Cpu, Motherboard, RamMemory, VideoCard

# Register your models here.

admin.site.register(Cpu)
admin.site.register(Motherboard)
admin.site.register(RamMemory)
admin.site.register(VideoCard)
