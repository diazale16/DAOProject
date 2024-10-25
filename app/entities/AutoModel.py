import uuid
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..persistency.DBManager import Base
from .ClienteModel import Cliente
from .EstadoModel import Estado

class Auto(Base):
    __tablename__ = 'autos'
    vin = Column(String(17), primary_key=True, default=lambda:uuid.uuid4().hex[:17])
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    año = Column(Integer, nullable=False)
    precio = Column(Float, nullable=False)
    # estado = Column(String, nullable=False)
    estado_id = Column(String, ForeignKey('estados.id'), nullable=False)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=True)

    # Relación con la entidad Dirección
    cliente_relacion = relationship('Cliente', back_populates='auto_relacion')
    estado_relacion = relationship('Estado', back_populates='auto_relacion')
    venta_relacion = relationship('Venta', back_populates='auto_relacion')
    servicio_relacion = relationship('Servicio', back_populates='auto_relacion')