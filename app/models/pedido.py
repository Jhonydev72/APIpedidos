from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime, timezone


class Base(DeclarativeBase):
    pass


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cliente = Column(String, nullable=False)
    produto = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
    valor_unitario = Column(Float, nullable=False)
    valor_total = Column(Float, nullable=False)
    status = Column(String, nullable=False, default="CRIADO")
    data_criacao = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
