from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.schemas.projeto import ProjetoCreate, ProjetoUpdate
from backend.services.projeto_service import (
    listar_projetos,
    buscar_projeto,
    criar_projeto,
    atualizar_projeto,
    excluir_projeto
)

router = APIRouter(
    prefix="/projetos",
    tags=["Projetos"]
)


@router.get("/")
def get_projetos(db: Session = Depends(get_db)):
    return listar_projetos(db)


@router.get("/{projeto_id}")
def get_projeto(projeto_id: int, db: Session = Depends(get_db)):
    projeto = buscar_projeto(db, projeto_id)

    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")

    return projeto


@router.post("/")
def post_projeto(
    dados: ProjetoCreate,
    db: Session = Depends(get_db)
):
    return criar_projeto(db, dados)


@router.put("/{projeto_id}")
def put_projeto(
    projeto_id: int,
    dados: ProjetoUpdate,
    db: Session = Depends(get_db)
):
    projeto = atualizar_projeto(db, projeto_id, dados)

    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")

    return projeto


@router.delete("/{projeto_id}")
def delete_projeto(
    projeto_id: int,
    db: Session = Depends(get_db)
):
    sucesso = excluir_projeto(db, projeto_id)

    if not sucesso:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")

    return {"message": "Projeto excluído com sucesso"}