from django.db import models

class Product(models.Model):
    product_id = models.AutoField(auto_created=True,primary_key=True)
    product_name = models.CharField(max_length=100)
    product_weight = models.FloatField()
    product_price = models.FloatField()

    #def __str__(self):
        #return self.product_name

# Create your models here.

