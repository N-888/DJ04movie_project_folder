from django.contrib import admin  # Импортируем админку Django
from django.urls import path, include  # Импортируем path для маршрутов и include для подключения маршрутов приложения

urlpatterns = [  # Список маршрутов проекта
    path("admin/", admin.site.urls),  # Маршрут для Админки
    path("", include("films.urls")),  # Главную страницу отдаём приложению films
]