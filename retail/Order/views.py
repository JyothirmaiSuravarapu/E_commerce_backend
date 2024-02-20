from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from Order.models import Cart, Order
from .serializers import CartSerializer, OrderSerializer
from Shop.serializers import ProductSerializer
from Shop.models import Product

## endpoint for cart Items

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_items(request):
    user = request.user
    cart_items = Cart.objects.filter(user = user, purchased = False)
    serializer = CartSerializer(cart_items, many=True)
    return Response(serializer.data)

##endpoint for adding to cart
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
@permission_classes([AllowAny]) #For testing purposes
def add_to_cart(request):
    # user = request.user
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity')

    try:
        product = Product.objects.get(pk=product_id)
    except:
        return Response({'ERROR':'Product not found!!'}, status =400)
    
    cart_item, created = Cart.objects.get_or_create(user=None, item=product, purchased=False)##modified for api testing purposes
    cart_item.quantity += int(quantity)
    cart_item.save()

    return Response({'message': 'Item added to cart!!'})

## For updating quantity in the cart
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
@permission_classes([AllowAny])
def update_cart(request):
    user = request.user
    cart_item_id = request.data.get('cart_item_id')
    new_quantity = request.data.get('quantity')

    try:
        cart_item = Cart.objects.get(pk=cart_item_id, user = None, purchased = False)#modifies
    except Cart.DoesNotExist:
        return Response({'error!!':'Cart item not found'}, status = 400)
    
    cart_item.quantity = int(new_quantity)
    cart_item.save()

    return Response({'message!!':'Cart item quantity updated'})

## remove option in cart
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request):
    user = request.user
    cart_item_id = request.data.get('cart_item_id')

    try:
        cart_item = Cart.objects.get(pk=cart_item_id, user = user, purchased = False)
    
    except Cart.DoesNotExist:
        return Response({'error!!':'Cart item does not exist'}, status = 400)
    
    cart_item.delete()
    cart_item.save()

    return Response({'message!!':'Cart item removed from cart!!'})

## cart total
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_total(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user, purchased = False)
    total = sum(item.get_total() for item in cart_items)
    return Response({'total':total})

## Order history
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_history(request):
    user = request.user
    orders = Order.objects.filter(user=user, ordered=True).order_by('-created')

    
    serializer = OrderSerializer(orders, many=True)

    return Response(serializer.data)




    






