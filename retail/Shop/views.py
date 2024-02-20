from django.shortcuts import render
from Shop.models import Category, Product
from django.views.generic import ListView, DetailView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, CategorySerializer


# Create your views here.

## for products
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

## api to fetch the product detail
@api_view(['GET'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)



## for categories
@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_details(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

## for searching products
@api_view(['GET'])
def search_products(request):
    query = request.query_params.get('query')
    products = Product.objects.filter(Product_name__icontains=query)

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

## for filtering for now filtering based on categories and price
@api_view(['GET'])
def filter_products(request):
    products = Product.objects.all()

    # by category
    category = request.GET.get('category')
    if category:
        products = products.filter(Category__title = category)

    # by price
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price and max_price:
        products = products.filter(price__range=(min_price, max_price))
    
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)









