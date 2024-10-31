from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from ..persistency.DBManager import Base
import uuid

class Vendedor(Base):
    __tablename__ = 'vendedores'
    id = Column(String(10), primary_key=True, default=lambda: uuid.uuid4().hex[:10].upper())
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    porc_comision = Column(Integer, nullable=False) # Porcentaje de comision asignado al vendedor para las ventas o servicios que logre

    # Relación con la entidad Venta
    venta = relationship('Venta', back_populates='vendedor', lazy="joined")
    servicio = relationship('Servicio', back_populates='vendedor', lazy="joined")
    # Relación con la entidad Comision (uno-a-muchos)
    comision = relationship('Comision', back_populates='vendedor', lazy="joined") # cascade="all, delete-orphan", lazy="joined"
