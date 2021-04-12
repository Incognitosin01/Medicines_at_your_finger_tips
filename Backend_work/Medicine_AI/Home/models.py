from django.db import models,OperationalError
import os,sys


# Create your models here.

class Contact_us(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    topic = models.CharField(max_length=100)
    Issue = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class medicine(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class side_effect(models.Model):
    name = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.name