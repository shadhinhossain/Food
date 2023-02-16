from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#==========contact model===============

class Contact(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    description = models.TextField()


    def __str__(self):
        return self.email

class Menu(models.Model):
    Name = models.name = models.CharField(max_length=55)
    