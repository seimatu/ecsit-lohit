from django.shortcuts import render
from django.shortcuts import redirect

from .models import AllInfo
from .forms import AllInfoForm

# Create your views here.
def free(request):
    return render(request,'name.html')
    

def home(request):
    all_list=AllInfo.objects.all()
    return render(request,'home.html',{'all_list':all_list})

def create_info(request):
    form=AllInfoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(home)
    return render(request,'deta.html',{'form':form})

