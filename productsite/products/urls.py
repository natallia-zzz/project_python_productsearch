from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('results/', views.ResultsView.as_view(), name = 'results'),
    url(r'^signup/$', views.signup, name='signup'),
]
