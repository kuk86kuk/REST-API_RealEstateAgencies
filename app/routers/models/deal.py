from pydantic import BaseModel
from datetime import date

class Deal(BaseModel):
    id: int = None
    id_object_realty: int = 2
    id_sobstvenik: int = 2
    id_client: int = 1
    datetime_deal: date = None
    amount: int = 6000000
    currency: str = 'руболь'
    status: str = 'завершено'
    type: str = "дкп"