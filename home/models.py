# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import connection

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=122)
    message = models.TextField()

    def __str__(self):
        return self.name

class Ourteams:
    id = int
    name = str
    designation = str
    img = str

class teams(models.Model):
    name = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    designation = models.CharField(max_length=122)
    img = models.ImageField(upload_to='uploaded_imgs')
    status = models.IntegerField(default=1)
    is_deleted = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class teamcrud(models.Model):
    name = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    designation = models.CharField(max_length=122)
    img = models.ImageField(upload_to='uploaded_imgs')
    status = models.IntegerField(default=1)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table='home_teams'        
    

class my_custom_sql(models.Model):
    class Meta:
        teamcrud('SELECT * FROM home_teams')


        

    
