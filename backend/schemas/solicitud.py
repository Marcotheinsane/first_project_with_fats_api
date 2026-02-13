#esto reemplaza a django forms y serializers o el DFR

from pydantic import BaseModel


class SolicitudCreate(BaseModel):
    nombre: str
    rut: str
    tipo: str

class SolicitudResponse(SolicitudCreate):#usa herencia de la clase solicitudCreate
                                        # porque tiene los mismos campos mas el id y estado
    id: int
    estado: str

    class Config:
        from_attributes = True #quiere decir que puede crear el modelo a partir de un objeto ORM