# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-04 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_auto_20161204_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]