# URL-Shortener-FastAPI
Небольшой pet-проект, демонстрирующий работу с FastAPI, PostgreSQL, Docker.

<img width="1442" height="857" alt="Снимок экрана от 2025-12-01 22-04-09" src="https://github.com/user-attachments/assets/89ef9ae0-3c83-4097-82d8-8acb6efdbe89" />
<img width="1407" height="129" alt="Снимок экрана от 2025-12-01 22-04-32" src="https://github.com/user-attachments/assets/2b7871fd-1428-45d4-ae6e-820ca74753c5" />


## Возможности
- Создание коротких ссылок
- Перенаправление по короткому коду
- Хранение в PostgreSQL
- Автоматическая генерация коротких UUID
- Swagger документация
- Docker-контейнеры для простого запуска

## Стек технологий
```
aiosqlite>=0.21.0
asyncpg>=0.31.0
fastapi>=0.122.0
greenlet>=3.2.4
httpx>=0.28.1
pytest>=9.0.1
pytest-asyncio>=1.3.0
sqlalchemy>=2.0.44
uvicorn>=0.38.0
```

## Установка и запуск
```
git clone https://github.com/username/project.git
cd project
```

```
python -m venv .venv
source .venv/bin/activate
```

```
pip install -r requirements.txt
uvicorn src.main:app --reload
```

## API документация
```
http://localhost:8000/docs
```

## Структура проекта
```
.
├── docker-compose.yaml        # Docker-компоуз для запуска приложения и PostgreSQL
├── pyproject.toml             # Конфигурация зависимостей (uv)
├── requirements.txt           # Альтернативный способ установки зависимостей (pip)
├── uv.lock                    # Lock-файл зависимостей для uv
├── pytest.ini                 # Конфигурация Pytest
├── README.md                  # Документация проекта
│
├── src/                       # Основной код приложения
│   ├── main.py                # Точка входа FastAPI
│   ├── index.html             # Простая HTML-страница для UI
│   ├── exception.py           # Обработчики ошибок и кастомные исключения
│   ├── service.py             # Бизнес-логика сокращения ссылок
│   ├── shortener.py           # Генератор коротких ссылок / утилиты
│   │
│   └── database/              # Работа с базой данных
│       ├── db.py              # Подключение к PostgreSQL / sessionmaker
│       ├── models.py          # SQLAlchemy модели
│       └── crud.py            # CRUD-операции
│
└── tests/                     # Тесты
    ├── conftest.py            # Фикстуры для Pytest (тестовая БД, клиент и т.д.)
    ├── test_api.py            # Тесты API FastAPI
    └── test_service.py        # Тесты бизнес-логики

```
