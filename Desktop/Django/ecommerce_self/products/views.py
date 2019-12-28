from django.shortcuts import render,get_object_or_404,redirect
# Create your views here.
from django.views.generic import ListView,DetailView,FormView
from products.models import Product
from .forms import checkout

class Home(ListView):
    model=Product
    templates_name='products/home.html'

class check(FormView):
    form_class=checkout
    template_name='products/checkout.html'



# def Detail(request,slug):
#     product_detail=Product.objects.get(slug=slug)
#     context={
#         # item:item,
#         slug:slug,
#     }
#     return render(request,'products/detail.html',context)

from django.contrib.auth.mixins import LoginRequiredMixin

class ProductDetail(LoginRequiredMixin,DetailView):
    model=Product

