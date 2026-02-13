# aca es donde se configuran = SETTINGS DJANGO
from pydantic_settings import BaseSettings
class setting(BaseSettings):
    # Aqui se puede congigurar la conexion a la base de datos, el puerto, etc
    DATABASE_URL: str = "postgresql+asyncpg://postgres:2077@localhost:5433/fastapi_db"


settings = setting()
    