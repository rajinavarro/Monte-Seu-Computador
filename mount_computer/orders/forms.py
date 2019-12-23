from django import forms
from .models import *
from products.models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['videocard'].required = False

    def clean_cpu(self, *args, **kwargs):
        cpu = self.cleaned_data.get('cpu')
        
        index_list = []
        for index in cpu:
            index_list.append(index)
            if len(index_list) > 1:
                raise forms.ValidationError("You can't choose more than one cpu")
                return None     
        return cpu
    
    def clean_motherboard(self, *args, **kwargs):
        motherboard = self.cleaned_data.get('motherboard')
        cpu = self.cleaned_data.get('cpu')
        
        index_list = []
        for index in motherboard:
            motherboard_object = Motherboard.objects.get(name=index)
            index_list.append(index)
            if len(index_list) > 1:
                raise forms.ValidationError("You can't choose more than one motherboard")
                return motherboard
        print(motherboard_object.name)
        if cpu != None:
            for index in cpu:
                cpu_object = Cpu.objects.get(name=index)
            
            if(motherboard_object.supported_cpu != cpu_object.enterprise and motherboard_object.supported_cpu != 'Intel e AMD'):
                raise forms.ValidationError("Motherboard not compatible with cpu") 
        
        return motherboard

    def clean_rammemory(self, *args, **kwargs):
        rammemory = self.cleaned_data.get('rammemory')
        motherboard = self.cleaned_data.get('motherboard')

        rammemory_list = []
        total_ram = 0
        for index in rammemory:

            rammemory_list.append(index)
            total_ram += int(str(index)[7:])
            
        if(motherboard != None):
            for index in motherboard:
                motherboard_object = Motherboard.objects.get(name=index)
            
            if(motherboard_object.supported_ram_size < total_ram ):
                raise forms.ValidationError("Maximum RAM limit reached")
                return rammemory
            if(motherboard_object.ram_slots < len(rammemory_list)):
                raise forms.ValidationError("Maximum RAM slots limit reached")
                return rammemory
        return rammemory

    def clean_videocard(self, *args, **kwargs):
        videocard = self.cleaned_data.get('videocard')
        motherboard = self.cleaned_data.get('motherboard')
    
        index_list = []
        for index in videocard:
            index_list.append(index)
            if(len(index_list) > 1):
                raise forms.ValidationError("You can't choose more than one Videocard")
                return videocard
        if (motherboard != None):  
            for index in motherboard:
                motherboard_object = Motherboard.objects.get(name=index)
            
            if(motherboard_object.integrated_video == False and index_list == []):
                raise forms.ValidationError("You have to choose one videocard, because yout motherboard doesn't have integrated videocard")
                return videocard
        return videocard