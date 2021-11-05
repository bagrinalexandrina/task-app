
from django.db.models import fields
from users.serializers import UserSerializer
from tasks.models import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields =['id','title','description','status','user']

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title']

class UserTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [ 'id', 'title']

class UserCompletedTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'status']

class UserAssignTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','user']



