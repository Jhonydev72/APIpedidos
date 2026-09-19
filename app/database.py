import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://pedidos_user:pedidos_pass@localhost:5432/pedidos_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Gera uma sessão de banco por request e garante o fechamento."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
