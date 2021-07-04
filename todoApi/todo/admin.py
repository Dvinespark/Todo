from django.contrib import admin
from django.apps import apps
from .models import User, Todo
# Register your models here.

# admin.site.register(User)
# admin.site.register(Todo)
app_models = apps.get_app_config('todo').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
