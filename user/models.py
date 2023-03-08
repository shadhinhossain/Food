from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved=models.BooleanField(default=True)


    def __str__(self):
        return self.name



class Menu(models.Model):
    name = models.CharField(max_length=55)
    image= models.ImageField(upload_to='default')
    details = models.TextField(blank=True)
    price = models.FloatField()
    is_available=models.BooleanField(default=True)
    added_on= models.DateTimeField(auto_now_add=True)
    updated_on =models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = models.ImageField(upload_to='default')
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __int__(self):
        return self.id


class Chef(models.Model):
    name = models.CharField(max_length=55)
    image = models.ImageField(upload_to='default')
    details = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name