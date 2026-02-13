#aca siempre va a ir la generacion de modelos
from sqlalchemy import String,text
from sqlalchemy.orm import Mapped, mapped_column
from db import Base



#ahora creamos el modelo de la solicitud
class Solicitud(Base):
    __tablename__= "peticion" #nombre de la tabla en la base de datos 

    # cuando creamos los campos de la tabla siempre va a ir el tipo de dato y si es llave primaria o no como en el orm de django
    id: Mapped[int]= mapped_column(primary_key=True, index=True)
    nombre: Mapped[str]= mapped_column(String(50), nullable=False)
    rut: Mapped[str]= mapped_column(String(12), nullable=False, unique=True)
    tipo: Mapped[str]= mapped_column(String(20), nullable=False)
    estado: Mapped[str]= mapped_column(String(20), default="en espera")

    