from django.db import models
from projectapp.models import Product
# Create your models here.
class Cartpage(models.Model):
    
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    user_id=models.IntegerField()
    
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()



    