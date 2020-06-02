from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Basket
from django.views import generic
from django.db.models import Q
from django.contrib.auth import login, authenticate, mixins
from django.contrib.auth.forms import UserCreationForm
from . import search_algorithm_strict as test
from django.urls import reverse

# Create your views here.
class HomePageView(generic.TemplateView):
    template_name = 'products/home.html'
    # def get_context_data(self, **kwargs):
    # c = super().get_context_data(**kwargs)
    # user = self.request.user
    # return {'user':user}


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
        context = get_object_or_404(Product, pk=self.kwargs['pr_id'])
        return {'product': context}


class CheckoutView(mixins.LoginRequiredMixin, generic.TemplateView):
    model = Product
    redirect_field_name = 'products:home'
    template_name = 'products/basket.html'


def addbin(request, pr_id):
    product = get_object_or_404(Product, pk=pr_id)
    user = request.user
    num = request.POST['num']
    item = Basket.object.create(prod=product.pr_id, user=user.id, num=num)
    return HttpResponseRedirect(reverse('products:checkout', kwargs=(item,)))


