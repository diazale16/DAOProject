import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..persistency.DBManager import Base

class Direccion(Base):
    __tablename__ = 'direcciones'
    id = Column(String(10), primary_key=True, default=lambda:uuid.uuid4().hex[:10])
    calle = Column(String, nullable=False)
    numero_calle = Column(Integer, nullable=False)
    ciudad = Column(String, nullable=False)
    codigo_postal = Column(String, nullable=False)
    
    # Relación inversa con la entidad Cliente
    cliente_relacion = relationship('Cliente', back_populates='direccion_relacion')