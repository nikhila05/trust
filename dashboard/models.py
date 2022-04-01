import hashlib
from datetime import datetime

from django.db import models

CONTACTFROM = (
    ('Enterprise', 'Enterprise'),
    ('Contactus', 'Contactus'),
)


class City(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.name)


def img_url(self, filename):
    hash_ = hashlib.md5()
    hash_.update(
        str(filename).encode('utf-8') + str(datetime.now()).encode('utf-8'))
    file_hash = hash_.hexdigest()
    return "%s%s/%s" % (self.file_prepend, file_hash, filename)


class Image(models.Model):
    file_prepend = "gallery/"
    logo = models.FileField(upload_to=img_url)

    def __str__(self):
        return str(self.logo.name)


class News(models.Model):
    file_prepend = "news/"
    file = models.FileField(upload_to=img_url)
    name = models.CharField(max_length=1000)
    published_on = models.DateTimeField()
    is_video = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(default='')
    gallery = models.ManyToManyField(Image)
    location = models.ManyToManyField(City)
    is_public = models.BooleanField(default=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return str(self.title)
