from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status
from .serializers import*
from .models import*

class PostViewSet(APIView):
  
  def get(self, request):
    Post_list = Post.objects.all()
    serializer = PostSerializer(Post_list , many = True) 
    return Response(serializer.data)
    

  def post(self , request) :
    serializer = PostSerializer(data=request.data) 
    if serializer.is_valid():              
      serializer.save()  
      return Response("successfully created ")  
    else:
      return Response(serializer.errors)





class updated_at(APIView):

  def get(self, request,pk):
    id=pk
    usr = Post.objects.get(pk=id)
    #usr = Post.objects.get(first_name='name')
    serializer = PostSerializer(usr)    
    return Response(serializer.data)


  def delete(self, request,pk):
    id=pk
    usr = Post.objects.get(pk=id)
    usr.delete()
    return Response("Post is successfully delete") 


  def put(self, request,pk):
    id=pk
    usr = Post.objects.get(pk=id)
    serializer = PostSerializer(usr, data=request.data)
    if serializer.is_valid():
      serializer.save()
      #return Response(serializer.data)
      return Response({'msg': 'Complete data Update'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.

