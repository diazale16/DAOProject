import uuid
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from ..persistency.DBManager import Base
from .AutoModel import Auto
from .TipoServicioModel import TipoServicio

class Servicio(Base):
    __tablename__ = 'servicios'
    id = Column(String(10), primary_key=True, default=lambda:uuid.uuid4().hex[:10].upper())
    fecha_servicio = Column(Date, nullable=False)
    costo = Column(Float, nullable=False)
    auto_vin = Column(String, ForeignKey('autos.vin'), nullable=False)
    tipo_servicio_id = Column(String, ForeignKey('tipos_servicios.id'), nullable=False)

    # Relación con la entidad Dirección
    auto_relacion = relationship('Auto', back_populates='servicio_relacion')
    tipo_servicio_relacion = relationship('TipoServicio', back_populates='servicio_relacion')