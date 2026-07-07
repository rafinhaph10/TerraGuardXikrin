from sqlalchemy import Column, Integer, String, DateTime, Float
from geoalchemy2 import Geometry

from backend.models import Base


class Foco(Base):

    __tablename__ = "focos"

    id = Column(Integer, primary_key=True)

    fonte = Column(String(50))

    satelite = Column(String(100))

    data_hora = Column(DateTime)

    frp = Column(Float)

    confianca = Column(Float)

    risco_fogo = Column(Float)

    precipitacao = Column(Float)

    latitude = Column(Float)

    longitude = Column(Float)

    municipio = Column(String(150))

    estado = Column(String(100))

    pais = Column(String(100))

    bioma = Column(String(100))

    geometry = Column(
        Geometry(
            geometry_type="POINT",
            srid=4326
        )
    )