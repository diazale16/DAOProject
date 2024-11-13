import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..persistency.DBManager import Base

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(String(10), primary_key=True, default=lambda:uuid.uuid4().hex[:10].upper())
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    telefono = Column(Integer, nullable=False)
    direccion = Column(String, nullable=False)
    
    # Relación con la entidad Dirección
    auto = relationship('Auto', back_populates='cliente', lazy="joined")
    venta = relationship('Venta', back_populates='cliente', lazy="joined")



