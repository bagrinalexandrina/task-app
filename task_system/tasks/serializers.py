
from django.db.models import fields
from tasks.models import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields =['id','title','description','status']

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title']


