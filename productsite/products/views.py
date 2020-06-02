from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Basket
from django.views import generic
from django.db.models import Q
from django.contrib.auth import login, authenticate, mixins
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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

# @login_required
def addbin(request, pr_id):
    product = Product.objects.get(pk=pr_id)
    user = request.user
    cart = Basket.objects.create( prod = product, user=user)
    cart.save()
    return redirect('products:checkout')


class ProductView(generic.TemplateView):
    model = Product
    template_name = 'products/detail.html'
    def get_context_data(self, **kwargs):
        context = get_object_or_404(Product, pk=self.kwargs['pr_id'])
        return {'product': context}
# def add_to_cart(request,book_id):
#     if request.user.is_authenticated():
#         try:
#             book = Book.objects.get(pk=book_id)
#         except c
#             pass
#         else :
#             try:
#                 cart = Cart.objects.get(user = request.user, active = True)
#             except ObjectDoesNotExist:
#                 cart = Cart.objects.create(user = request.user)
#                 cart.save()
#             cart.add_to_cart(book_id)
#         return redirect('cart')
#     else:
#         return redirect('index')