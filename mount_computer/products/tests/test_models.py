from django.test import TestCase
from model_mommy import mommy
from products.models import *

class TestCpu(TestCase):

    def setUp(self):
        self.cpu = mommy.make(Cpu, name='i5')
        self.cpu = mommy.make(Cpu, enterprise='Intel')
    def test_cpu_creation(self):
        self.assertTrue(isinstance(self.cpu, Cpu))
        self.assertEquals(self.cpu.__str__(), self.cpu.name)


class TestMotherboard(TestCase):

    def setUp(self):
        self.motherboard = mommy.make(Motherboard, name='asus')
        self.motherboard = mommy.make(Motherboard, supported_cpu='Intel')
        self.motherboard = mommy.make(Motherboard, ram_slots=2)
        self.motherboard = mommy.make(Motherboard, supported_ram_size=4)
    def test_motherboard_creation(self):
        self.assertTrue(isinstance(self.motherboard, Motherboard))
        self.assertEquals(self.motherboard.__str__(), self.motherboard.name)


class TestRamMemory(TestCase):

    def setUp(self):
        self.rammemory = mommy.make(RamMemory, name='Hiper X (8 GB)')
        self.rammemory = mommy.make(RamMemory, ram_size=8)
    def test_rammemory_creation(self):
        self.assertTrue(isinstance(self.rammemory, RamMemory))
        self.assertEquals(self.rammemory.__str__(), self.rammemory.name  + ' (8 GB)')

class TestVideoCard(TestCase):

    def setUp(self):
        self.videocard = mommy.make(VideoCard, name='Video card test')
    def test_videocard_creation(self):
        self.assertTrue(isinstance(self.videocard, VideoCard))
        self.assertEquals(self.videocard.__str__(), self.videocard.name)

