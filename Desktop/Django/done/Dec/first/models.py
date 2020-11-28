from django.db import models

# Create your models here.
class AllInfo(models.Model):
    name=models.CharField(max_length=20)
    adress=models.CharField(max_length=20)
    PhoneNumber=models.BigIntegerField()
    work=models.CharField(max_length=20)
    total_salary=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
    