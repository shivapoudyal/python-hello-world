# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Contact
from models import teams


# Register your models here.
myModels = [Contact, teams]
admin.site.register(myModels)
