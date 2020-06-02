from django.contrib import admin
from .models import Product, Basket
# Register your models here.
class PrAdmin(admin.ModelAdmin):
    list_display = ("pr_title", "pr_manufacturer","pr_price")
admin.site.register(Product, PrAdmin)

class BasAdmin(admin.ModelAdmin):
    list_display = ("id", "prod_id","user_id", "inbasket")
admin.site.register(Basket, BasAdmin)