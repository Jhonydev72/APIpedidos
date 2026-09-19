from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.pedido import PedidoCreate, PedidoResponse, StatusUpdate
from app.services import pedido_service

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.post("/", response_model=PedidoResponse, status_code=status.HTTP_201_CREATED)
def criar_pedido(dados: PedidoCreate, db: Session = Depends(get_db)):
    """Cria um novo pedido calculando o valor total."""
    return pedido_service.criar_pedido(db, dados)


@router.get("/{pedido_id}", response_model=PedidoResponse)
def obter_pedido(pedido_id: int, db: Session = Depends(get_db)):
    """Retorna um pedido pelo ID."""
    return pedido_service.obter_pedido(db, pedido_id)


@router.get("/", response_model=list[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):
    """Lista todos os pedidos cadastrados."""
    return pedido_service.listar_pedidos(db)


@router.patch("/{pedido_id}/status", response_model=PedidoResponse)
def atualizar_status(pedido_id: int, dados: StatusUpdate, db: Session = Depends(get_db)):
    """Atualiza exclusivamente o status de um pedido."""
    return pedido_service.atualizar_status_pedido(db, pedido_id, dados)
