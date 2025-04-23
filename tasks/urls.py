from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskListCreateView, TaskDetailView
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'api', TaskViewSet, basename='task')

urlpatterns = [
    path('api/', TaskListCreateView.as_view(), name='task_list_create'),  
    path('api/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('', include(router.urls)),
]
