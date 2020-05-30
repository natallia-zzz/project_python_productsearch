from django.db import models

# Create your models here.
class Product(models.Model):
   pr_id = models.CharField('id',max_length=30)
   pr_title = models.CharField('title',max_length=100)
   pr_description =  models.CharField('description',max_length=15000)
   pr_manufacturer = models.CharField('manufacturer',max_length=30)
   pr_price = models.DecimalField('price',max_digits=8, decimal_places=2)
