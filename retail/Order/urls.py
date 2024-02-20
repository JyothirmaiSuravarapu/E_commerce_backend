from django.urls import path
from . import views

urlpatterns = [
    path('cart/items/', views.cart_items, name='cart-items'),
    path('cart/add/', views.add_to_cart, name='add-to-cart'),
    path('cart/update/', views.update_cart, name='update-cart'),
    path('cart/remove/', views.remove_from_cart, name='remove-from-cart'),
    path('cart/total/', views.cart_total, name='cart-total'),
]
