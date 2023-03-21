from rest_framework.serializers import ModelSerializer

from todoapp.models import Task


class ToDoSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('owner',)
