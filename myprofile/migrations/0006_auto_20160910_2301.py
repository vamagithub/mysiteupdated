# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-10 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0005_auto_20160610_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thing',
            name='email',
        ),
        migrations.AlterField(
            model_name='thing',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
