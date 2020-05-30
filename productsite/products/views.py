from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'products/home.html', {})

def results(request):
    latest_list = Product.objects.all
    context = {'latest_list': latest_list}
    return render(request, 'products/results.html', context)
