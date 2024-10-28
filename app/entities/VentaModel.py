import uuid
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from ..persistency.DBManager import Base
from .AutoModel import Auto
from .ClienteModel import Cliente
from .VendedorModel import Vendedor

class Venta(Base):
    __tablename__ = 'ventas'
    id = Column(String(10), primary_key=True, default=lambda:uuid.uuid4().hex[:10].upper())
    fecha = Column(Date, nullable=False)
    auto_vin = Column(String, ForeignKey('autos.vin'), nullable=False)
    cliente_id = Column(String, ForeignKey('clientes.id'), nullable=False)
    vendedor_id = Column(String, ForeignKey('vendedores.id'), nullable=False)
    monto = Column(Float, nullable=False)

    # Relación con la entidad Dirección
    cliente_relacion = relationship('Cliente', back_populates='venta_relacion', lazy="joined")
    auto_relacion = relationship('Auto', back_populates='venta_relacion', lazy="joined")
    vendedor_relacion = relationship('Vendedor', back_populates='venta_relacion', lazy="joined")