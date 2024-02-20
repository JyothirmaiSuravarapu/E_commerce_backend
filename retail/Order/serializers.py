from rest_framework import serializers
from .models import Cart, Order

class CartSerializer(serializers.ModelSerializer):
    item = serializers.StringRelatedField()
    class Meta:
        model = Cart
        fields = ['id', 'item', 'quantity', 'purchased', 'created', 'updated']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'  # You can specify the fields you want to include in the response


        