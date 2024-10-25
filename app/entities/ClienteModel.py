import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..persistency.DBManager import Base
from .DireccionModel import Direccion

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(String(10), primary_key=True, default=lambda:uuid.uuid4().hex[:10])
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    telefono = Column(Integer, nullable=False)
    direccion = Column(Integer, ForeignKey('direcciones.id'))
    
    # Relación con la entidad Dirección
    direccion_relacion = relationship('Direccion', back_populates='cliente_relacion')
    auto_relacion = relationship('Auto', back_populates='cliente_relacion')
    venta_relacion = relationship('Venta', back_populates='cliente_relacion')



