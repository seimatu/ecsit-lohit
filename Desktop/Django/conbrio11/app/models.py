from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):
        return self.title

    

class Plan(models.Model):
    mainimage=models.ImageField(upload_to='photos/',blank=True)
    title=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,default=1)
    created_at = models.DateTimeField(auto_now=True)
    meeting_place = models.CharField(max_length=200)
    moving_method = models.CharField(max_length=200)
    second_place = models.CharField(max_length=200)
    third_place = models.CharField(max_length=200)


    def __str__(self):
        return self.title