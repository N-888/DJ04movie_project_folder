from django.shortcuts import render, redirect  # Импортируем render для HTML и redirect для перенаправления
from django.contrib import messages  # Импортируем messages для сообщений “успешно/ошибка”
from .models import Film  # Импортируем модель Film, чтобы читать данные из базы
from .forms import FilmForm  # Импортируем FilmForm, чтобы добавлять данные в базу через форму

def film_list(request):  # Представление для страницы со списком фильмов
    films = Film.objects.all().order_by("-id")  # Берём все фильмы из базы и сортируем: новые сверху
    return render(request, "films/film_list.html", {"films": films})  # Открываем HTML и передаём films в шаблон

def film_create(request):  # Представление для страницы добавления фильма
    if request.method == "POST":  # Проверяем, отправили ли форму
        form = FilmForm(request.POST)  # Создаём форму и заполняем данными из POST
        if form.is_valid():  # Проверяем, корректно ли заполнены поля
            form.save()  # Сохраняем фильм в базу данных
            messages.success(request, "Фильм успешно добавлен!")  # Показываем успешное сообщение
            return redirect("film_list")  # Перенаправляем на страницу списка фильмов
        messages.error(request, "Проверь поля: данные заполнены некорректно.")  # Показываем сообщение об ошибке
    else:  # Если просто открыли страницу
        form = FilmForm()  # Создаём пустую форму

    return render(request, "films/film_create.html", {"form": form})  # Открываем HTML и передаём form в шаблон