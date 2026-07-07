from pydantic import BaseModel


class CamadaUpload(BaseModel):

    projeto_id: int

    nome: str

    tipo: str

    descricao: str | None = None