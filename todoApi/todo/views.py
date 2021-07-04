from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .serializers import TodoCustomSerializer
from .models import Todo
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home(request):
    return HttpResponse("API is working...")


class TodoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print("This is executed at first")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = Todo.objects.all()
        serializer = TodoCustomSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = TodoCustomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

