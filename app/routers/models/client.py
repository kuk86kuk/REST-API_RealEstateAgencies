from pydantic import BaseModel


class Client(BaseModel):
    id: int
    full_name: str
    contact_information: list
    date_birth: data
    