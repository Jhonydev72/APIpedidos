from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.pedido import Pedido
from app.repositories import pedido_repository
from app.schemas.pedido import PedidoCreate, StatusUpdate


def criar_pedido(db: Session, dados: PedidoCreate) -> Pedido:
    """Calcula o valor total e delega a persistência ao repository."""
    valor_total = dados.quantidade * dados.valor_unitario

    pedido = Pedido(
        cliente=dados.cliente,
        produto=dados.produto,
        quantidade=dados.quantidade,
        valor_unitario=dados.valor_unitario,
        valor_total=valor_total,
        status="CRIADO",
    )
    return pedido_repository.criar(db, pedido)


def obter_pedido(db: Session, pedido_id: int) -> Pedido:
    """Retorna um pedido ou levanta 404."""
    pedido = pedido_repository.buscar_por_id(db, pedido_id)
    if pedido is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pedido {pedido_id} não encontrado",
        )
    return pedido


def listar_pedidos(db: Session) -> list[Pedido]:
    """Retorna todos os pedidos."""
    return pedido_repository.listar_todos(db)


def atualizar_status_pedido(db: Session, pedido_id: int, dados: StatusUpdate) -> Pedido:
    """Busca o pedido e atualiza seu status."""
    pedido = obter_pedido(db, pedido_id)
    return pedido_repository.atualizar_status(db, pedido, dados.status)
