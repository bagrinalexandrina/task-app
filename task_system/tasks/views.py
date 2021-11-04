import re
from drf_util.decorators import serialize_decorator
from model_utils.fields import StatusField
from rest_framework.response import Response
from tasks.models import Task
from rest_framework.generics import GenericAPIView, get_object_or_404
from tasks.serializers import TaskListSerializer, TaskSerializer

from rest_framework import permissions

class TaskListView(GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        tasks = Task.objects.all()

        return Response(TaskListSerializer(tasks, many=True).data)

    @serialize_decorator(TaskSerializer)
    def post(self, request):
        validated_data=request.serializer.validated_data
        
        try:
            user = validated_data["user"]
        except KeyError:
            user = request.user
        
        tasks = Task.objects.create(
            user=user,
            title = validated_data['title'],
            description = validated_data['description']
        )
        

        return Response(TaskSerializer(tasks).data)
    
class TaskDetailView(GenericAPIView):

    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        task = get_object_or_404(Task.objects.filter(pk=pk))
        return Response(TaskSerializer(task).data)



class TaskStatusInProgressView(GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        task = get_object_or_404(Task.objects.filter(pk=pk))
        task.status = "in_progress"
        task.save()
        return Response(TaskSerializer(task).data)


class TaskStatusDoneView(GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        task = get_object_or_404(Task.objects.filter(pk=pk))
        task.status = "done"
        task.save()
        return Response(TaskSerializer(task).data)

       
