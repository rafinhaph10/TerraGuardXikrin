from sqlalchemy import text

from backend.database import engine


def listar_areas():

    with engine.connect() as conn:

        resultado = conn.execute(text("""
            SELECT
                id,
                nome,
                descricao,
                tipo
            FROM areas
            ORDER BY id
        """))

        return [dict(row._mapping) for row in resultado]


def criar_area(nome, descricao, tipo):

    with engine.begin() as conn:

        conn.execute(
            text("""
                INSERT INTO areas
                (nome, descricao, tipo)
                VALUES
                (:nome, :descricao, :tipo)
            """),
            {
                "nome": nome,
                "descricao": descricao,
                "tipo": tipo
            }
        )