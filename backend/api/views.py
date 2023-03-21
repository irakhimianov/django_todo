from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from todoapp.models import Task
from .permissions import IsOwner
from .serializers import ToDoSerializer


class TaskListAPIView(ListCreateAPIView):
    serializer_class = ToDoSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)


class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    permission_classes = (IsOwner,)
    lookup_field = 'pk'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
