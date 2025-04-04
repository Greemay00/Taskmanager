from django.urls import path, include
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('api/', TaskListCreateView.as_view(), name='task_list_create'),  
    path('api/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]
