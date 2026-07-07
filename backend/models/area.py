from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from geoalchemy2 import Geometry

from backend.models import Base


class Area(Base):

    __tablename__ = "areas"

    id = Column(Integer, primary_key=True)

    nome = Column(String(200), nullable=False)

    descricao = Column(String)

    tipo = Column(String(100))

    origem = Column(String(100))

    responsavel = Column(String(150))

    ativo = Column(Integer, default=1)

    data_cadastro = Column(
        DateTime,
        server_default=func.now()
    )

    data_atualizacao = Column(
        DateTime,
        server_default=func.now()
    )

    srid = Column(Integer, default=4326)

    area_ha = Column(Float)

    perimetro_m = Column(Float)

    bbox = Column(String)

    geometry = Column(
        Geometry(
            geometry_type="MULTIPOLYGON",
            srid=4326
        )
    )

    centroide = Column(
        Geometry(
            geometry_type="POINT",
            srid=4326
        )
    )