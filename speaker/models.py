from __future__ import unicode_literals

from django.db import models
import os
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_delete
from jsonfield import JSONField

# Create your models here.


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.name, ext)
    return os.path.join(instance.directory_string_var, filename)


class Voice(models.Model):
    name = models.CharField(max_length=60, unique=True)
    filename = models.FileField(upload_to=content_file_name)
    directory_string_var = 'Speaker/voice/'


class SavedMessage(models.Model):
    name = models.CharField(max_length=60, unique=True)
    jsonlist = JSONField(blank=True, null=True)



@receiver(pre_delete, sender=Voice)
def userprofile_delete(sender, instance, **kwargs):
     if instance.filename:
        if os.path.isfile(instance.filename.path):
            os.remove(instance.filename.path)