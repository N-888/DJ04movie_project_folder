from pathlib import Path  # Импортируем Path, чтобы удобно собирать пути к папкам проекта

BASE_DIR = Path(__file__).resolve().parent.parent  # Находим корневую папку проекта (там, где manage.py)

SECRET_KEY = "django-insecure-change-me-in-production"  # Секретный ключ проекта (для учебного проекта можно так)

DEBUG = True  # Включаем режим отладки (в продакшене должно быть False)

ALLOWED_HOSTS = []  # Список доменов, которым разрешено открывать сайт (для локальной разработки оставляем пустым)

INSTALLED_APPS = [  # Список подключённых приложений Django
    "django.contrib.admin",  # Админка Django
    "django.contrib.auth",  # Авторизация и пользователи
    "django.contrib.contenttypes",  # Система типов контента
    "django.contrib.sessions",  # Сессии
    "django.contrib.messages",  # Сообщения (success/error)
    "django.contrib.staticfiles",  # Работа со статическими файлами
    "films",  # Подключаем наше приложение films
]

MIDDLEWARE = [  # Список middleware (прослоек обработки запросов)
    "django.middleware.security.SecurityMiddleware",  # Базовая безопасность
    "django.contrib.sessions.middleware.SessionMiddleware",  # Поддержка сессий
    "django.middleware.common.CommonMiddleware",  # Общие настройки обработки запросов
    "django.middleware.csrf.CsrfViewMiddleware",  # CSRF-защита для форм
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # Подключает пользователя к request
    "django.contrib.messages.middleware.MessageMiddleware",  # Подключает сообщения к request
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # Защита от clickjacking
]

ROOT_URLCONF = "movie_project.urls"  # Говорим Django, где главный файл маршрутов (urls.py)

TEMPLATES = [  # Настройки шаблонов (HTML)
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",  # Используем стандартный движок шаблонов Django
        "DIRS": [BASE_DIR / "templates"],  # Указываем папку templates в корне проекта для base.html
        "APP_DIRS": True,  # Разрешаем искать шаблоны внутри приложений (например films/templates/films)
        "OPTIONS": {
            "context_processors": [  # Добавляем “переменные по умолчанию” в шаблоны
                "django.template.context_processors.debug",  # Добавляет DEBUG и другие данные для отладки
                "django.template.context_processors.request",  # Добавляет request в шаблоны (нужно для подсветки активного меню)
                "django.contrib.auth.context_processors.auth",  # Добавляет пользователя и auth-данные
                "django.contrib.messages.context_processors.messages",  # Добавляет messages (success/error) в шаблоны
            ],
        },
    },
]

WSGI_APPLICATION = "movie_project.wsgi.application"  # Указываем файл для запуска проекта через WSGI-сервер

DATABASES = {  # Настраиваем базу данных
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # Используем SQLite (учебный вариант, хранится файлом)
        "NAME": BASE_DIR / "db.sqlite3",  # Путь к файлу базы данных
    }
}

AUTH_PASSWORD_VALIDATORS = [  # Валидаторы паролей (оставляем стандартные)
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},  # Запрещает слишком похожий на имя пароль
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},  # Проверяет минимальную длину
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},  # Запрещает популярные пароли
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},  # Запрещает пароли только из цифр
]

LANGUAGE_CODE = "ru-ru"  # Выставляем русский язык интерфейса Django

TIME_ZONE = "Europe/Amsterdam"  # Выставляем часовой пояс (как ты просила)

USE_I18N = True  # Включаем интернационализацию

USE_TZ = True  # Включаем timezone-aware даты

STATIC_URL = "static/"  # URL-префикс для статических файлов

STATICFILES_DIRS = [BASE_DIR / "static"]  # Говорим Django, что статика лежит в папке static в корне проекта

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"  # Тип поля id по умолчанию