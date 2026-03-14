from django.contrib import admin  # Импортируем админку Django
from django.urls import path, include  # Импортируем path для маршрутов и include для подключения маршрутов приложения

urlpatterns = [  # Создаём список маршрутов проекта
    path("admin/", admin.site.urls),  # Маршрут для админки
    path("", include("films.urls")),  # Главную страницу и пути отдаём приложению films
]