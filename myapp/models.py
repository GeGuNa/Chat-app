from django.db import models
from django.db.models import Model
import datetime


class Chat(Model):
    poster = models.PositiveBigIntegerField(default=0)
    reply = models.PositiveBigIntegerField(default=0)
    when = models.DateTimeField()
    text = models.CharField()
    post_type = models.CharField(max_length=10)
    
    
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
   uid = models.PositiveBigIntegerField()
