from django.urls import path
from .views import home, TodoList, todo_add, todo_list_add

urlpatterns = [
  path('', todo_list_add),
  path('list/', TodoList),
  path('add/', todo_add)
]