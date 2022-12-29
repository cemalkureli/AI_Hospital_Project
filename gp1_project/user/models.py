from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Doctor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10)
    age=models.CharField(max_length=3)
    gender=models.CharField(max_length=10)
    Department=models.CharField(max_length=20)
    status=models.CharField(max_length=15)
    salary=models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.user.first_name}'