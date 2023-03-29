from django.db import models
from django.contrib.auth.models import User


 
class Post(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.IntegerField()
    username= models.CharField(max_length=60)


# Create your models here.
