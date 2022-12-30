from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class RegisterDoctor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=25, verbose_name="Username", unique=True)
    email = models.EmailField(verbose_name="Email")
    password = models.CharField(max_length=200, verbose_name="Password")
    name = models.CharField(max_length=25, verbose_name="Name")
    surname = models.CharField(max_length=25, verbose_name="Surname")
    phone_number = models.CharField(max_length=11, verbose_name="Phone Number")
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, verbose_name="Gender")
    department = models.CharField(max_length=20, verbose_name="Department")
    degree = models.CharField(max_length=20, verbose_name="Degree")
    status = models.CharField(max_length=15)
    
    def __str__(self):
        return f'{self.username}'


class DoctorLogin(models.Model):
    email = models.EmailField(verbose_name = "Email",blank=True)
    password = models.CharField(max_length=200,verbose_name = "Password", blank=True)