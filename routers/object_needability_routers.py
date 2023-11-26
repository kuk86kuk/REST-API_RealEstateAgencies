from fastapi import APIRouter


router = APIRouter(prefix='/object_realty', tags=['object_realty'])


@router.get("/properties")
def get_all_object_realty():
    '''
    GET	/properties	Получить список всех объектов недвижимости
    '''
    pass



@router.get("/properties/{id}")
def get_all_object_realty(id):
    '''
    GET	/properties/:id	Получить информацию об указанном объекте
    '''
    pass



@router.post("/properties")
def creat_new_object_realty(json: realty):
    '''
    POST	/properties	Создать новый объект недвижимости
    '''
    pass



@router.post("/properties/{id}")
def change_object_needability(id, json: realty):
    '''
   PUT	/properties/:id	Обновить информацию об указанном объекте
    '''
    pass



@router.delete("/properties/{id}")
def change_object_needability(id):
    '''
   DELETE	/properties/:id	Удалить указанный объект недвижимости
    '''
    pass