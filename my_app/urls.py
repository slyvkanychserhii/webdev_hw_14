from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    TaskListCreateView, TaskRetrieveUpdateDestroyView, TaskStatisticsView,
    SubTaskListCreateView, SubTaskRetrieveUpdateDestroyView
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>', TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),
    path('tasks/statistics/', TaskStatisticsView.as_view(), name='task-statistics'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>', SubTaskRetrieveUpdateDestroyView.as_view(), name='subtask-retrieve-update-destroy'),
    path('', include(router.urls)),
]