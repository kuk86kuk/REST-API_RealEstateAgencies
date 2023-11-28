from fastapi import FastAPI
from app.database.model import Base, engine
from app.routers import clients_routers, deal_routers, object_realty_routers
from sqlalchemy.orm import sessionmaker, Session
from fastapi.openapi.utils import get_openapi

Base.metadata.create_all(engine)
# создаем сессию подключения к бд
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()
 

app = FastAPI()
app.include_router(clients_routers.router)
app.include_router(deal_routers.router)
app.include_router(object_realty_routers.router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="REST-API_RealEstateAgencies",
        version="1.0.1",
        description="This is a very custom OpenAPI schema, Система предоставляет API, позволяющее агентству управлять информацией о недвижимости.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

