from pydantic import BaseModel
from datetime import date

class Client(BaseModel):
    id: int = None
    full_name: str = 'Иван Иван Иванович'
    phone_number: str = '89995643269'
    email: str = "egro@yandex.ru"
    