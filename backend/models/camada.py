from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime,
    Float,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func

from backend.models import Base


class Camada(Base):

    __tablename__ = "camadas"

    id = Column(Integer, primary_key=True)

    projeto_id = Column(
        Integer,
        ForeignKey("projetos.id"),
        nullable=False
    )

    nome = Column(String(200), nullable=False)

    tipo = Column(String(100), nullable=False)

    descricao = Column(Text)

    arquivo_original = Column(String(255))

    formato = Column(String(50))

    metadata = Column(JSONB)

    total_features = Column(Integer)

    area_total_ha = Column(Float)

    perimetro_total_m = Column(Float)

    usuario_importacao = Column(
        Integer,
        ForeignKey("usuarios.id")
    )

    ativo = Column(Boolean, default=True)

    data_importacao = Column(
        DateTime,
        server_default=func.now()
    )