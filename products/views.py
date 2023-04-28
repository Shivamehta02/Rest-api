from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from .serializers import ProductSerializer


from django.db.models import Q    # for searching
from rest_framework.pagination import PageNumberPagination   #for pagination

@api_view(['GET','POST'])
@csrf_exempt
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
 

@api_view(['GET','PUT', 'DELETE'])
@csrf_exempt
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=204) 

#only search
# @api_view(['GET'])
# def search_products(request):
   
#     query = request.GET.get('query', '')
#     if not query:
#         return Response({'error': 'No search query provided.'}, status=400)
    
#     products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)



# searching and pagination
@api_view(['GET'])
@csrf_exempt
def search_products(request):
   
    query = request.GET.get('query', '')
    if not query:
        return Response({'error': 'No search query provided.'}, status=400)
    
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    # Pagination
    paginator = PageNumberPagination()
    paginator.page_size = 10 # set the number of items per page
    paginated_products = paginator.paginate_queryset(products, request)
    
    serializer = ProductSerializer(paginated_products, many=True)
    return paginator.get_paginated_response(serializer.data)