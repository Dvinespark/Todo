from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .serializers import TodoCustomSerializer
from .models import Todo
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.views import Response

# Create your views here.


def home(request):
    return HttpResponse("API is working...")


class TodoListView(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print("This is executed at first")
        return super().dispatch(request, *args, **kwargs)

    # return all Todo objects
    def get(self, request):
        print(request)
        if 'is_complete' in request.GET.keys():
            filter_by = request.GET.get('is_complete')
            todos = Todo.objects.filter(is_complete=filter_by)
        else:
            todos = Todo.objects.all()
        serializer = TodoCustomSerializer(todos, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    # create new object
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = TodoCustomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class TodoDetailView(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return HttpResponse("Object does not exists", status=404)

    def get(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoCustomSerializer(todo)
        return JsonResponse(serializer.data, safe=True)

    # delete object
    def delete(self, request, pk):
        todo = self.get_object(pk)
        todo.delete()
        return HttpResponse(status=200)

    # update object
    def put(self, request, pk):
        todo = self.get_object(pk=pk)
        serializer = TodoCustomSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=204)
