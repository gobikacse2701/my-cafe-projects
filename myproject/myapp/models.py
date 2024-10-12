from django.db import models

# Create your models here.
# class register(models.Model):
#     name=models.CharField(max_length=50)
#     password=models.CharField(max_length=50)

class huge(models.Model):
    coname = models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    contact=models.IntegerField()
    cost=models.IntegerField()
    