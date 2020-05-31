from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.views import generic
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

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
        return result.order_by('pr_price')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'products/signup.html', {'form': form})