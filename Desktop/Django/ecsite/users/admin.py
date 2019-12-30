from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import User

class MyUserChangeFrom(UserChangeForm):
    #User情報を変更するフォーム
    class Meta:
        model=User
        fields='__all__'

class MyUserCreationForm(UserCreationForm):
    #Userを作成するフォーム
    class Meta:
        model=User
        fields=('email',)#emailとパスワードが必要

class MyUserAdmin(UserAdmin):
    #カスタムユーザーモデルのAdmin
    fieldsets=(
        (None,{'fields':('email','password','fav_products')}),
        (_('permissions'),{'fields':('is_active','is_staff','is_superuser','groups','user_parmissions')}),
        (_('Inportant datas'),{'fields':('last_login','date_joined')}),
    )
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2'),
        }),
    )
    form=MyUserChangeFrom
    add_form=MyUserCreationForm
    list_display=('email','is_staff')
    list_filter=('is_staff','is_superuser','is_active','groups')
    search_fields=('email',)
    ordering=('email',)

admin.site.register(User,MyUserAdmin)