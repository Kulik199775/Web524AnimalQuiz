# Web524AnimalQuiz

Веб-приложение для викторин о животных. Проект разработан на Django Rest Framework (DRF) и поддерживает запуск как 
в локальном окружении, так и в Docker.

---

## Возможности

- Управление разделами, контентом и вопросами викторины
- Пользовательская система с ролями (администратор, участник)
- REST API с пагинацией и фильтрацией
- JWT-аутентификация (Simple JWT)
- Документация API (подготовка к интеграции Swagger/ReDoc)
- Готовность к запуску в Docker
- Полное покрытие тестами (17 успешных тестов)

---

## Технологии

|Backend| Python 3.x, Django 6.0.3, Django REST Framework
|Кеширование| redis
|База данных| SQLite (локально), PostgreSQL (Docker), поддержка MSSQL
|Аутентификация| JWT (djangorestframework-simplejwt)
|Инфраструктура| Docker, Docker Compose
|Тестирование| Unit-тесты, Coverage.py
|Документация| drf-yasg (Swagger, redoc)
|Дополнительно| django-filter, corsheaders, redis

---

## Установка и запуск

### Предварительные требования

- Python 3.12+
- pip
- redis
- Docker и Docker Compose (для контейнерного запуска) 

### 1. Клонирование репозитория

```bash
git clone https://github.com/Kulik199775/Web524AnimalQuiz.git
cd Web524AnimalQuiz
```

### 2. Настройка окружения

Скопируйте файл `.env_sample` в `.env` и заполните его своими данными:

```bash
cp .env_sample .env
```

Отредактируйте файл `.env`, указав необходимые параметры:

```env
# Для PostgreSQL (Docker)
POSTGRESQL_USER_DOCKER=your_user
POSTGRESQL_DATABASE_DOCKER=your_db
POSTGRESQL_PASSWORD_DOCKER=your_password
POSTGRESQL_PORT_DOCKER=5432
POSTGRESQL_HOST_DOCKER=postgres

# Для MSSQL (локально)
MS_SQL_USER=your_user
MS_SQL_KEY=your_password
MS_SQL_SERVER=localhost
MS_SQL_DATABASE=Web524AnimalQuiz
MS_SQL_DRIVER=ODBC Driver 18 for SQL Server
MS_SQL_PAD_DATABASE=master

# Email настройки
EMAIL_HOST_USER=your_email@yandex.com
HOST_PASSWORD_APP=your_app_password

# Redis для кэширования
CACHE_STATUS=True
CACHE_LOCATION=redis://redis:6379
```

### 3. Запуск проекта

#### Вариант 1: Локально (без Docker)

```bash
# Создание виртуального окружения
python -m venv .venv
source .venv/bin/activate  # для Linux/Mac
# или
.venv\Scripts\activate  # для Windows

# Установка зависимостей
pip install -r requirements.txt

# Создание базы данных
python manage.py ccdb
```

# Создание миграций
```bash
python manage.py makemigrations
```

# Применение миграций
```bash
python manage.py migrate
```

# Создание пользователей с разным уровнем доступа при помощи:
```bash
python manage.py ccsu
```

# Загрузка тестовых данных (опционально)
```bash
python manage.py loaddata users_fixture.json
python manage.py loaddata sections_fixture.json
```

# Запуск сервера redis
```bash
redis-server
```

# Запуск сервера
```bash
python manage.py runserver
```


#### Вариант 2: В Docker-контейнере

```bash
# Сборка и запуск контейнеров
docker-compose up -d --build


Приложение будет доступно по адресу: `http://localhost:8000`

### 4. Остановка Docker-контейнеров

```bash
docker-compose down
```

---

## Тестирование

### Запуск всех тестов

```bash
python manage.py test
```

Ожидаемый результат:
```
Found 17 test(s).
System check identified no issues (0 silenced).
.................
----------------------------------------------------------------------
Ran 17 tests in 21.201s
OK
```

### Запуск конкретного теста

```bash
# Тесты конкретного приложения
python manage.py test sections.tests

# Конкретный тестовый класс
python manage.py test sections.tests.test_03_question.QuestionTestAdmin

# Конкретный тестовый метод
python manage.py test sections.tests.test_03_question.QuestionTestAdmin.test_17_question_is_correct
```

### Проверка покрытия кода тестами

```bash
# Установка coverage
pip install coverage

# Запуск тестов с coverage
coverage run --source='.' manage.py test

# Просмотр отчета в терминале
coverage report

# Создание HTML-отчета
coverage html
# Открыть отчет: htmlcov/index.html
```

## API Эндпоинты

### Аутентификация

| POST | `/users/token/` | Получение JWT токена 
| POST | `/users/token/refresh/` | Обновление JWT токена

### Разделы (Sections)

| GET | `/section/` | Список разделов | Все 
| GET | `/section/{id}/` | Детали раздела | Все 
| POST | `/sections/create/` | Создание раздела | Админ 
| PUT | `/section/{id}/update/` | Обновление раздела | Админ 
| DELETE | `/section/{id}/delete/` | Удаление раздела | Админ 

### Контент (Content)

| GET | `/content/` | Список контента | Все 
| GET | `/content/{id}/` | Детали контента | Все 
| POST | `/content/create/` | Создание контента | Админ 
| PATCH | `/content/{id}/update/` | Обновление контента | Админ 
| DELETE | `/content/{id}/delete/` | Удаление контента | Админ 

### Вопросы (Questions)

| GET | `/question/` | Список вопросов | Все 
| GET | `/question/{id}/` | Детали вопроса | Все 
| POST | `/question/{id}/` | Проверка ответа | Все 

---

## Полезные команды

### Управление базой данных

```bash
# Создание и применение миграций
python manage.py makemigrations
python manage.py migrate

# Очистка базы данных
python manage.py flush
```

### Работа с Docker

```bash
# Сборка образов
docker-compose build

# Просмотр логов
docker-compose logs -f

# Выполнение команд в контейнере
docker-compose exec web python manage.py shell

# Остановка и удаление контейнеров
docker-compose down -v
```

---

---

## Пагинация:
- Реализована пагинация 1-го объекта на страницу.

---

## Решенные проблемы и особенности

### Известные проблемы и их решения

| Ошибка подключения к PostgreSQL | В файле `settings.py` раскомментированы настройки PostgreSQL и 
закомментированы настройки MSSQL. Выберите нужную конфигурацию. 


### Рекомендации по разработке

1. Для локальной разработки используйте SQLite или MSSQL (раскомментируйте соответствующие строки в `settings.py`)
2. Для продакшена используйте PostgreSQL в Docker
3. Всегда используйте `.env` файл для хранения чувствительных данных
4. Перед коммитом проверяйте код на соответствие PEP8 (flake8)

---
