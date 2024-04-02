from django.db import models
import datetime


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100) 
    price = models.IntegerField(default=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
class BooBqk(models.Model):
    name = models.CharField(max_length=100) 
    price = models.IntegerField(default=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Accounts(models.Model):
   name = models.CharField(max_length=300)
   surn = models.CharField(max_length=300)
   day = models.IntegerField(default=0)
   month = models.IntegerField(default=0)
   year = models.IntegerField(default=0)
   level = models.IntegerField(default=0)
   when = models.DateTimeField(auto_now=True)
