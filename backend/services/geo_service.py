import geopandas as gpd


def ler_arquivo_geografico(caminho_arquivo):
    gdf = gpd.read_file(caminho_arquivo)

    if gdf.empty:
        raise ValueError("O arquivo não possui feições.")

    if gdf.crs is None:
        raise ValueError("O arquivo não possui sistema de coordenadas definido.")

    gdf = gdf.to_crs("EPSG:4326")
    gdf = gdf[gdf.geometry.notnull()]
    gdf = gdf[~gdf.geometry.is_empty]

    if gdf.empty:
        raise ValueError("Todas as geometrias estão vazias ou inválidas.")

    return gdf


def resumir_geodataframe(gdf):
    gdf_metrico = gdf.to_crs("EPSG:5880")

    area_total_ha = float(gdf_metrico.geometry.area.sum() / 10000)
    perimetro_total_m = float(gdf_metrico.geometry.length.sum())

    return {
        "total_features": int(len(gdf)),
        "crs": str(gdf.crs),
        "tipo_geometria": list(gdf.geometry.geom_type.unique()),
        "area_total_ha": round(area_total_ha, 4),
        "perimetro_total_m": round(perimetro_total_m, 2),
    }


def preparar_features(gdf):
    gdf_metrico = gdf.to_crs("EPSG:5880")

    features = []

    for idx, row in gdf.iterrows():
        geom = row.geometry
        geom_metrico = gdf_metrico.loc[idx].geometry

        atributos = row.drop(labels="geometry").to_dict()

        area = None
        if geom.geom_type in ["Polygon", "MultiPolygon"]:
            area = float(geom_metrico.area / 10000)

        perimetro = float(geom_metrico.length)

        features.append({
            "nome": atributos.get("nome") or atributos.get("name") or f"feature_{idx}",
            "atributos": atributos,
            "geometry_wkt": geom.wkt,
            "tipo_geometria": geom.geom_type,
            "area_ha": round(area, 4) if area is not None else None,
            "perimetro_m": round(perimetro, 2),
        })

    return features