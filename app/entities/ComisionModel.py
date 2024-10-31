from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from ..persistency.DBManager import Base
import uuid

class Comision(Base):
    __tablename__ = 'comisiones'
    id = Column(String(10), primary_key=True, default=lambda: uuid.uuid4().hex[:10].upper())
    monto = Column(Integer, nullable=False)
    fecha = Column(String, nullable=False)
    vendedor_id = Column(String(10), ForeignKey('vendedores.id'), nullable=False)

    # Relación de regreso hacia el vendedor
    vendedor = relationship('Vendedor', back_populates='comision', lazy="joined")
