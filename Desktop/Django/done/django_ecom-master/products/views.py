from django.shortcuts import render

# Create your views here.

from products.models import Product
from django.views.generic import ListView

class Home(ListView):
    model=Product
    template_name='products/home.html'