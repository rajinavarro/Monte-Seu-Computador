from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError
from orders.models import Order
from rest_framework import serializers
from .validators import validate

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
    
    def create(self, validated_data):
        if validate(self.data):
            return Order.objects.create(**validated_data)