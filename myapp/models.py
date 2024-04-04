from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

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
