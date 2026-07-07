from sqlalchemy.orm import Session

from backend.models.projeto import Projeto
from backend.schemas.projeto import ProjetoCreate, ProjetoUpdate


def listar_projetos(db: Session):
    return db.query(Projeto).all()


def buscar_projeto(db: Session, projeto_id: int):
    return db.query(Projeto).filter(
        Projeto.id == projeto_id
    ).first()


def criar_projeto(db: Session, dados: ProjetoCreate):

    projeto = Projeto(**dados.model_dump())

    db.add(projeto)

    db.commit()

    db.refresh(projeto)

    return projeto


def atualizar_projeto(
    db: Session,
    projeto_id: int,
    dados: ProjetoUpdate
):

    projeto = buscar_projeto(db, projeto_id)

    if not projeto:
        return None

    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(projeto, campo, valor)

    db.commit()

    db.refresh(projeto)

    return projeto


def excluir_projeto(
    db: Session,
    projeto_id: int
):

    projeto = buscar_projeto(db, projeto_id)

    if not projeto:
        return False

    db.delete(projeto)

    db.commit()

    return True