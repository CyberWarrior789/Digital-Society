from email.policy import default
from tkinter import CASCADE
from turtle import update
from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique= True) 
    password = models.CharField(max_length=20)
    otp = models.IntegerField(default = 9851)
    is_active = models.BooleanField(default=True)
    is_verfied = models.BooleanField(default=False)
    first_login = models.BooleanField(default=False) 
    role = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.email

class House(models.Model):
    houses_choise=(
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("7","7"),
    ("8","8"),
    ("9","9"),
    ("10","10"),
    )

    house_no = models.CharField(max_length=20,choices=houses_choise,default=1)
    status = models.CharField(max_length=50)
    detail = models.CharField(max_length=100)
    def __str__(self):
        return self.house_no

class Chairman(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    house_id = models.ForeignKey(House,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    locality = models.CharField(max_length=100)
    profile_pic = models.FileField(upload_to="media/images",default="media/default.png")

    def __str__(self):
        return self.firstname +" "+str(self.house_id.house_no)