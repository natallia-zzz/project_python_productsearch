from django.contrib import admin
from .models import Product
# Register your models here.
class PrAdmin(admin.ModelAdmin):
    list_display = ("pr_title", "pr_manufacturer","pr_price")
admin.site.register(Product, PrAdmin)
