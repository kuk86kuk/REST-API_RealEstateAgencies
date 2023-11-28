from fastapi import APIRouter
from app.routers.models.object_realty import ObjectRealty
from app.database.model import ObjectRealty_table
import main



router = APIRouter(prefix='/object_realty', tags=['object_realty'])


@router.get("/properties")
def get_all_object_realty():
    '''
    Функция get_all_object_realty отвечает за получение списка всех объектов недвижимости. 
    Она отправляет GET запрос на /properties и возвращает список объектов ObjectRealty.
    '''
    list_new = []
    object_realty_all = main.db.query(ObjectRealty_table).all()
    for object_realty in object_realty_all:
       list_new.append(ObjectRealty(
            id=object_realty.id,
            tupe_object_realty=object_realty.tupe_object_realty, 
            address=object_realty.address,
            square=object_realty.square,
            number_rooms=object_realty.number_rooms, 
            object_status=object_realty.object_status,
            year_construction=object_realty.year_construction,
            price=object_realty.price,
            id_sobstvenik=object_realty.id_sobstvenik,
            id_deal=object_realty.id_deal
       ))
    return list_new


@router.get("/properties/{id}")
def get_object_realty(id):
    '''
    Функция get_object_realty отвечает за получение информации об указанном объекте недвижимости. 
    Она отправляет GET запрос на /properties/{id} с указанным идентификатором объекта и возвращает 
    информацию о нем в виде объекта ObjectRealty.
    '''
    object_realty = main.db.query(ObjectRealty_table).filter(ObjectRealty_table.id == id).first()
    if not object_realty:
        return 'Id не найден'
    return ObjectRealty(
            id=object_realty.id,
            tupe_object_realty=object_realty.tupe_object_realty, 
            address=object_realty.address,
            square=object_realty.square,
            number_rooms=object_realty.number_rooms, 
            object_status=object_realty.object_status,
            year_construction=object_realty.year_construction,
            price=object_realty.price,
            id_sobstvenik=object_realty.id_sobstvenik,
            id_deal=object_realty.id_deal
    )


@router.post("/properties")
def creat_new_object_realty(json: ObjectRealty):
    '''
    Функция creat_new_object_realty отвечает за создание нового объекта недвижимости. 
    Она отправляет POST запрос на /properties с данными нового объекта в формате JSON 
    и сохраняет его в базе данных. Возвращает идентификатор созданного объекта.
    '''
    # Создание объекта SQLAlchemy из объекта Pydantic
    object_realty = ObjectRealty_table(
        tupe_object_realty=json.tupe_object_realty, 
        address=json.address,
        square=json.square,
        number_rooms=json.number_rooms, 
        object_status=json.object_status,
        year_construction=json.year_construction,
        price=json.price,
        id_sobstvenik=json.id_sobstvenik,
        id_deal=json.id_deal)
    
    main.db.add(object_realty)     # добавляем в бд
    main.db.commit()     # сохраняем изменения
    return object_realty.id


@router.put("/properties/{id}")
def change_object_needability(id, json: ObjectRealty):
    '''
    Функция change_object_needability отвечает за обновление информации об указанном объекте недвижимости. 
    Она отправляет PUT запрос на /properties/{id} с указанным идентификатором объекта и данными, 
    которые нужно обновить. Обновляет информацию в базе данных и возвращает обновленную информацию о объекте.
    '''
    object_realty = main.db.query(ObjectRealty_table).filter(ObjectRealty_table.id == id).first()
    if not object_realty:
        return 'Id не найден'
    object_realty.tupe_object_realty = json.tupe_object_realty
    object_realty.address = json.address
    object_realty.square = json.square
    object_realty.number_rooms = json.number_rooms
    object_realty.object_status = json.object_status
    object_realty.year_construction = json.year_construction
    object_realty.price = json.price
    object_realty.id_sobstvenik = json.id_sobstvenik
    object_realty.id_deal = json.id_deal
    main.db.commit()
    return ObjectRealty(
        id=object_realty.id,
        tupe_object_realty=object_realty.tupe_object_realty, 
        address=object_realty.address,
        square=object_realty.square,
        number_rooms=object_realty.number_rooms, 
        object_status=object_realty.object_status,
        year_construction=object_realty.year_construction,
        price=object_realty.price,
        id_sobstvenik=object_realty.id_sobstvenik,
        id_deal=object_realty.id_deal
    )


@router.delete("/properties/{id}")
def change_object_needability(id):
    '''
    Функция delete_object_realty отвечает за удаление указанного объекта недвижимости. 
    Она отправляет DELETE запрос на /properties/{id} с указанным идентификатором объекта. 
    Удаляет объект из базы данных и возвращает информацию об удаленном объекте.
    '''
    object_realty = main.db.query(ObjectRealty_table).filter(ObjectRealty_table.id == id).first()
    if not object_realty:
        return 'Id не найден'
    main.db.delete(object_realty)  # удаляем объект
    main.db.commit()     # сохраняем изменения
    return ObjectRealty(
        id=object_realty.id,
        tupe_object_realty=object_realty.tupe_object_realty, 
        address=object_realty.address,
        square=object_realty.square,
        number_rooms=object_realty.number_rooms, 
        object_status=object_realty.object_status,
        year_construction=object_realty.year_construction,
        price=object_realty.price,
        id_sobstvenik=object_realty.id_sobstvenik,
        id_deal=object_realty.id_deal
    )