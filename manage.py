#!/usr/bin/env python  # Говорим системе запускать файл через Python
"""Django's command-line utility for administrative tasks."""  # Краткое описание назначения файла

import os  # Импортируем os, чтобы работать с переменными окружения
import sys  # Импортируем sys, чтобы передавать аргументы командной строки Django


def main():  # Создаём главную функцию, которая запускает Django-команды
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_project.settings")  # Указываем Django, где лежат настройки проекта
    try:  # Пробуем импортировать функцию запуска Django-команд
        from django.core.management import execute_from_command_line  # Импортируем запуск команд Django из консоли
    except ImportError as exc:  # Если Django не найден, перехватываем ошибку
        raise ImportError(  # Показываем понятную ошибку
            "Couldn't import Django. Are you sure it's installed and "  # Подсказываем, что Django может быть не установлен
            "available on your PYTHONPATH environment variable? Did you "  # Подсказываем, что может быть проблема с окружением
            "forget to activate a virtual environment?"  # Подсказываем, что могло быть не включено venv
        ) from exc  # Привязываем исходную ошибку
    execute_from_command_line(sys.argv)  # Запускаем команду Django, которую ввели в терминале


if __name__ == "__main__":  # Проверяем, что файл запускают напрямую
    main()  # Запускаем главную функцию