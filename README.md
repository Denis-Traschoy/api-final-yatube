# Yatube API

API для социальной сети Yatube. Позволяет публиковать посты, оставлять комментарии, подписываться на авторов и объединять публикации в тематические группы.

## Технологии

- Python 3.12
- Django 4.2
- Django REST Framework 3.14
- Djoser + Simple JWT (аутентификация по JWT-токенам)
- SQLite (разработка)
- Pytest (тестирование)

## Возможности API

- Регистрация и аутентификация пользователей (JWT-токены)
- Создание, редактирование, удаление и просмотр публикаций
- Добавление изображений к публикациям (в формате Base64)
- Комментирование публикаций
- Подписка на авторов и просмотр списка подписок
- Поиск по подпискам
- Просмотр тематических групп (сообществ)
- Пагинация ответов для списков публикаций

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

## Примеры запросов

### Получение JWT-токена

```http
POST /api/v1/jwt/create/
Content-Type: application/json

{
    "username": "string",
    "password": "string"
}
```

Ответ:
```json
{
    "refresh": "string",
    "access": "string"
}
```

### Обновление JWT-токена

```http
POST /api/v1/jwt/refresh/
Content-Type: application/json

{
    "refresh": "string"
}
```

Ответ:
```json
{
    "access": "string"
}
```

### Проверка JWT-токена

```http
POST /api/v1/jwt/verify/
Content-Type: application/json

{
    "token": "string"
}
```

### Получение списка публикаций (доступно всем)

```http
GET /api/v1/posts/?limit=10&offset=0
```

Ответ с пагинацией:
```json
{
    "count": 123,
    "next": "http://127.0.0.1:8000/api/v1/posts/?limit=10&offset=10",
    "previous": null,
    "results": [
        {
            "id": 0,
            "author": "string",
            "text": "string",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "string",
            "group": 0
        }
    ]
}
```

### Создание публикации (требуется авторизация)

```http
POST /api/v1/posts/
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
    "text": "string",
    "group": 0
}
```

Ответ:
```json
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2021-10-14T20:41:29.648Z",
    "image": null,
    "group": 0
}
```

### Получение публикации по ID (доступно всем)

```http
GET /api/v1/posts/{id}/
```

### Обновление публикации (только автор)

```http
PUT /api/v1/posts/{id}/
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
    "text": "string",
    "group": 0
}
```

### Частичное обновление публикации (только автор)

```http
PATCH /api/v1/posts/{id}/
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
    "text": "string"
}
```

### Удаление публикации (только автор)

```http
DELETE /api/v1/posts/{id}/
Authorization: Bearer <your_access_token>
```

### Получение списка сообществ (доступно всем)

```http
GET /api/v1/groups/
```

Ответ:
```json
[
    {
        "id": 0,
        "title": "string",
        "slug": "string",
        "description": "string"
    }
]
```

### Получение информации о сообществе (доступно всем)

```http
GET /api/v1/groups/{id}/
```

### Получение комментариев к публикации (доступно всем)

```http
GET /api/v1/posts/{post_id}/comments/
```

Ответ:
```json
[
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "created": "2021-10-14T20:41:29.648Z",
        "post": 0
    }
]
```

### Добавление комментария (требуется авторизация)

```http
POST /api/v1/posts/{post_id}/comments/
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
    "text": "string"
}
```

Ответ:
```json
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2021-10-14T20:41:29.648Z",
    "post": 0
}
```

### Получение комментария по ID (доступно всем)

```http
GET /api/v1/posts/{post_id}/comments/{id}/
```

### Обновление комментария (только автор)

```http
PUT /api/v1/posts/{post_id}/comments/{id}/
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
    "text": "string"
}
```

### Частичное обновление комментария (только автор)

```http
PATCH /api/v1/posts/{post_id}/comments/{id}/
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
    "text": "string"
}
```

### Удаление комментария (только автор)

```http
DELETE /api/v1/posts/{post_id}/comments/{id}/
Authorization: Bearer <your_access_token>
```

### Получение списка подписок (требуется авторизация)

```http
GET /api/v1/follow/?search=string
Authorization: Bearer <your_access_token>
```

Ответ:
```json
[
    {
        "user": "string",
        "following": "string"
    }
]
```

### Подписка на пользователя (требуется авторизация)

```http
POST /api/v1/follow/
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
    "following": "string"
}
```

Ответ:
```json
{
    "user": "string",
    "following": "string"
}
```

### Ошибки валидации при подписке

При попытке подписаться на самого себя:
```json
{
    "following": [
        "Нельзя подписаться на самого себя!"
    ]
}
```

При попытке подписаться на несуществующего пользователя:
```json
{
    "following": [
        "Объект с username=... не существует."
    ]
}
```

При отсутствии обязательного поля:
```json
{
    "following": [
        "Обязательное поле."
    ]
}
```
## Автор

Трещёв Денис

- GitHub: https://github.com/Denis-Traschoy
- Email: Denzdayplay@gmail.com
- Telegram: [@ScarlettFool](https://t.me/ScarlettFool)