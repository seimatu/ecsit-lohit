from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from .forms import signupForm
from django.views.generic import ListView
from app.models import Product,Category
# Create your views here.


class index(ListView):
    model=Product
    templates_name='app/product_list.html'


def signup(request):
    if request.method=='POST':
        form=signupForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('index')
    else:
            form=signupForm()
    return render(request,'app/signup.html',{'form':form})