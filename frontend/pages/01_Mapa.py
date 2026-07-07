import requests
import streamlit as st
import folium
from streamlit_folium import st_folium

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="TerraGuard | Mapa",
    layout="wide"
)

st.title("🗺️ TerraGuard - Visualizador GIS")

# =====================================================
# BUSCAR CAMADAS
# =====================================================

try:
    resposta = requests.get(f"{API_URL}/camadas/")
    resposta.raise_for_status()

    camadas = resposta.json()

except Exception as e:
    st.error("Não foi possível conectar à API.")
    st.exception(e)
    st.stop()

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("Camadas")

if len(camadas) == 0:
    st.warning("Nenhuma camada cadastrada.")
    st.stop()

nomes = {
    f"{c['nome']} ({c['tipo']})": c["id"]
    for c in camadas
}

camada_escolhida = st.sidebar.selectbox(
    "Selecione uma camada",
    list(nomes.keys())
)

camada_id = nomes[camada_escolhida]

# =====================================================
# CARREGAR GEOJSON
# =====================================================

geojson = requests.get(
    f"{API_URL}/camadas/{camada_id}/geojson"
).json()

# =====================================================
# MAPA
# =====================================================

mapa = folium.Map(
    location=[-6.35, -50.80],
    zoom_start=8,
    tiles="OpenStreetMap"
)

folium.GeoJson(
    geojson,
    name=camada_escolhida,
    style_function=lambda x: {
        "color": "#0B8F3A",
        "weight": 2,
        "fillOpacity": 0.25,
    },
    tooltip=folium.GeoJsonTooltip(
        fields=[
            "nome",
            "tipo_geometria",
            "area_ha",
            "perimetro_m",
        ],
        aliases=[
            "Nome",
            "Tipo",
            "Área (ha)",
            "Perímetro (m)",
        ],
        localize=True,
    ),
).add_to(mapa)

folium.LayerControl().add_to(mapa)

st_folium(
    mapa,
    width=None,
    height=750,
)