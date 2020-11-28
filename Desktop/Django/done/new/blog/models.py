from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=40)
    description=models.TextField()
    technology=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images/',blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    