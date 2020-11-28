from django.shortcuts import render
from django.http import HttpResponse

def common(request):
    return HttpResponse('How are you')

# Create your views here.
