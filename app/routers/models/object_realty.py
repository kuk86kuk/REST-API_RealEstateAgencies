from pydantic import BaseModel


class ObjectRealty(BaseModel):
    id: int
    tupe_object_realty: str 
    address: str
    square: int 
    number_rooms: None
    object_status: str
    year_construction: int
    contact_information: str
    price: int
    id_clint: int
    id_deal: int
    