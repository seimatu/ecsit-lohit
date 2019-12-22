from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from products.models import Product


class Home(ListView):
    model=Product
    templates_name='products/product_list.html'