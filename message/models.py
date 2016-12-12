from __future__ import unicode_literals
from django.core.validators import MaxValueValidator,MinValueValidator
from jsonfield import JSONField

from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=60, unique=True)
    text = models.TextField()
    x = models.IntegerField(default=0);
    y = models.IntegerField(default=0);
    r = models.SmallIntegerField(validators=[ MinValueValidator(0),MaxValueValidator(255),])
    g = models.SmallIntegerField(validators=[ MinValueValidator(0),MaxValueValidator(255),])
    b = models.SmallIntegerField(validators=[ MinValueValidator(0),MaxValueValidator(255),])
    brightness = models.SmallIntegerField(default=100,validators=[ MinValueValidator(0),MaxValueValidator(100),])
    showtime = models.SmallIntegerField(default=10, help_text="test",validators=[ MinValueValidator(0),MaxValueValidator(100),])
    Static = 0
    Scroll = 1
    EFFECT_CHOICES = (
        (Static, "Static"),
        (Scroll, "Scroll"),
    )
    effect = models.IntegerField(
        choices=EFFECT_CHOICES,
        default=Static,
    )
    F1 = '4x6';F2 = '5x7';F3 = '5x8';F4 = '6x10';F5 = '6x12';    F6 = '6x13';   F7 = '6x13B';    F8 = '6x13O';
    F9 = '6x9';    F10 = '7x13';    F11 = '7x13B';    F12 = '7x13O';    F13 = '7x14';    F14 = '7x14B';
    F15 = '8x13';    F16 = '8x13B';    F17 = '8x13O';    F18 = '9x15';    F19 = '9x15B';    F20 = '9x18';
    F21 = '9x18B';    F22 = '10x20'
    fonts = (
        (F1, '4x6'), (F2, '5x7'), (F3, '5x8'), (F4, '6x10'),
        (F5, '6x12'), (F6, '6x13'), (F7, '6x13B'), (F8, '6x13O'),
        (F9, '6x9'), (F10, '7x13'), (F11, '7x13B'), (F12, '7x13O'),
        (F13, '7x14'), (F14, '7x14B'), (F15, '8x13'), (F16, '8x13B'),
        (F17, '8x13O'), (F18, '9x15'), (F19, '9x15B'), (F20, '9x18'),
        (F21, '9x18B'), (F22, '10x20'),
    )
    font = models.CharField(max_length=20, choices=fonts, default=F1)


class SavedMessage(models.Model):
    name = models.CharField(max_length=60, unique=True)
    jsonlist = JSONField(blank=True, null=True)
