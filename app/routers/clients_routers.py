from fastapi import APIRouter
from app.routers.models.client import Client
from app.database.model import Client_table
import main


router = APIRouter(prefix='/clients', tags=['clients'])


@router.get("/")
def get_all_clients():
    '''
    Функция get_all_clients возвращает список всех клиентов из базы данных.
    '''
    list_new = []
    clients = main.db.query(Client_table).all()
    for cl in clients:
       list_new.append(Client(
           id=cl.id,
           full_name=cl.full_name,
           phone_number=cl.full_name,
           email=cl.email

       ))
    return list_new



@router.get("/{id}")
def get_client(id):
    '''
    Функция get_client возвращает информацию о клиенте с указанным id.
    '''
    client = main.db.query(Client_table).filter(Client_table.id == id).first()
    if not client:
        return 'Id не найден'
    return Client(
        id=client.id,
        full_name=client.full_name,
        phone_number=client.phone_number,
        email=client.email
    )



@router.post("/")
def creat_new_client(json: Client):
    '''
    Функция creat_new_client отвечает за создание нового клиента. 
    Она отправляет POST запрос с данными нового объекта в формате JSON 
    и сохраняет его в базе данных. Возвращает идентификатор созданного объекта.
    '''
    full_name = json.full_name
    phone_number = json.phone_number
    email = json.email
    # Создание объекта SQLAlchemy из объекта Pydantic
    Client = Client_table(
        full_name = full_name,
        phone_number = phone_number,
        email = email)
    
    main.db.add(Client)     # добавляем в бд
    main.db.commit()     # сохраняем изменения
    return Client.id



@router.put("/{id}")
def change_client(id, json: Client):
    '''
    Функция change_client отвечает за обновление информации об указанном клиенте. 
    Она отправляет PUT запрос на с указанным идентификатором объекта и JSON, которые нужно обновить.
    Обновляет информацию в базе данных и возвращает обновленную информацию о объект
    '''
    
    client = main.db.query(Client_table).filter(Client_table.id == id).first()
    if not client:
        return 'Id не найден'
    client.full_name = json.full_name
    client.phone_number = json.phone_number
    client.email = json.email
    main.db.commit()

    return Client(
        id=client.id,
        full_name=client.full_name,
        phone_number=client.phone_number,
        email=client.email
    )



@router.delete("/{id}")
def delete_client(id):
    '''
    Функция delete_client отвечает за удаление указанного клиента. 
    Она отправляет DELETE запрос с указанным идентификатором объекта. 
    Удаляет объект из базы данных и возвращает информацию об удаленном объекте.
    '''
    client = main.db.query(Client_table).filter(Client_table.id == id).first()
    if not client:
        return 'Id не найден'
    main.db.delete(client)  # удаляем объект
    main.db.commit()     # сохраняем изменения
    return Client(
        id=client.id,
        full_name=client.full_name,
        phone_number=client.phone_number,
        email=client.email
    )


