from tabnanny import verbose
from django.db import models
from Chairman.models import *
from django.utils import timezone
import math

# Create your models here.
class Member(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    house_id = models.ForeignKey(House,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    mobileno = models.CharField(max_length=30)
    job_specification = models.CharField(max_length=50)
    job_address = models.TextField(max_length=500)
    birthdate = models.CharField(max_length=20)
    no_of_members = models.CharField(max_length=30)
    marrital_status = models.CharField(max_length=30)
    locality = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100,default="Indian")
    gender = models.CharField(max_length=20,default="Male")
    no_of_vehicles = models.CharField(max_length=50,null=True,blank=True)
    vehicle_type = models.CharField(max_length=100)
    id_proof = models.FileField(upload_to="media/documents",default="media/default.png")
    profile_pic = models.FileField(upload_to="media/images",default="media/default.png")
    def __str__(self):
        return self.firstname +" "+str(self.house_id.house_no)

class Family_member(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    mobileno = models.CharField(max_length=30)
    job_specification = models.CharField(max_length=50)
    job_address = models.TextField(max_length=500)
    birthdate = models.CharField(max_length=20)
    locality = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100,default="Indian")
    gender = models.CharField(max_length=20,default="Male")
    relation = models.CharField(max_length=20)
    profile_pic = models.FileField(upload_to="media/images",default="media/default.png")
    def __str__(self):
        return self.firstname +" "+self.member_id.firstname

class Notice(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=1000)
    pic = models.FileField(upload_to="media/images/", null=True, blank=True)
    video = models.FileField(upload_to="media/videos/", null = True, verbose_name ="video")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    def __str__(self):
        return self.title
        
    def whenpublished(self):
        now = timezone.now()

        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"

            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"

            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days

            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)


            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"




class Event(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=1000)
    pic = models.FileField(upload_to="media/images/", null=True, blank=True)
    video = models.FileField(upload_to="media/videos/", null = True, blank = True, verbose_name ="video")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    def __str__(self):
        return self.title

    def whenpublished(self):
        now = timezone.now()

        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"

            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"

            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days

            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)


            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"


class Complain(models.Model):
    member_id = models.ForeignKey(Member,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=1000)
    pic = models.FileField(upload_to="media/images/",null=True, blank=True)
    video = models.FileField(upload_to="media/videos/", null = True,blank = True ,verbose_name ="video")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    def __str__(self):
        return self.title