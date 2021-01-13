# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class companyMembers:
    name = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    designation = models.CharField(max_length=122)
    img = models.ImageField(upload_to='uploaded_imgs')

    def __str__(self):
        return self.name
    
