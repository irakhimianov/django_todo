from django.urls import path

from .views import (TaskCreateView, TaskDetailView, TaskListView,
                    TaskUpdateView, TaskDeleteView)

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('<uuid:pk>/', TaskDetailView.as_view(), name='task'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('update/<uuid:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('delete/<uuid:pk>/', TaskDeleteView.as_view(), name='task_delete'),
]
