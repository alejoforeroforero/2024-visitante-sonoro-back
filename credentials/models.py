from django.contrib.auth.models import AbstractUser
from django.db import models
from recordings.models import Record


class CustomUser(AbstractUser):
    google_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    google_picture = models.URLField(max_length=500, null=True, blank=True)
    profile_picture = models.ImageField(
            upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    favorite_records = models.ManyToManyField(Record, related_name='favorited_by')


    def __str__(self):
        return self.username