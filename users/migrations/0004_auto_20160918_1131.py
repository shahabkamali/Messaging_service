# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-18 07:01
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160918_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='/static/dist/img/404_user.png', upload_to=users.models.content_file_name),
        ),
    ]
