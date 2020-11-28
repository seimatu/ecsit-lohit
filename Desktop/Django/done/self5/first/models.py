from django.db import models

# Create your models here.
class AllInfo(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    adress=models.CharField(max_length=30)
    Email=models.EmailField()

def __str__(self):
    return self.name

