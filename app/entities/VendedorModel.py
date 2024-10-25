import uuid
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..persistency.DBManager import Base
from .ClienteModel import Cliente

class Vendedor(Base):
    __tablename__ = 'vendedores'
    id = Column(String(10), primary_key=True, default=lambda:uuid.uuid4().hex[:10])
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    comisiones = Column(Integer, nullable=False)

    # Relación con la entidad Dirección
    venta_relacion = relationship('Venta', back_populates='vendedor_relacion')