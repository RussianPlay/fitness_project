FROM python:3.11-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории
WORKDIR /app

# Копирование файлов зависимостей
COPY requirements.txt .

# Установка Python зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Создание непривилегированного пользователя
RUN useradd -m appuser

# Копирование проекта
COPY . .

# Установка прав доступа
RUN chown -R appuser:appuser /app && \
    chmod -R 755 /app && \
    mkdir -p /app/fitness_project/staticfiles /app/fitness_project/media && \
    chown -R appuser:appuser /app/fitness_project/staticfiles /app/fitness_project/media

# Переключение на непривилегированного пользователя
USER appuser

# Порт для Django
EXPOSE 8000

# Переменные окружения
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=fitness_project.settings 