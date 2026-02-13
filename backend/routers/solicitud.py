#verdaderamente la magia
# se puede compara a django views
from fastapi import APIRouter, Depends, 
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db import get_db # importo la sesion de la base de datos
from models.solicitud import Solicitud # importo el modelo de la solicitud
from schemas.solicitud import SolicitudCreate, SolicitudResponse # importo los esquemas de la solicitud

"defino el router"

router = APIRouter(
    prefix="/solicitudes", # para poder usar el router con el prefijo /solicitudes al llamar las rutas
    tags=["solicitudes"] #tags para documentacion 
)

#esto de aca es para crear una solicitud despues de peticion/< aqui va el endpoint >
@router.post("/", response_model=SolicitudResponse)
async def crear_solicitud(
    data: SolicitudCreate,
    db: AsyncSession = Depends(get_db)
):
    solicitud = Solicitud(**data.model_dump())
    db.add(solicitud)
    await db.commit()
    await db.refresh(solicitud)
    return solicitud

@router.get("/", response_model=list[SolicitudResponse])
async def listar_solicitudes(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Solicitud))
    return result.scalars().all()