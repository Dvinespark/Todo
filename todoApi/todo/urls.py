from django.urls import path, include
from .views import *
from .viewsets import *
app_name = "todo"
router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('api-todo/', include(router.urls)),
    path('api/todo', TodoListView.as_view()),
    path('api/todo/<int:pk>', TodoDetailView.as_view())
]