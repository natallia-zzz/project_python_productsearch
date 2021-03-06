from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Product, Basket
from django.views import generic
from django.db.models import Q, base
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import requests
from decimal import Decimal


# Create your views here.
class HomePageView(generic.TemplateView):
    template_name = 'products/home.html'

    def get_context_data(self):
        response = requests.get('https://api.ratesapi.io/api/latest')
        bank = response.json()
        context = Product.objects.all()[:5]
        return {'recommend': context, 'USD': bank['rates']['USD'], 'date': bank['date'], 'GBP': bank['rates']['GBP']}


class ResultsView(generic.ListView):
    model = Product
    template_name = 'products/results.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('res')
        result = Product.objects.filter(
            Q(pr_title__icontains=query) | Q(pr_description__icontains=query) | Q(pr_description__icontains=query))
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
            return redirect('products:home')
    else:
        form = UserCreationForm()
    return render(request, 'products/signup.html', {'form': form})


class ProductView(generic.TemplateView):
    model = Product
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        response = requests.get('https://api.ratesapi.io/api/latest')
        bank = response.json()
        context = get_object_or_404(Product, pk=self.kwargs['pr_id'])
        course = Decimal(self.kwargs['course'])
        return {'product': context,'USD': bank['rates']['USD'], 'GBP': bank['rates']['GBP'], 'course':course}


class CheckoutView(generic.TemplateView):
    model = Basket
    template_name = 'products/basket.html'
    def get_context_data(self, **kwargs):
        response = requests.get('https://api.ratesapi.io/api/latest')
        bank = response.json()
        context = Basket.objects.filter(user=self.kwargs['user_id'], inbasket=True)
        total = 0
        course = Decimal(self.kwargs['course'])
        for item in context:
            total += item.num * item.prod.pr_price
        return {'basket': context, 'total': total, 'course': course,'USD': bank['rates']['USD'],
                'GBP': bank['rates']['GBP'],}


@login_required
def addbin(request, pr_id):
    user = request.user
    course = 1
    product = Product.objects.get(pk=pr_id)
    try:
        cart = Basket.objects.get(prod=product, user=user, inbasket=True)
    except Basket.DoesNotExist:
        cart = Basket.objects.create(prod=product, user=user)
        cart.save()
        return HttpResponseRedirect(reverse('products:checkout', args=(user.id,course)))
    else:
        cart.num += 1
        cart.save()
        return HttpResponseRedirect(reverse('products:checkout', args=(user.id,course)))


def buy(request, user_id):
    checked = Basket.objects.filter(user=user_id)
    for item in checked:
        item.inbasket = False
        item.save()
    return HttpResponseRedirect(reverse('products:home'))


def delete(request, pr_id):
    user = request.user
    product = Product.objects.get(pk=pr_id)
    checked = Basket.objects.get(user=user.id, prod=product, inbasket=True)
    checked.delete()
    course = 1
    return HttpResponseRedirect(reverse('products:checkout', args=(user.id,course)))


class HistoryView(generic.TemplateView):
    model = Basket
    template_name = 'products/history.html'

    def get_context_data(self, **kwargs):
        context = Basket.objects.filter(user=self.kwargs['user_id'], inbasket=False)
        return {'history': context}



