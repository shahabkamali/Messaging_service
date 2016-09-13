from __future__ import unicode_literals
from django.contrib.auth.models import User
import os
from django.db import models
from PIL import Image as Img
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from mainserver.settings import BASE_DIR


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.user.username, ext)
    return os.path.join('users/static/users/picture/', filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    picture = models.ImageField(upload_to=content_file_name, blank=True, null=True)

    def delete(self, *args, **kwargs):
        self.user.delete()
        pth = os.path.join(BASE_DIR + '/users/static/users/picture/', self.user.username + '.jpg')
        if os.path.isfile(pth):
            os.remove(pth)
        else:
            return
        return super(self.__class__, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.picture:
            image = Img.open(StringIO.StringIO(self.picture.read()))
            image.thumbnail((300,400), Img.ANTIALIAS)
            output = StringIO.StringIO()
            image.save(output, format='JPEG', quality=75)
            output.seek(0)
            self.picture = InMemoryUploadedFile(output,'ImageField', "%s.jpg" % self.picture.name, 'image/jpeg', output.len, None)
        super(UserProfile, self).save(*args, **kwargs)


