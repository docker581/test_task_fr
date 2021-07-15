# test_task_fr

## Описание проекта
Тестовое задание - API для системы опросов пользователей

## Стек технологий
- Python 3.8.5
- Django 2.2.10
- Django Rest Framework (DRF) 3.12.4
- Docker-compose 3.3
- Postgres 12.4
- Nginx 1.19.3
- Gunicorn 20.0.4

## Установка docker
https://docs.docker.com/engine/install/

## Команды
### Клонирование репозитория
```bash
git clone https://github.com/docker581/test_task_fr
```

### Пример файла .env
```bash
DB_ENGINE=django.db.backends.postgresql 
DB_NAME=postgres 
POSTGRES_USER=postgres 
POSTGRES_PASSWORD=postgres
DB_HOST=db 
DB_PORT=5432
```

### Запуск приложения
```bash
docker-compose up -d
```

### Создание суперпользователя
```bash
docker-compose exec web python manage.py makemigrations
```
```bash
docker-compose exec web python manage.py migrate --noinput
```
```bash
docker-compose exec web python manage.py createsuperuser
```

## Документация по API
- localhost/polls/ - работа с опросами
- localhost/polls/<poll_id>/questions/ - работа с вопросами
