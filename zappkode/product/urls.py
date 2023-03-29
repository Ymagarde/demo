from django.urls import path
from .import views
from .views import *

urlpatterns = [
    
    path('create/', ProductViewSet.as_view()),
    path('update/<int:pk>/', updated_at.as_view()),
    
     

 ]