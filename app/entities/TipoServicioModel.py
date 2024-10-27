import uuid
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from ..persistency.DBManager import Base
from .AutoModel import Auto
from .ClienteModel import Cliente
from .VendedorModel import Vendedor

class TipoServicio(Base):
    __tablename__ = 'tipos_servicios'
    id = Column(String(10), primary_key=True, default=lambda:uuid.uuid4().hex[:10].upper())
    nombre = Column(String, nullable=False)
    # fecha_venta = Column(Date, nullable=False)
    # auto = Column(String, ForeignKey('autos.id'), nullable=False)
    # cliente = Column(String, ForeignKey('clientes.id'), nullable=False)
    # vendedor = Column(Float, ForeignKey('vendedores.id'), nullable=False)

    # Relación con la entidad Dirección
    servicio_relacion = relationship('Servicio', back_populates='tipo_servicio_relacion')