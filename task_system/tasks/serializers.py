
from tasks.models import Comment, Task
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'task']

class TaskSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields =['id','title','description','status','user', 'comments']

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





