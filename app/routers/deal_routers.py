from fastapi import APIRouter
from app.routers.models.deal import Deal
from app.routers.models.object_realty import ObjectRealty
from app.database.model import Deal_table, ObjectRealty_table, Client_table
import main

router = APIRouter(prefix='/deals', tags=['deals'])


@router.get("/")
def get_all_deals():
    '''
    Функция get_all_deals возвращает список всех сделок из базы данных.
    '''
    list_new = []
    deals = main.db.query(Deal_table).all()
    for deal in deals:
       list_new.append(Deal(
            id=deal.id,
            id_sobstvenik=deal.id_sobstvenik,
            id_object_realty=deal.id_object_realty,
            id_clint=deal.id_client,
            datatime_deal=deal.datetime_deal,
            amount=deal.amount,
            currency=deal.currency,
            status=deal.status,
            type=deal.type,
       ))
    return list_new



@router.get("/{id}")
def get_deal(id):
    '''
    Функция get_deal возвращает информацию о сделке с указанным id.
    '''
    deal = main.db.query(Deal_table).filter(Deal_table.id == id).first()
    if not deal:
        return 'Id не найден'
    return Deal(
            id=deal.id,
            id_sobstvenik=deal.id_sobstvenik,
            id_object_realty=deal.id_object_realty,
            id_clint=deal.id_client,
            datatime_deal=deal.datetime_deal,
            amount=deal.amount,
            currency=deal.currency,
            status=deal.status,
            type=deal.type,
    )



@router.post("/")
def creat_new_deal(json: Deal):
    '''
    Функция create_new_deal создает новую сделку на основе переданных данных в формате JSON. 
    Перед созданием сделки проверяется существование объекта недвижимости, клиента и владельца 
    с указанными id. Если какой-то из них не найден, возвращается сообщение "Id не найден".
   '''
    object_realty = main.db.query(ObjectRealty_table).filter(ObjectRealty_table.id == json.id_object_realty).first()
    client = main.db.query(Client_table).filter(Client_table.id == json.id_client).first()
    sobstvenik = main.db.query(Client_table).filter(Client_table.id == json.id_sobstvenik).first()
    if (not object_realty) or (not client) or (not sobstvenik):
        return 'Id не найден'
    deal = Deal_table(
        id_object_realty=json.id_object_realty,
        id_sobstvenik=json.id_sobstvenik,
        id_client=json.id_client,
        datetime_deal=json.datetime_deal,
        amount=json.amount,
        currency=json.currency,
        status=json.status,
        type=json.type
        )
       
    main.db.add(deal)     # добавляем в бд
    main.db.commit()     # сохраняем изменения
    
    object_realty.id_sobstvenik=json.id_client   
    object_realty.id_deal=deal.id
    main.db.commit() 
    return deal.id




@router.put("/{id}")
def change_deal(id, json: Deal):
    '''
    Функция change_deal обновляет информацию о сделке с указанным id. 
    Также проверяется существование объекта недвижимости, клиента и владельца с указанными id. 
    Если какой-то из них не найден, возвращается сообщение "Id не найден".
    '''
    deal = main.db.query(Deal_table).filter(Deal_table.id == id).first()
    object_realty = main.db.query(ObjectRealty_table).filter(ObjectRealty_table.id == json.id_object_realty).first()
    client = main.db.query(Client_table).filter(Client_table.id == json.id_client).first()
    sobstvenik = main.db.query(Client_table).filter(Client_table.id == json.id_sobstvenik).first()
    if (not deal) or (not object_realty) or (not client) or (not sobstvenik):
        return 'Id не найден'
    
    deal.id_object_realty=json.id_object_realty
    deal.id_sobstvenik=json.id_sobstvenik
    deal.id_client=json.id_client
    deal.datetime_deal=json.datetime_deal
    deal.amount=json.amount
    deal.currency=json.currency
    deal.status=json.status
    deal.type=json.type

    object_realty.id_sobstvenik=json.id_client   
    object_realty.id_deal=deal.id
    main.db.commit()
    return Deal(
            id=deal.id,
            id_sobstvenik=deal.id_sobstvenik,
            id_object_realty=deal.id_object_realty,
            id_clint=json.id_client,
            datatime_deal=deal.datetime_deal,
            amount=deal.amount,
            currency=deal.currency,
            status=deal.status,
            type=deal.type,
    )


@router.delete("/{id}")
def delete_deal(id):
    '''
    Функция delete_deal удаляет сделку с указанным id из базы данных.
    Если сделка не найдена, возвращается сообщение "Id не найден".
    '''
    deal = main.db.query(Deal_table).filter(Deal_table.id == id).first()
    if not deal:
        return 'Id не найден'
    main.db.delete(deal)  # удаляем объект
    main.db.commit()     # сохраняем изменения
    return Deal(
            id=deal.id,
            id_sobstvenik=deal.id_sobstvenik,
            id_object_realty=deal.id_object_realty,
            id_clint=deal.id_client,
            datatime_deal=deal.datetime_deal,
            amount=deal.amount,
            currency=deal.currency,
            status=deal.status,
            type=deal.type,
    )