"""
URL configuration for taskmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# taskmanager/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    # админка
    path('admin/', admin.site.urls),

    # фронтенд-часть (HTML-шаблоны задач)
   path('api/', include('tasks.urls')),

    # Все API-эндпоинты начинаются с /api/
    # 1) Авторизация JWT
    path('api/token/',    TokenObtainPairView .as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 2) CRUD-API задач
    #    Сюда попадают маршруты из tasks/urls.py, например:
    #      GET  /api/tasks/       → список задач
    #      POST /api/tasks/       → создать задачу
    #      GET  /api/tasks/1/     → детально задача #1

    # 3) Схема OpenAPI и документация
    path('api/schema/',               SpectacularAPIView   .as_view(), name='schema'),
    path('api/schema/swagger-ui/',    SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',         SpectacularRedocView   .as_view(url_name='schema'), name='redoc'),
]

