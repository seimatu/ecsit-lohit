from django.shortcuts import render
from django.shortcuts import redirect
from . forms import AllInfoForm
# Create your views here.
from . models import AllInfo


def fixed(request):
    return render(request,'home.html')

def call(request):
    all_list=AllInfo.objects.all
    return render(request,'about.html',{'all_list':all_list})

def create_info(request):
    form=AllInfoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(call)
    return render(request,'info_form.html',{'form':form})

def update_info(request,id):
    all_items=AllInfo.objects.get(id=id)
    form=AllInfoForm(request.POST or None,instance=all_items)

    if form.is_valid():
        form.save()
        return redirect(call)

    return render(request,'info_form.html',{'form':form,'all_items':all_items})

def delete_info(request,id):
    delete_info=AllInfo.objects.get(id=id)

    if request.method=='POST':
        delete_info.delete()
        return redirect(call)

    return render(request,'info_delete.html',{'delete_info':delete_info})