from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.sql import func

from backend.models import Base


class Projeto(Base):

    __tablename__ = "projetos"

    id = Column(Integer, primary_key=True)

    nome = Column(String(200), nullable=False)

    descricao = Column(Text)

    cliente = Column(String(200))

    estado = Column(String(100))

    pais = Column(String(100), default="Brasil")

    sistema_coordenadas = Column(String(50), default="EPSG:4326")

    ativo = Column(Boolean, default=True)

    data_cadastro = Column(
        DateTime,
        server_default=func.now()
    )