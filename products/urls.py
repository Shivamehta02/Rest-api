from django.urls import path
from . import views

urlpatterns = [
    
    path('api/', views.product_list, name='product-list'),
    # path('add/', views.addproduct_list, name='addproduct-list'),
    path('api/<int:pk>/', views.product_detail, name='product-detail'),
    path('api/search/', views.search_products, name='search_products'),
   
]
