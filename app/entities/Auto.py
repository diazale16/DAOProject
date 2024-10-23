# entities/auto.py
from sqlalchemy import Column, Integer, String, Float
from ..persistency.DBManager import Base

class Auto(Base):
    __tablename__ = 'autos'
    vin = Column(String, primary_key=True)
    marca = Column(String)
    modelo = Column(String)
    año = Column(Integer)
    precio = Column(Float)
    estado = Column(String)
    cliente_id = Column(Integer, nullable=True)
