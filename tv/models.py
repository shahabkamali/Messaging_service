from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=50, unique=True)
    showtime = models.SmallIntegerField(default=10,validators=[MinValueValidator(0), MaxValueValidator(100), ])
    context = models.TextField()


class SavedMessage(models.Model):
    name = models.CharField(max_length=60, unique=True)
    jsonlist = JSONField(blank=True, null=True)