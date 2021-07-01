from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.


class User(AbstractUser):
    pass


class Todo(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    short_description = models.TextField(blank=False)
    long_description = models.TextField()
    allocated_time = models.TextField()
    created_date = models.DateTimeField(default=datetime.datetime.now())
    created_by = models.ForeignKey(User)
    completed = models.BooleanField(default=False)
