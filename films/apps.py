from django.apps import AppConfig  # Импортируем базовый класс конфигурации приложения


class FilmsConfig(AppConfig):  # Создаём конфигурацию приложения films
    default_auto_field = "django.db.models.BigAutoField"  # Указываем тип id по умолчанию
    name = "films"  # Указываем имя приложения