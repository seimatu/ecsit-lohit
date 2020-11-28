from django.db import models

# Create your models here.


class Category(models.Model):
    title=models.CharField(max_length=100)
    primaryCategory=models.BooleanField(default=False)
     
    def __str__(self):
        return self.title


class Product(models.Model):
    mainimage=models.ImageField(upload_to='photos/',blank=True)
    name=models.CharField(max_length=100)
    slug=models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    
    def __str__(self):
        return self.name