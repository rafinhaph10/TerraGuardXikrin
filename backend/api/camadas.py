from fastapi import UploadFile, File, Form, HTTPException
from sqlalchemy import text

from backend.database import engine
from backend.services.upload_service import salvar_upload
from backend.services.geo_service import (
    ler_arquivo_geografico,
    resumir_geodataframe,
    preparar_features,
)
from backend.services.camada_service import criar_camada_com_features


def listar_camadas():
    with engine.connect() as conn:
        resultado = conn.execute(
            text("""
                SELECT
                    id,
                    nome,
                    tipo,
                    descricao,
                    total_features,
                    area_total_ha,
                    perimetro_total_m
                FROM camadas
                WHERE ativo = true
                ORDER BY nome;
            """)
        ).mappings().all()

    return list(resultado)


def upload_camada(
    projeto_id: int = Form(...),
    nome: str = Form(...),
    tipo: str = Form(...),
    descricao: str | None = Form(None),
    arquivo: UploadFile = File(...)
):
    try:
        caminho = salvar_upload(arquivo)
        gdf = ler_arquivo_geografico(caminho)
        resumo = resumir_geodataframe(gdf)
        features = preparar_features(gdf)

        metadata = {
            "arquivo_original": arquivo.filename,
            "arquivo_salvo": str(caminho),
            "crs_final": resumo["crs"],
            "tipo_geometria": resumo["tipo_geometria"],
        }

        camada_id = criar_camada_com_features(
            projeto_id=projeto_id,
            nome=nome,
            tipo=tipo,
            descricao=descricao,
            arquivo_original=arquivo.filename,
            formato=arquivo.filename.split(".")[-1].upper(),
            metadata=metadata,
            resumo=resumo,
            features=features,
        )

        return {
            "message": "Camada e features importadas com sucesso",
            "camada_id": camada_id,
            "resumo": resumo,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_camada_geojson(camada_id: int):
    with engine.connect() as conn:
        rows = conn.execute(
            text("""
                SELECT
                    id,
                    nome,
                    tipo_geometria,
                    area_ha,
                    perimetro_m,
                    atributos,
                    ST_AsGeoJSON(geometry)::json AS geometry
                FROM features
                WHERE camada_id = :camada_id
                ORDER BY id;
            """),
            {"camada_id": camada_id}
        ).mappings().all()

    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": row["geometry"],
                "properties": {
                    "id": row["id"],
                    "nome": row["nome"],
                    "tipo_geometria": row["tipo_geometria"],
                    "area_ha": row["area_ha"],
                    "perimetro_m": row["perimetro_m"],
                    "atributos": row["atributos"],
                },
            }
            for row in rows
        ],
    }