from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.views import generic
from django.db.models import Q

# Create your views here.
class HomePageView(generic.TemplateView):
    template_name = 'products/home.html'

class ResultsView(generic.ListView):
    model = Product
    template_name = 'products/results.html'
    context_object_name = 'results'
    def get_queryset(self):
        query = self.request.GET.get('res')
        result = Product.objects.filter(Q(pr_title__icontains=query)|Q(pr_description__icontains=query)|Q(pr_description__icontains=query))
        return result
    #latest_list = Product.objects.all
    #context = {'latest_list': latest_list}
    #return render(request, 'products/results.html', context)
