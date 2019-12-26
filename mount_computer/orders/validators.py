from django.core.exceptions import ValidationError
from products.models import *

def validate(data):
    cpu = Cpu.objects.get(name=data['cpu'])
    motherboard = Motherboard.objects.get(name=data['motherboard'])

    try:
        videocard = VideoCard.objects.get(name=data['videocard'])
    except:
        videocard = None

    try:
        rammemory = RamMemory.objects.get(ram_size=data['rammemory'])
    except:
        rammemory = None

    try:
        rammemory2 = RamMemory.objects.get(ram_size=data['rammemory2'])
    except:
        rammemory2 = None

    if (type(data['cpu']) != str or type(data['motherboard']) != str):
        raise ValidationError("You can't choose more than one")
        return False

    if (motherboard.supported_cpu != cpu.enterprise):
        if(motherboard.supported_cpu != 'Intel e AMD'):
            raise ValidationError("Motherboard doesn't support this CPU")
            return False

    if(rammemory == None and rammemory2 == None):
        raise ValidationError('You have to choose at least one ram memory ')
        return False

    if(motherboard.supported_ram_size < rammemory.ram_size):
        raise ValidationError("Motherboard doesn't support this ram size")
        return False

    if (rammemory2 != None and rammemory != None and (rammemory.ram_size + rammemory2.ram_size) > motherboard.supported_ram_size):
        raise ValidationError("Motherboard doesn't support this ram size")
        return False

    if(motherboard.integrated_video == False and videocard == None):
        raise ValidationError("Your motherboard doesn't have integrated video, you have to choose one video card ")
        return False
    return True