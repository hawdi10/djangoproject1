from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=8,verbose_name="نام")
    lname=models.CharField(max_length=8,verbose_name="نام خانوادگی")
    code_melli=models.IntegerField(verbose_name="کد ملی")

    
    def __str__(self):
        return f'{self.name}'
