# Шаблон Telegram бота на aiogram 3.15

В проекте использовались:

    - Aiogram 3.15
    - SQLAlchemy 2.0 (драйвер sqlite, меняется под вашу базу)
    - Fluent localization

Особенности шаблона:

    - Подключение базы данных с помощью SQLAlchemy ORM
    - Несколько готовых middlewares
    - l10n с помощью Fluent
    - Рассылка всем пользователям из базы данных  

# Установка

Требования для установки:

    - Linux
    - Docker

Процесс установки:
    
    - Копируем env-example и меняем на .env
    - docker-compose up -d (or docker compose up -d)
