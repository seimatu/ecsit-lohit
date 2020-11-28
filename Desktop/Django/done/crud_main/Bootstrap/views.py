from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def bootstrap(request):
    return render(request,'bootstrap.html')

