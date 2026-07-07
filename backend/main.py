from fastapi import FastAPI

from backend.api.schemas import AreaCreate
from backend.services.area_service import listar_areas, criar_area

from backend.api.projetos import (
    get_projetos,
    get_projeto,
    post_projeto,
    put_projeto,
    delete_projeto,
)

from backend.api.camadas import (
    listar_camadas,
    upload_camada,
    get_camada_geojson,
)

app = FastAPI(
    title="TerraGuardXikrin API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "TerraGuardXikrin API Online"}


@app.get("/areas")
def get_areas():
    areas = listar_areas()
    return {
        "total": len(areas),
        "areas": areas
    }


@app.post("/areas")
def post_area(area: AreaCreate):
    criar_area(
        nome=area.nome,
        descricao=area.descricao,
        tipo=area.tipo
    )

    return {
        "message": "Área cadastrada com sucesso",
        "area": area
    }


# ===========================
# PROJETOS
# ===========================

app.add_api_route("/projetos/", get_projetos, methods=["GET"], tags=["Projetos"])
app.add_api_route("/projetos/{projeto_id}", get_projeto, methods=["GET"], tags=["Projetos"])
app.add_api_route("/projetos/", post_projeto, methods=["POST"], tags=["Projetos"])
app.add_api_route("/projetos/{projeto_id}", put_projeto, methods=["PUT"], tags=["Projetos"])
app.add_api_route("/projetos/{projeto_id}", delete_projeto, methods=["DELETE"], tags=["Projetos"])


# ===========================
# CAMADAS
# ===========================

app.add_api_route(
    "/camadas/",
    listar_camadas,
    methods=["GET"],
    tags=["Camadas"]
)

app.add_api_route(
    "/camadas/upload",
    upload_camada,
    methods=["POST"],
    tags=["Camadas"]
)

app.add_api_route(
    "/camadas/{camada_id}/geojson",
    get_camada_geojson,
    methods=["GET"],
    tags=["Camadas"]
)