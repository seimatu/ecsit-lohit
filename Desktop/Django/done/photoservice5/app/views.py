from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import PhotoForm
from .models import Photo,Category


# Create your views here.
def index(request):
    photos=Photo.objects.all().order_by('-created_at')
    return render(request,'app/index.html',{'photos':photos})

def users_detail(request,pk):
    user=get_object_or_404(User,pk=pk)
    photos=user.photo_set.all().order_by('-created_at')
    return render(request,'app/users_detail.html',{'user':user,'photos':photos})

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)#Userインスタンスを作成。
        if form.is_valid():#生成されたインスタンスが正しい値を持っているかチェック。
            new_user=form.save()#新しいユーザーインスタンスを保存。
            input_username=form.cleaned_data['username']
            input_password=form.cleaned_data['password']
            #フォームの入力値で認証出来ればユーザーオブジェクト、出来なければNoneを返す。
            new_user=authenticate(username=input_username, password=input_password)
            #認証成功時のみ、ユーザーをログインさせる
            if new_user is not None:
                #loginメソッドは、認証が出来ていなくてもログインさせることができる。（上のauthenticateで認証を実行する）
                login(request,new_user)
                return redirect('app:users_detail',pk=new_user.pk)
    else:
        form=UserCreationForm()
    return render(request,'app/signup.html',{'form':form})

@login_required
def photos_new(request):
    if request.method=='POST':
        form=PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            photo=form.save(commit=False)
            photo.user=request.user
            photo.save()
            messages.success(request,"completad post")
        return redirect('app:users_detail',pk=request.user.pk)
    else:
        form=PhotoForm()
    return render(request,'app/photos_new.html',{'form':form})

def photos_detail(request,pk):
    photo=get_object_or_404(Photo,pk=pk)
    return render(request,'app/photos_detail.html',{'photo':photo})

@require_POST
def photos_delete(request,pk):
    photo=get_object_or_404(Photo,pk=pk)
    photo.delete()
    return redirect('app:users_detail',request.user.id)

def photos_category(request,category):
    #titleがURLの文字列と一致するCategoryインスタンスを取得
    category=Category.objects.get(title=category)
    #取得したCategoryに属するPhoto一覧を取得
    photos=Photo.objects.filter(category=category).order_by('-created_at')

    return render(request,'app/index.html',{'photos':photos,'category':category})