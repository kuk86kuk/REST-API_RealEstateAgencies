from pydantic import BaseModel


class Deal(BaseModel):
    id: int
    id_object_realty: int 
    id_clint: int
    datatime_deal: data
    amount: int
    currency: str
    status: str
    type: str