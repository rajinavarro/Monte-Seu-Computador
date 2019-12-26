from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError
from django import forms
from orders.models import Order
from rest_framework import serializers
from .validators import validate
from products.models import *

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        

    def create(self, validated_data):
        
        if validate(self.data) == True:
            print('all fields are valid')
            return Order.objects.create(**validated_data)
        else:
            print('Not valid field')

