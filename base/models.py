from datetime import datetime
from hashlib import new
from django.conf import settings
from django.db import models
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    category_1 = 'Arbeit'
    category_2 = 'Studium'
    category_3 = 'Freizeit'
    category_4 = 'Haushalt'
    category_5 = 'others'
    category_6 = 'none'
    CHOICES = [
        (category_1, 'Arbeit'),
        (category_2, 'Studium'),
        (category_3, 'Freizeit'),
        (category_4 ,'Haushalt'),
        (category_5 ,'others'),
        (category_6 ,'none'),
    ] 
    user = models.ForeignKey( User, on_delete=models.CASCADE, null=True, blank=True)
    aufgabe = models.CharField(max_length=200)
    Beschreibung = models.CharField(max_length=250)
    #date = models.CharField(max_length=50)
    date = models.DateField() 
    #date = models.DateTimeField()
    #created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=8,choices=CHOICES,default=category_1)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.aufgabe

    class Meta:
        order_with_respect_to = 'user'


# Create your models here.
