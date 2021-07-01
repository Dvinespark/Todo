from django.urls import path
from .views import home

app_name = "todo"

urlpatterns = [
    path('', home, name="home")
]