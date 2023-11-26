from fastapi import APIRouter


router = APIRouter(prefix='/deals', tags=['deals'])


@router.get("/")
def get_all_deals():
    '''
   GET	/deals	Получить список всех сделок
    '''
    pass



@router.get("/{id}")
def get_deal(id):
    '''
   GET	/deals/:id	Получить информацию о указанной сделке
    '''
    pass



@router.post("/")
def creat_new_deal(json: deal):
    '''
   POST	/deals	Создать новую сделку
   '''
    pass



@router.put("/{id}")
def change_deal(id, json: deal):
    '''
  PUT	/deals/:id	Обновить информацию о указанной сделке
    '''
    pass



@router.delete("/{id}")
def delete_deal(id):
    '''
    DELETE	/deals/:id	Удалить указанную сделку

    '''
    pass