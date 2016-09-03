from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='users/static/picture')

