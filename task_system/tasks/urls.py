from django.urls import path
from tasks.views import  TaskDetailView, TaskListView, TaskStatusDoneView, TaskStatusInProgressView, UserCompletedTasksView, UserTasksView




urlpatterns = [
    path('task/', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/in_progress', TaskStatusInProgressView.as_view(), name='task_status_in_progress'),
    path('task/<int:pk>/done', TaskStatusDoneView.as_view(), name='task_status_done'),
    path('user/', UserTasksView.as_view(), name='user_tasks'),
    path('user/completed_tasks', UserCompletedTasksView.as_view(), name='completed_tasks'),


]