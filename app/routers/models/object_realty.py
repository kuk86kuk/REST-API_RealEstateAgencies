from pydantic import BaseModel


class ObjectRealty(BaseModel):
    id: int = None
    tupe_object_realty: str = 'Продажа' 
    address: str = 'г. Екатеринбург, ул. Ленина 210, кв. 7'
    square: int = 53
    number_rooms: int = 3
    object_status: str = "Вторичка"
    year_construction: int = 1993
    price: int = 5000000
    id_sobstvenik: int = 1
    id_deal: int = None
    