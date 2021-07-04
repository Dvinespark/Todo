from django.db import models


class TodoMixins(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mixin = models.CharField(max_length=100)

    class Meta:
        abstract = True
