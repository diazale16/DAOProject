import uuid
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from ..persistency.DBManager import Base
from .AutoModel import Auto
from .ClienteModel import Cliente
from .VendedorModel import Vendedor

class Venta(Base):
    __tablename__ = 'ventas'
    id = Column(String(10), primary_key=True, default=lambda:uuid.uuid4().hex[:10])
    fecha_venta = Column(Date, nullable=False)
    auto_vin = Column(String, ForeignKey('autos.vin'), nullable=False)
    cliente_id = Column(String, ForeignKey('clientes.id'), nullable=False)
    vendedor_id = Column(Float, ForeignKey('vendedores.id'), nullable=False)

    # Relación con la entidad Dirección
    cliente_relacion = relationship('Cliente', back_populates='venta_relacion')
    auto_relacion = relationship('Auto', back_populates='venta_relacion')
    vendedor_relacion = relationship('Vendedor', back_populates='venta_relacion')