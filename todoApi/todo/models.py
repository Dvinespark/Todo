from .mixins import *
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    photo = models.ImageField(upload_to='media', blank=True)


class Todo(TodoMixins):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    short_description = models.TextField(blank=False)
    long_description = models.TextField()
    allocated_time = models.CharField(max_length=200, blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.short_description
