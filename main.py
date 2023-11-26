from fastapi import FastAPI
from app.database.model import Base, engine
from app.routers import clients, deal, object_realty_routers
from sqlalchemy.orm import sessionmaker, Session

Base.metadata.create_all(engine)
# создаем сессию подключения к бд
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()
 

app = FastAPI()
app.include_router(clients.router)
app.include_router(deal.router)
app.include_router(object_realty_routers.router)


