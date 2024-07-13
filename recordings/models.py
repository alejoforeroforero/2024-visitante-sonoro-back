from django.db import models
from django.utils import timezone
from .validators import validate_audio_file


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/authors', blank=True)
    slug = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/authors', blank=True)
    slug = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/authors', blank=True)
    slug = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Record(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    lugar = models.CharField(max_length=200, blank=True)
    recordingDate = models.DateTimeField()
    publishDate = models.DateTimeField(default=timezone.now)
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(upload_to='images/record', blank=True)
    audio = models.FileField(upload_to='audio/', blank=True,  validators=[validate_audio_file])
    category = models.ForeignKey(
        Category, related_name='recordings', on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(
        Author, related_name='recordings', on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='recordings', blank=True)

    def __str__(self):
        return self.title
    

