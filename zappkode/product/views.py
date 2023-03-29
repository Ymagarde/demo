
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status
from .serializers import ProductSerializer
from .models import Product

class ProductViewSet(APIView):

  def get(self, request):
    product_list = Product.objects.all()
    serializer = ProductSerializer(product_list , many = True) 
    return Response(serializer.data)


  def post(self , request) :
    serializer = ProductSerializer(data=request.data) 
    if serializer.is_valid():              
      serializer.save()  
      return Response("successfully created ")  
    else:
      return Response(serializer.errors)





class updated_at(APIView):

  def get(self, request,pk):
    pro = Product.objects.get(product_id=pk)
    serializer = ProductSerializer(pro)    
    return Response(serializer.data)


  def delete(self, request,pk):
    pro = Product.objects.get(product_id=pk)
    pro.delete()
    return Response("product is successfully delete") 


  def put(self, request, pk, format=None):
    pro = Product.objects.get(product_id=pk)
    serializer = ProductSerializer(pro, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
