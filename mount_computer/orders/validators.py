from django.core.exceptions import ValidationError
from products.models import *

def validate(data):
    
    # Verifying if name, motherboard or cpu fields are empty.
    if(data['name'] == None or data['motherboard'] == None or data['cpu'] == None):
        raise ValidationError("You can't leave this fields blank") 

    # Verifying if cpu, motherboard or videocard have more than one item.
    if (type(data['cpu']) != str or type(data['motherboard']) != str or (type(data['videocard']) != str and data['videocard'] != None )):
        raise FieldError("You can't choose more than one")
    
    # Attribute data fields to your respective item in Products list.
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

    try:
        rammemory3 = RamMemory.objects.get(ram_size=data['rammemory3'])
    except:
        rammemory3 = None

    try:
        rammemory4 = RamMemory.objects.get(ram_size=data['rammemory4'])
    except:
        rammemory4 = None

    # Verifying if motherboard have support for CPU choosed
    if (motherboard.supported_cpu != cpu.enterprise):
        if(motherboard.supported_cpu != 'Intel e AMD'):
            raise ValidationError("Motherboard doesn't support this CPU")

    # Verifying if at least one ram memory are chosen.
    if(rammemory == None and rammemory2 == None):
        raise ValidationError('You have to choose at least one ram memory ')

    # Verifying if ram memories are in limit specified 
    if(motherboard.supported_ram_size < rammemory.ram_size):
        raise ValidationError("Motherboard doesn't support this ram size")

    # Verifying number of RAM and supported number of rams of motherboard
    list_of_ram = [rammemory, rammemory2, rammemory3, rammemory4]
    counter = 0
    for index in list_of_ram:
        if index != None:
            counter += 1
    if (motherboard.ram_slots < counter):
        raise ValidationError("You can't choose more RAM than motherboard supports")

    # Verifying if motherboard support the size of two ram memory
    
    # Verifying if motherboard need videocard
    if(motherboard.integrated_video == False and videocard == None):
        raise ValidationError("Your motherboard doesn't have integrated video, you have to choose one video card ")
    return True
