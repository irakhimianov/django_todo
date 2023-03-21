from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from .views import TaskDetailAPIView, TaskListAPIView

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('redoc/', SpectacularRedocView.as_view(), name='redoc'),
    path('swagger/', SpectacularSwaggerView.as_view(), name='swagger'),
    path('tasks/', TaskListAPIView.as_view()),
    path('task_detail/<uuid:pk>/', TaskDetailAPIView.as_view()),
]
