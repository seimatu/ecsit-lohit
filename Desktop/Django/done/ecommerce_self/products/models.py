from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=200)
    PrimaryCategory=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Product(models.Model):
    mainimage=models.ImageField(upload_to='product/',blank=True)
    name=models.CharField(max_length=50)
    slug=models.SlugField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    preview_text=models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text=models.TextField(max_length=200, verbose_name='Detail Text')
    price=models.FloatField()

    def __str__(self):
        return self.name

class User(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    address1=models.CharField(max_length=100)
    address2=models.CharField(max_length=100)    
    email=models.EmailField()
    phonenumber=models.IntegerField()

    def __str__(self):
        return self.firstname
    

    