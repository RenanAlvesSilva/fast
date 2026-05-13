from sqlalchemy import Column, Integer, String
from .database import Base


class StoreModel(Base):
    __tablename__ = "stores"
    
    id = Column(Integer, primary_key = True, index= True)
    name = Column(String, index = True)
    latitude = Column(String, index = True)
    longitude =Column(String, index = True)
    
    