from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from backend.models import Base


class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)

    nome = Column(String(150), nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    senha_hash = Column(String, nullable=False)

    perfil = Column(String(50), default="usuario")

    ativo = Column(Boolean, default=True)

    data_cadastro = Column(
        DateTime,
        server_default=func.now()
    )