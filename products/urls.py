from django.urls import path
from . import views
urlpatterns = [
    path('', views.product_list, name='product-list'),
    # path('add/', views.addproduct_list, name='addproduct-list'),
    path('<int:pk>/', views.product_detail, name='product-detail'),
    path('search/', views.search_products, name='search_products'),
    path('search/', views.search_products, name='search_products'),
]
