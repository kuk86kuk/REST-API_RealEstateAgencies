from fastapi import APIRouter
from app.routers.models.client import Client
from app.database.model import Client_table
import main


router = APIRouter(prefix='/clients', tags=['clients'])


@router.get("/")
def get_all_clients():
    '''
   GET	/clients	Получить список всех клиентов
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
    GET	/clients/:id	Получить информацию о указанном клиенте
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
    POST	/clients	Создать нового клиента
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
  PUT	/clients/:id	Обновить информацию о указанном клиенте
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
   DELETE	/clients/:id	Удалить указанного клиента
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