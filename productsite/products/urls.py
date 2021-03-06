from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'products'
urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('results/', views.ResultsView.as_view(), name = 'results'),
    url(r'^signup/$', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='products/login.html'), name="login"),
    path('<pr_id>/<course>', views.ProductView.as_view(), name='details'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('<pr_id>/add/', views.addbin, name = 'add'),
    path('<pr_id>/delete/', views.delete, name = 'del'),
    path('checkout/<user_id>/<course>/', views.CheckoutView.as_view(), name = 'checkout'),
    path('buy/<user_id>/', views.buy, name = 'buy'),
    path('history/<user_id>/', views.HistoryView.as_view(), name = 'history'),
]
