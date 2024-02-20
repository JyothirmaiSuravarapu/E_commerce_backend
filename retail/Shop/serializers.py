from rest_framework import serializers
from Shop.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title','created']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'main_img', 'Product_name', 'Category', 'Preview_text', 'details', 'price', 'old_price', 'created']






