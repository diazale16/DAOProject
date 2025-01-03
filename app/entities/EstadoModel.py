import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..persistency.DBManager import Base

class Estado(Base):
    __tablename__ = 'estados'
    id = Column(String(10), primary_key=True, default=lambda:uuid.uuid4().hex[:10].upper())
    nombre = Column(String, nullable=False)
    # descripcion = Column(Integer, nullable=False)
    
    # Relación inversa con la entidad Cliente
    auto = relationship('Auto', back_populates='estado', lazy="joined")