from django.contrib import admin  # Импортируем admin, чтобы регистрировать модели в админке
from .models import Film  # Импортируем модель Film из models.py


@admin.register(Film)  # Регистрируем модель Film в админке через декоратор
class FilmAdmin(admin.ModelAdmin):  # Создаём настройки отображения модели Film в админке
    list_display = ("id", "title")  # Какие колонки показывать в списке объектов
    search_fields = ("title",)  # По каким полям можно искать