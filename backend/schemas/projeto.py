from pydantic import BaseModel
from typing import Optional


class ProjetoCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None
    cliente: Optional[str] = None
    estado: Optional[str] = None
    pais: Optional[str] = "Brasil"


class ProjetoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    cliente: Optional[str] = None
    estado: Optional[str] = None
    pais: Optional[str] = None
    ativo: Optional[bool] = None