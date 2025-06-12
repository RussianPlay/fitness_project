.PHONY: help install test lint run docker-build docker-up docker-down docker-logs clean

# Переменные
PYTHON = python3
VENV = venv
PIP = $(VENV)/bin/pip
MANAGE = $(PYTHON) manage.py

help:
	@echo "Доступные команды:"
	@echo "  make install    - Установка зависимостей"
	@echo "  make test       - Запуск тестов"
	@echo "  make lint       - Проверка кода линтерами"
	@echo "  make run        - Запуск сервера разработки"
	@echo "  make migrate    - Применение миграций"
	@echo "  make shell      - Запуск Django shell"
	@echo "  make docker-build - Сборка Docker-образов"
	@echo "  make docker-up  - Запуск контейнеров"
	@echo "  make docker-down - Остановка контейнеров"
	@echo "  make docker-logs - Просмотр логов контейнеров"
	@echo "  make clean      - Очистка временных файлов"

# Установка зависимостей
install:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Тестирование
test:
	$(MANAGE) test

# Линтинг
lint:
	flake8 .
	black . --check
	isort . --check-only

# Запуск сервера разработки
run:
	$(MANAGE) runserver

# Миграции
migrate:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

# Django shell
shell:
	$(MANAGE) shell

# Docker команды
docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

# Очистка
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} +
	find . -type d -name "*.egg" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type d -name ".coverage" -exec rm -r {} +
	find . -type d -name "htmlcov" -exec rm -r {} +
	find . -type d -name ".mypy_cache" -exec rm -r {} +
	find . -type d -name ".ruff_cache" -exec rm -r {} +
	find . -type d -name ".tox" -exec rm -r {} +
	find . -type d -name "dist" -exec rm -r {} +
	find . -type d -name "build" -exec rm -r {} +
	rm -rf .coverage
	rm -rf coverage.xml
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf .tox
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
