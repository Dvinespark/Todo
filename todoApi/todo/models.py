from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.


class User(AbstractUser):
    pass


class Todo(models.Model):
    short_description = models.TextField(blank=False)
    long_description = models.TextField()
    allocated_time = models.TextField()
    created_date = models.DateTimeField(default=datetime.datetime.now())
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
