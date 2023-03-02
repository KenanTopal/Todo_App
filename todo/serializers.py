from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = "__all__"
    # fields = ("id", "task", "description", "priority", "done")
    # exclude = ("createDate", "updateDate")