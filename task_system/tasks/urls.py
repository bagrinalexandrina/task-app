from django.urls import path
from tasks.views import  TaskDetailView, TaskListView




urlpatterns = [
    path('task/', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]