from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('results/', views.ResultsView.as_view(), name = 'results'),
]
