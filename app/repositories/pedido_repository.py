from sqlalchemy.orm import Session

from app.models.pedido import Pedido


def criar(db: Session, pedido: Pedido) -> Pedido:
    """Persiste um novo pedido no banco de dados."""
    db.add(pedido)
    db.commit()
    db.refresh(pedido)
    return pedido


def buscar_por_id(db: Session, pedido_id: int) -> Pedido | None:
    """Retorna um pedido pelo ID ou None se não existir."""
    return db.query(Pedido).filter(Pedido.id == pedido_id).first()


def listar_todos(db: Session) -> list[Pedido]:
    """Retorna todos os pedidos cadastrados."""
    return db.query(Pedido).all()


def atualizar_status(db: Session, pedido: Pedido, novo_status: str) -> Pedido:
    """Atualiza exclusivamente o status de um pedido existente."""
    pedido.status = novo_status
    db.commit()
    db.refresh(pedido)
    return pedido
