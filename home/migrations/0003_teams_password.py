# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-10 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_teams'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='password',
            field=models.CharField(default=0, max_length=122),
            preserve_default=False,
        ),
    ]
