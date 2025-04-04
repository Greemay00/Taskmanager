from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# API для списка задач и создания новой задачи
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# API для просмотра, обновления и удаления задачи
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
