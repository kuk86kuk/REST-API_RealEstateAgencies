# REST-API информационная система агентства недвижимости

Проект является информационной системой для агентства недвижимости, разработанной на FastApi, Pydantic, SQLAlchemy, SQLite. Система предоставляет API, позволяющее агентству управлять информацией о недвижимости.


## Эндпойнты

## Объекты недвижимости
Метод	Эндпоинт	    Описание
GET	    /properties	    Получить список всех объектов недвижимости
GET	    /properties/:id	Получить информацию об указанном объекте
POST	/properties	    Создать новый объект недвижимости
PUT	    /properties/:id	Обновить информацию об указанном объекте
DELETE	/properties/:id	Удалить указанный объект недвижимости

## Клиенты
Метод	Эндпоинт	    Описание
GET	    /clients	    Получить список всех клиентов
GET	    /clients/:id	Получить информацию о указанном клиенте
POST	/clients	    Создать нового клиента
PUT	    /clients/:id	Обновить информацию о указанном клиенте
DELETE	/clients/:id	Удалить указанного клиента

## Сделки
Метод	Эндпоинт	    Описание
GET	    /deals	        Получить список всех сделок
GET	    /deals/:id	    Получить информацию о указанной сделке
POST	/deals	        Создать новую сделку
PUT	    /deals/:id	    Обновить информацию о указанной сделке
DELETE	/deals/:id	    Удалить указанную сделку


## Требования
- Python
- Установка зависимостей: `pip install -r requirements.txt`


## Установка
1. Клонируйте репозиторий:
   
   ```bash
   https git clone https://github.com/kuk86kuk/REST-API_RealEstateAgencies.git
   ssh   git clone git@github.com:kuk86kuk/REST-API_RealEstateAgencies.git

2. Запуск
Перейдите в директорию проекта:

   cd REST-API_RealEstateAgencies
   pip install -r requirements.txt
   
Запустите приложение:

    uvicorn main:app --reload
    или
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload

    Приложение будет доступно по адресу 
      http://localhost:8000/
      http://127.0.0.1:8000/


## Документация API
   http://127.0.0.1:8000/docs


## Технологии
    FastApi    REST-API.
    SQLAlchemy Работа с базой данных.
    SQLite     База данных.
    Pydantic   Проверки и сериализации данных.


## Автор
   Треглазов Егор Васильевич





