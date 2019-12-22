from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model
from products.models import Product


User=get_user_model()

class Cart(models.Model):
    user=models.CharField(max_length=100)
    item=models.ForeignKey(on_delete=models.CASCADE)
    quentity=models.PositiveIntegerField(default=0)
    created=models.DateTimeField(auto_now=True)
    
    def ___str__(self):
            return f'{self.quentity} of {self.item.name}'