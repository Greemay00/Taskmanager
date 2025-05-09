# tasks/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from . import views

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')  
# пустой префикс, потому что префикс "tasks" уже в главном urls.py

urlpatterns = [
    path('', views.task_list_view, name='task_list'),
    path('complete/<int:task_id>/', views.task_complete_view, name='task_complete'),
    path('delete/<int:task_id>/', views.task_delete_view, name='task_delete'),
]
