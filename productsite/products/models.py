from django.db import models

# Create your models here.
class Product(models.Model):
   pr_id = models.CharField(max_length=12)
   pr_title = models.CharField(max_length=50)
   pr_description =  models.CharField(max_length=200)
   pr_manufacturer = models.CharField(max_length=30)
   pr_price = models.DecimalField(max_digits=8, decimal_places=2)

   
