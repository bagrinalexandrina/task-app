from drf_util.decorators import serialize_decorator
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from tasks.models import Task
from rest_framework.generics import GenericAPIView
from tasks.serializers import TaskSerializer

from rest_framework import permissions

class TaskListView(GenericAPIView):
    serializer_class = TaskSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    @serialize_decorator(TaskSerializer)
    def post(self, request):
        validated_data=request.serializer.validated_data

        task = Task.objects.create(
            user=request.user,
            title = validated_data['title'],
            description = validated_data['description']
        )
        

        return Response(TaskSerializer(task).data)
    


