from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from ..persistency.DBManager import Base
import uuid

class Vendedor(Base):
    __tablename__ = 'vendedores'
    id = Column(String(10), primary_key=True, default=lambda: uuid.uuid4().hex[:10].upper())
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    comision = Column(Integer, nullable=False) # Porcentaje de comision asignado al vendedor para las ventas o servicios que logre

    # Relación con la entidad Venta
    venta_relacion = relationship('Venta', back_populates='vendedor_relacion', lazy="joined")
    servicio_relacion = relationship('Servicio', back_populates='vendedor_relacion', lazy="joined")
    # Relación con la entidad Comision (uno-a-muchos)
    comision_relacion = relationship('Comision', back_populates='vendedor_relacion', lazy="joined") # cascade="all, delete-orphan", lazy="joined"
