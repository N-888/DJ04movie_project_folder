from django.urls import path  # Импортируем path для создания маршрутов
from . import views  # Импортируем views.py, чтобы использовать функции-страницы

urlpatterns = [  # Список маршрутов приложения
    path("", views.film_list, name="film_list"),  # Главная страница со списком фильмов
    path("add/", views.film_create, name="film_create"),  # Страница добавления фильма
]