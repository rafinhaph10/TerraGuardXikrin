from sqlalchemy import text
from backend.database import engine

try:
    with engine.connect() as conn:
        print("✅ Conectado ao banco!")

        banco = conn.execute(text("SELECT current_database();"))
        print("Banco:", banco.scalar())

        versao = conn.execute(text("SELECT PostGIS_Version();"))
        print("PostGIS:", versao.scalar())

except Exception as e:
    print("❌ Erro:")
    print(e)