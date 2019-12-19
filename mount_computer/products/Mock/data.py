from products.models import VideoCard
from products.serializers import VideoCardSerializer

cpu = Cpu(name='Processsador Intel Core i5', enterprise='Intel')
cpu.save()
cpu = Cpu(name='Processsador Intel Core i7', enterprise='Intel')
cpu.save()
cpu = Cpu(name='Processsador AMD Athlon', enterprise='AMD')
cpu.save()
cpu = Cpu(name='Processsador AMD RYzen 7', enterprise='AMD')
cpu.save()

motherboard = Motherboard(name='Placa Mãe Asus Prime', supported_cpu = 'Intel', ram_slots=2, supported_ram_size=16, integrated_video=False)
motherboard.save()
motherboard = Motherboard(name='Placa Mãe Gigabyte', supported_cpu = 'AMD', ram_slots=2, supported_ram_size=16, integrated_video=False)
motherboard.save()
motherboard = Motherboard(name='Placa Mãe ASRock Fatal', supported_cpu = 'Intel e AMD', ram_slots=4, supported_ram_size=64, integrated_video=True)
motherboard.save()

ram = RamMemory(ram_size=4)
ram.save()
ram = RamMemory(name='Hiper X',ram_size=8)
ram.save()
ram = RamMemory(name='Hiper X',ram_size=16)
ram.save()
ram = RamMemory(name='Hiper X',ram_size=32)
ram.save()

ram = RamMemory(name='Hiper X',ram_size=64)
ram.save()

videocard = VideoCard(name='Placa de Video Gigabyte Geforce GTX 1060 6GB')
videocard.save()

videocard = VideoCard(name='Placa de Video PNY RTX 2060 6GB')

videocard.save()
videocard = VideoCard(name='Placa de Video Radeon RX 580 8GB')
videocard.save()

print(cpu.name, cpu.enterprise)
