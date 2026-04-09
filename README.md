# Yatube API

API для социальной сети Yatube. Позволяет публиковать посты, оставлять комментарии, подписываться на авторов и объединять публикации в тематические группы.

## Технологии

- Python 3.12
- Django 4.2
- Django REST Framework 3.14
- Djoser + Simple JWT (аутентификация по токенам)

## Документация 

```
http://127.0.0.1:8000/redoc/
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone {ссылка на гит}
```

```
cd api-final-yatube
```

Cоздать и активировать виртуальное окружение:

```
py -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
py -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
py manage.py migrate
```

Запустить проект:

```
py manage.py runserver
```
