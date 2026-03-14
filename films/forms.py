from django import forms  # Импортируем forms, чтобы создавать формы
from .models import Film  # Импортируем модель Film, чтобы связать форму с базой данных

class FilmForm(forms.ModelForm):  # Создаём форму на основе модели Film
    class Meta:  # Внутренний класс настроек формы
        model = Film  # Указываем модель, к которой привязана форма
        fields = ["title", "description", "review"]  # Указываем поля формы, которые будут сохраняться в базу

        widgets = {  # Настраиваем внешний вид полей для Bootstrap
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Например: Интерстеллар"}),  # Поле названия
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Коротко о сюжете…", "rows": 4}),  # Поле описания
            "review": forms.Textarea(attrs={"class": "form-control", "placeholder": "Твоё мнение о фильме…", "rows": 5}),  # Поле отзыва
        }  # Закрываем widgets