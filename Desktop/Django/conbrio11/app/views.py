from django.shortcuts import get_object_or_404,render,redirect
from django.contrib.auth.models import User
from .models import Category,Plan
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import PlanForm
from django.contrib import messages

# Create your views here.

class Index(ListView):
    model=Plan
    template_name='app/index.html'
# def index(request):
#     plans=Plan.objects.all().order_by('-created_at')
#     return render(request,'app/index.html',{'plans':plans})

def users_detail(request,pk):
    user=get_object_or_404(User,pk=pk)
    photos=user.plan_set.all().order_by('-created_at')
    return render(request,'app/users_detail.html',{'user':user,'photos':photos})

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            input_username=form.cleaned_data['username']
            input_password=form.cleaned_data['password1']
            # input_email=form.cleaned_data['email']
            new_user=authenticate(username=input_username,password=input_password)
            if new_user is not None:
                login(request,new_user)
                return redirect('mainapp:users_detail',pk=new_user.pk)
    else:
        form=UserCreationForm()
    return render(request,'app/signup.html', {'form':form})

@login_required
def plans_new(request):
    if request.method=='POST':
        form=PlanForm(request.POST,request.FILES)
        if form.is_valid():
            plan=form.save(commit=False)
            plan.user=request.user
            plan.save()
            messages.success(request,'投稿が完了しました')
        return redirect('app/users_detail',pk=request.user.pk)
    else:
        form=PlanForm()
    return render(request,'mainapp/plans_new.html' , {'form':form})

def plans_category(request,category):
    category=Category.objects.get(title=category)
    plans=Plan.objects.filter(category=category),order_by('-created_at')
    return render(request,'app/index.html',{'category':category,'plans':plans})

