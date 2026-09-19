from pydantic import BaseModel, Field
from datetime import datetime


class PedidoCreate(BaseModel):
    """Schema de entrada para criação de pedido."""
    cliente: str = Field(..., min_length=1, examples=["João Silva"])
    produto: str = Field(..., min_length=1, examples=["Notebook"])
    quantidade: int = Field(..., gt=0, examples=[2])
    valor_unitario: float = Field(..., gt=0, examples=[3500.00])


class StatusUpdate(BaseModel):
    """Schema de entrada para atualização de status."""
    status: str = Field(..., min_length=1, examples=["APROVADO"])


class PedidoResponse(BaseModel):
    """Schema de resposta de um pedido."""
    id: int
    cliente: str
    produto: str
    quantidade: int
    valor_unitario: float
    valor_total: float
    status: str
    data_criacao: datetime

    model_config = {"from_attributes": True}
