from django.urls import path
from . import views

urlpatterns = [
    
    path('api/', views.product_list, name='product-list'),#/api/?sort_by=price&sort_order=desc
    path('api/<int:pk>/', views.product_detail, name='product-detail'),
    path('api/search/', views.search_products, name='search_products'),# searching and pagination #/api/search/?query=phone
   
]
