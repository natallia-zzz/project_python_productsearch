from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.home, name='home'),
    path('results/', views.results, name = 'results'),
]
