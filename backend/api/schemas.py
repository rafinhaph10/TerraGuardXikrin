from pydantic import BaseModel
from typing import Optional


class AreaCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None
    tipo: Optional[str] = None


class AreaResponse(BaseModel):
    id: int
    nome: str
    descricao: Optional[str]
    tipo: Optional[str]