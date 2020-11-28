from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('My home')

def about(request):
    return HttpResponse('My name is sei')

def fixed(request):
    return render(request,'home.html')

def call(request):
    return render(request,'new/about.html')


# Create your views here.

