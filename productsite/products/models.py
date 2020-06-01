from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
   pr_id = models.CharField('id', primary_key = True, max_length=12)
   pr_title = models.CharField('title',max_length=100)
   pr_description =  models.CharField('description',max_length=15000)
   pr_manufacturer = models.CharField('manufacturer',max_length=30)
   pr_price = models.DecimalField('price',max_digits=8, decimal_places=2)

class Basket(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   prod = models.ForeignKey('products.Product', on_delete=models.CASCADE)
   num = models.IntegerField(default = 1)