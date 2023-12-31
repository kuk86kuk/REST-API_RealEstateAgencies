from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create engine and session
SQLALCHEMY_DATABASE_URL = 'sqlite:///database.db'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)



# Create base class
Base = declarative_base()



# Create Client model
class Client_table(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    phone_number = Column(String)
    email = Column(String)




# Create Deal model
class Deal_table(Base):
    __tablename__  = 'deal'

    id = Column(Integer, primary_key=True, index=True)
    id_object_realty = Column(Integer)
    id_sobstvenik = Column(Integer)
    id_client = Column(Integer)
    datetime_deal = Column(String)
    amount = Column(Integer)
    currency = Column(String)
    status = Column(String)
    type = Column(String)



# Create ObjectRealty model
class ObjectRealty_table(Base):
    __tablename__ = 'object_realty'

    id = Column(Integer, primary_key=True, index=True)
    tupe_object_realty = Column(String)
    address = Column(String)
    square = Column(Float)
    number_rooms = Column(Integer, nullable=True)
    object_status = Column(String)
    year_construction = Column(Integer)
    price = Column(Integer)
    id_sobstvenik = Column(Integer)
    id_deal = Column(Integer)




