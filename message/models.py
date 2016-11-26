from __future__ import unicode_literals
from django.core.validators import MaxValueValidator,MinValueValidator

from django.db import models

class Message(models.Model):
    text = models.TextField()
    x = models.IntegerField();
    y = models.IntegerField();
    r = models.SmallIntegerField(validators=[ MinValueValidator(0),MaxValueValidator(255),])
    g = models.SmallIntegerField(validators=[ MinValueValidator(0),MaxValueValidator(255),])
    b = models.SmallIntegerField(validators=[ MinValueValidator(0),MaxValueValidator(255),])
    brightness =models.SmallIntegerField(validators=[ MinValueValidator(0),MaxValueValidator(100),])
    showtime = models.SmallIntegerField(validators=[ MinValueValidator(0),MaxValueValidator(100),])
    Static = 0
    Scroll = 1
    EFFECT_CHOICES = (
        (Static, 0),
        (Scroll, 1),
    )
    effect = models.IntegerField(
        choices=EFFECT_CHOICES,
        default=Static,
    )

