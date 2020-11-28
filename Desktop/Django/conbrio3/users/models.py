from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser 
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    """カスタムユーザーマネージャー"""
    use_in_migrations = True

    def _create_user(self, sirname, email, password, **extra_fields): # email を必須にする
        if not sirname:
            raise ValueError('メールアドレスが入力されていません。')
        if not email:
            raise ValueError('メールアドレスが入力されていません。')

        email = self.normalize_email(email)
        sirname = self.models.sirname(sirname)
        user = self.model(sirname=sirname,email=email,**extra_fields)
        user.set_password(password)
        user.save(self.db)
        
        return user

    def create_user(self,sirname ,email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(sirname, email, password,**extra_fields)
    
    def create_superuser(self,sirname ,email, password,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(sirname, email, password, **extra_fields)


# User モデルより上に記載する

class User(AbstractBaseUser, PermissionsMixin): 
    """カスタムユーザーモデル"""
    sirname = models.CharField(max_length=100)
    email = models.EmailField("メールアドレス", unique=True)
    name = models.CharField(max_length=30, blank=True,)
    is_staff = models.BooleanField("is_staff", default=False)
    is_active = models.BooleanField("is_active", default=True)
    date_joined = models.DateTimeField("date_joined",default=timezone.now)

    objects = UserManager()


    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['sirname']


    class Meta:
        verbose_name = "user" 
        verbose_name_plural = "users"