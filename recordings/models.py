from django.db import models
from django.utils import timezone
from .validators import validate_audio_file
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError(_('The Email field must be set'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
        
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True.'))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True.'))
#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(_('email address'), unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email

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
    

