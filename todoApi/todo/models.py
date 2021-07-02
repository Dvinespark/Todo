from .mixins import *
# Create your models here.


class User(AbstractUserMixin):
    photo = models.ImageField(upload_to='media', blank=True)


class Todo(TodoMixins):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    short_description = models.TextField(blank=False)
    long_description = models.TextField()
    allocated_time = models.CharField(max_length=200, blank=True)
    is_complete = models.BooleanField(default=False)
