# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class teamMembers():
    name = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    designation = models.CharField(max_length=122)
    img = models.ImageField(upload_to='uploaded_imgs')
    status = models.IntegerField(default=1)
    is_deleted = models.IntegerField(default=0)
    is_working = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class stockSellerProductsModel(models.Model):
    id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=200)
    seller_name = models.CharField(max_length=200)



    