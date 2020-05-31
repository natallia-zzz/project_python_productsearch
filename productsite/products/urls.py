from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView

app_name = 'products'
urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('results/', views.ResultsView.as_view(), name = 'results'),
    url(r'^signup/$', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='products/login.html'), name="login"),
]
