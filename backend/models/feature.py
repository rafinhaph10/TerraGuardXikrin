from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Float,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from geoalchemy2 import Geometry

from backend.models import Base


class Feature(Base):

    __tablename__ = "features"

    id = Column(Integer, primary_key=True)

    camada_id = Column(
        Integer,
        ForeignKey("camadas.id"),
        nullable=False
    )

    nome = Column(String(200))

    atributos = Column(JSONB)

    area_ha = Column(Float)

    perimetro_m = Column(Float)

    geometry = Column(
        Geometry(
            geometry_type="GEOMETRY",
            srid=4326
        )
    )

    data_cadastro = Column(
        DateTime,
        server_default=func.now()
    )