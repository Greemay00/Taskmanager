from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Показываем только задачи текущего пользователя
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # При создании задачи автоматически задаём владельца
        serializer.save(owner=self.request.user)

# Django HTML-шаблонный view
@login_required
def task_list_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title, owner=request.user)
        return redirect('task_list')

    tasks = Task.objects.filter(owner=request.user)
    return render(request, 'tasks/index.html', {'tasks': tasks})
@login_required
def task_complete_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)
    if request.method == 'POST':
        task.completed = True
        task.save()
    return redirect('task_list')

@login_required
def task_delete_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)
    if request.method == 'POST':
        task.delete()
    return redirect('task_list')