## Описание проекта.

_**Планировщик постов автосервиса**_ - API для ведения записей клиентов на сервис, резервирования времени, планирование работ и создания заказ-нарядов.
Подключена база данных sqlite+aiosqlite через SQLAlchemy. Миграции настроены средставами Alembic.

В планах найти frontend-разработчика и дополнить приложение графическим web-интерфейсом; добавить личный кабинет администратора.

## Используемые технологии.

[![Python 3.12](https://img.shields.io/badge/Python-3.12-brightgreen.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.1-brightgreen.svg?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.30.1-brightgreen.svg?style=flat&logo=uvicorn&logoColor=white)](https://www.uvicorn.org/)
[![Alembic](https://img.shields.io/badge/Alembic-1.13.1-brightgreen.svg?style=flat&logo=alembic&logoColor=white)](https://alembic.sqlalchemy.org/en/latest/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.29-brightgreen.svg?style=flat&logo=sqlalchemy&logoColor=white)](https://alembic.sqlalchemy.org/en/latest/)

## Запуск проекта
Из директории приложения, выполните следующую команду:
```
uvicorn app.main:app --reload
```
Теперь документация доступна по адресу:
```
http://127.0.0.1:8000/docs
```
