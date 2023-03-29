from django.urls import path
from .views import *

urlpatterns = [
    path('post/',PostViewSet.as_view()),
    path('update/<int:pk>/', updated_at.as_view()),
    
    
    
     

 ]