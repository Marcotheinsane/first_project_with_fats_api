import asyncio #para correr funciones asincronas

from db import engine, Base
from models.solicitud import Solicitud

async def crear_tablas():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(crear_tablas())