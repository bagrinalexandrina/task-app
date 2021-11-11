from django.urls import path
from tasks.views import  CommentsViewSet, DeleteTaskView, SearchTaskView, TaskDetailView, TaskListView, TaskStatusDoneView, TaskStatusInProgressView, UserAssignTaskView, UserCompletedTasksView, UserTasksView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'comments', CommentsViewSet, basename='comment')

urlpatterns = router.urls

urlpatterns += [
    path('task/', TaskListView.as_view(), name='tasks'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/in_progress/', TaskStatusInProgressView.as_view(), name='task_status_in_progress'),
    path('<int:pk>/done/', TaskStatusDoneView.as_view(), name='task_status_done'),
    path('current_user_tasks/', UserTasksView.as_view(), name='user_tasks'), #get all the task the logged user has
    path('logged_user/completed_tasks/', UserCompletedTasksView.as_view(), name='completed_tasks'),
    path('<int:pk>/assign/<int:user_id>/', UserAssignTaskView.as_view(), name='assigned_task'),
    path('task/<int:pk>/delete/',DeleteTaskView.as_view(),name='delete_task'),
    path('title_search/', SearchTaskView.as_view(), name='search_task')
]




