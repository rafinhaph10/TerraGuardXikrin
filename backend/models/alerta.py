from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func

from backend.models import Base


class Alerta(Base):

    __tablename__ = "alertas"

    id = Column(Integer, primary_key=True)

    foco_id = Column(Integer, ForeignKey("focos.id"))

    area_id = Column(Integer, ForeignKey("areas.id"))

    tipo = Column(String(100))

    status = Column(String(50))

    observacao = Column(Text)

    data_alerta = Column(
        DateTime,
        server_default=func.now()
    )