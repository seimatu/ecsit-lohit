from django.db import models

# Create your models here.

class AllInfo(models.Model):
    name=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    profession=models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    salary=models.DecimalField(max_digits=10,decimal_places=2)


def __str__(self):
    return self.name
