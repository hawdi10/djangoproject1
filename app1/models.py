from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=8,verbose_name="نام")
    lname=models.CharField(max_length=8,verbose_name="نام خانوادگی")
    img=models.ImageField(verbose_name="عکس")
    age=models.IntegerField(verbose_name="سن")
    date=models.DateField(verbose_name="عکس")