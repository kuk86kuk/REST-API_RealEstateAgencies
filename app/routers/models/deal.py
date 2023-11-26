from pydantic import BaseModel
from datetime import date

class Deal(BaseModel):
    id: int
    id_object_realty: int 
    id_clint: int
    datatime_deal: date
    amount: int
    currency: str
    status: str
    type: str