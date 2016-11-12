from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from jsonfield import JSONField
import os
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver




class Building(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Floor(models.Model):
    name = models.CharField(max_length=100)
    building = models.ForeignKey(Building)

    def __unicode__(self):
        return self.name + "--building: " + self.building.name


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    print 'inctance', type(instance)
    filename = "%s.%s" % (instance.mapname, ext)
    return os.path.join('map/picture', filename)


class Map(models.Model):
    mapname = models.CharField(max_length=100,unique=True)
    floor = models.ForeignKey(Floor)
    picture = models.FileField(upload_to=content_file_name)
    markers = JSONField(blank=True, null=True)


@receiver(pre_delete, sender=Map)
def map_delete(sender, instance, **kwargs):
     if instance.picture:
        try:
            if os.path.isfile(instance.picture.path):
                os.remove(instance.picture.path)
        except:
            pass


@receiver(models.signals.pre_save, sender=Map)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = Map.objects.get(pk=instance.pk).picture
    except Map.DoesNotExist:
        return False

    new_file = instance.picture
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
