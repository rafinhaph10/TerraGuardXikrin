from pathlib import Path
import shutil
from uuid import uuid4

from fastapi import UploadFile, HTTPException


UPLOAD_DIR = Path("data/uploads")

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


EXTENSOES_PERMITIDAS = {
    ".geojson",
    ".json",
    ".zip"
}


TAMANHO_MAXIMO = 200 * 1024 * 1024  # 200 MB


def salvar_upload(arquivo: UploadFile) -> Path:

    extensao = Path(arquivo.filename).suffix.lower()

    if extensao not in EXTENSOES_PERMITIDAS:
        raise HTTPException(
            status_code=400,
            detail=f"Formato '{extensao}' não suportado."
        )

    nome = f"{uuid4()}{extensao}"

    destino = UPLOAD_DIR / nome

    with open(destino, "wb") as buffer:
        shutil.copyfileobj(arquivo.file, buffer)

    return destino