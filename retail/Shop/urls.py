from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    # URLs for products
    path('api/products/', views.product_list, name = 'product-list'),
    path('api/products/<int:pk>', views.product_detail, name = 'product-detail'),

    # URLs for categories
    path('api/categories/', views.category_list, name='category-list'),
    path('api/categories/<int:pk>', views.category_details, name='category-details'),

    #for serach
    path('api/search/', views.search_products, name='search-products'),
    
    # for filter
    path('api/filter/', views.filter_products, name='filter-products'),

    #for order history
    # path('api/order-history/', views.order_history, name='order-history'),


]
