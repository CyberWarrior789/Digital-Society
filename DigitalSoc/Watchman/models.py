from django.db import models
from Chairman.models import *

# Create your models here.
class Watchman(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    id_proof = models.FileField(upload_to="media/documents",blank = True, null = True)
    profile_pic = models.FileField(upload_to="media/images",default="media/defaultm.png")
    status = models.CharField(max_length=50, default = "Pending")

    def __str__(self):
        return self.firstname

class Visitor(models.Model):
    house_id = models.ForeignKey(House,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique= True) 
    mobileno = models.CharField(max_length=30)
    reason = models.CharField(max_length=200, default = "Casual")
    visited_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname