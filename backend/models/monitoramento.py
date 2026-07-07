from sqlalchemy import Column, Integer, String, DateTime, Float, Text

from backend.models import Base


class Monitoramento(Base):

    __tablename__ = "monitoramentos"

    id = Column(Integer, primary_key=True)

    origem = Column(String(100))

    data_execucao = Column(DateTime)

    focos_encontrados = Column(Integer)

    tempo_execucao = Column(Float)

    observacao = Column(Text)