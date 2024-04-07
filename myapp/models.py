from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django.utils import timezone

import datetime


class Chat(Model):
    poster = models.PositiveBigIntegerField(default=0)
    reply = models.PositiveBigIntegerField(default=0)
    when = models.DateTimeField()
    text = models.CharField()
    post_type = models.CharField(max_length=10)
    us_id = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    
    
class Book(Model):
    name = models.CharField(max_length=100) 
    price = models.IntegerField(default=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Accounts(Model):
   name = models.CharField(max_length=300)
   surn = models.CharField(max_length=300)
   day = models.IntegerField(default=0)
   month = models.IntegerField(default=0)
   year = models.IntegerField(default=0)
   level = models.IntegerField(default=0)
   when = models.DateTimeField(auto_now=True)
   picurl = models.CharField(max_length=300, default='nope')
   #uid = models.PositiveBigIntegerField()
   uid = models.ForeignKey(User, on_delete=models.CASCADE, default=0)








class Photos(Model):
   Title = models.CharField(max_length=300)
   Desc = models.CharField(max_length=300)
   when = models.DateTimeField(auto_now=True)
   picurl = models.CharField(max_length=3000, default='nope')
   uid = models.ForeignKey(User, on_delete=models.CASCADE, default=0)


class Gallery_category(Model):
   Name = models.CharField(max_length=300)
   Desc = models.CharField(max_length=300)
   when = models.DateTimeField(auto_now=True)
   picurl = models.CharField(max_length=3000, default='nope')
   uid = models.ForeignKey(User, on_delete=models.CASCADE, default=0)


class Gallery_comments(Model):
   Text = models.CharField(max_length=300)
   Desc = models.IntegerField(null=True)
   when = models.DateTimeField(default=timezone.now)
   Author = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
   Photo_id = models.ForeignKey(Gallery_category, on_delete=models.CASCADE, default=0)
