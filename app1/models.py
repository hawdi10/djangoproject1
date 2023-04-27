from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=8)
    lname=models.CharField(max_length=8)
    img=models.ImageField()
    age=models.IntegerField()
    date=models.DateField()