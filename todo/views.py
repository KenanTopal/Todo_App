from django.shortcuts import render, HttpResponse
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def home(request):
  return HttpResponse("<h1> Welcome to Todo API</h1>")

@api_view(["GET"])
def TodoList(request):
  queryset = Todo.objects.all()
  serializer = TodoSerializer(queryset, many = True)
  return Response(serializer.data)

@api_view(["POST"])
def todo_add(request):
  serializer = TodoSerializer(data = request.data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)

  return Response(serializer.errors)

@api_view(["GET", "POST"])
def todo_list_add(request):
  if request.method == "GET":
    queryset = Todo.objects.all()
    serializer = TodoSerializer(queryset, many = True)
    return Response(serializer.data)
  
  elif request.method == "POST":
    serializer = TodoSerializer(data = request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

    return Response(serializer.errors)