from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=200)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    c_password=models.CharField(max_length=200)
    account_type = models.IntegerField(default=0)  # 0 for Buyer, 1 for Seller
    
    def __str__(self):
        return self.username