from django import forms
from .models import *

class CpuForm(forms.ModelForm):
    class Meta:
        model = Cpu
        fields = '__all__'

class MotherBoardForm(forms.ModelForm):
    class Meta:
        model = Motherboard
        fields = '__all__'
        
class VideocardForm(forms.ModelForm):
    class Meta:
        model = VideoCard
        fields = '__all__'
        
class RamMemoryForm(forms.ModelForm):
    class Meta:
        model = RamMemory
        fields = '__all__'
        