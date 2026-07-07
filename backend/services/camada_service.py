import json

from sqlalchemy import text

from backend.database import engine


def criar_camada_com_features(
    projeto_id,
    nome,
    tipo,
    descricao,
    arquivo_original,
    formato,
    metadata,
    resumo,
    features
):
    with engine.begin() as conn:
        resultado = conn.execute(
            text("""
                INSERT INTO camadas (
                    projeto_id,
                    nome,
                    tipo,
                    descricao,
                    arquivo_original,
                    formato,
                    metadata,
                    total_features,
                    area_total_ha,
                    perimetro_total_m
                )
                VALUES (
                    :projeto_id,
                    :nome,
                    :tipo,
                    :descricao,
                    :arquivo_original,
                    :formato,
                    CAST(:metadata AS jsonb),
                    :total_features,
                    :area_total_ha,
                    :perimetro_total_m
                )
                RETURNING id;
            """),
            {
                "projeto_id": projeto_id,
                "nome": nome,
                "tipo": tipo,
                "descricao": descricao,
                "arquivo_original": arquivo_original,
                "formato": formato,
                "metadata": json.dumps(metadata, default=str),
                "total_features": resumo["total_features"],
                "area_total_ha": resumo["area_total_ha"],
                "perimetro_total_m": resumo["perimetro_total_m"],
            }
        )

        camada_id = resultado.scalar()

        for feature in features:
            conn.execute(
                text("""
                    INSERT INTO features (
                        camada_id,
                        nome,
                        atributos,
                        geometry,
                        tipo_geometria,
                        area_ha,
                        perimetro_m,
                        centroide,
                        bbox
                    )
                    VALUES (
                        :camada_id,
                        :nome,
                        CAST(:atributos AS jsonb),
                        ST_GeomFromText(:geometry_wkt, 4326),
                        :tipo_geometria,
                        :area_ha,
                        :perimetro_m,
                        ST_Centroid(ST_GeomFromText(:geometry_wkt, 4326)),
                        ST_Envelope(ST_GeomFromText(:geometry_wkt, 4326))
                    );
                """),
                {
                    "camada_id": camada_id,
                    "nome": feature["nome"],
                    "atributos": json.dumps(feature["atributos"], default=str),
                    "geometry_wkt": feature["geometry_wkt"],
                    "tipo_geometria": feature["tipo_geometria"],
                    "area_ha": feature["area_ha"],
                    "perimetro_m": feature["perimetro_m"],
                }
            )

        return camada_id