from fastapi import FastAPI

from app.database import engine
from app.models.pedido import Base
from app.api.pedidos import router as pedidos_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Pedidos", version="1.0.0")

app.include_router(pedidos_router)


@app.get("/health", tags=["Health"])
def health_check():
    """Verifica se a aplicação está no ar."""
    return {"status": "ok"}
