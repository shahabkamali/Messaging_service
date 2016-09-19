from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField
import os


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
    filename = "%s.%s" % (instance.pk, ext)
    return os.path.join('map/picture', filename)


class Map(models.Model):
    mapname = models.CharField(max_length=100)
    floor = models.ForeignKey(Floor)
    picture = models.ImageField(upload_to=content_file_name)
    markers = JSONField(blank=True, null=True)

