from fastapi import APIRouter


router = APIRouter(prefix='/clients', tags=['clients'])


@router.get("/")
def get_all_clients():
    '''
   GET	/clients	Получить список всех клиентов
    '''
    pass



@router.get("/{id}")
def get_client(id):
    '''
   GET	/clients/:id	Получить информацию о указанном клиенте
    '''
    pass



@router.post("/")
def creat_new_client(json: client):
    '''
   POST	/clients	Создать нового клиента
   '''
    pass



@router.put("/{id}")
def change_client(id, json: client):
    '''
  PUT	/clients/:id	Обновить информацию о указанном клиенте
    '''
    pass



@router.delete("/{id}")
def delete_client(id):
    '''
   DELETE	/clients/:id	Удалить указанного клиента
    '''
    pass