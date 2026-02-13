#aqui esta la clave de fast api 

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker #este es para la conexion asyncrona
from sqlalchemy.orm import DeclarativeBase #esto es para crear las clases de los modelos
from config import settings


#now this the database engine echo= True is for logging the sql statements
engine= create_async_engine(settings.DATABASE_URL, echo=True)

async_session= async_sessionmaker(
    engine, expire_on_commit= False     
)

# the object base for the models 
class Base(DeclarativeBase):
    pass

async def get_db():
    async with async_session() as session:
        yield session #yild es como return pero para generadores es decir que
                        #va a devolver un valor pero la funcion puede seguir ejecutandose despues de eso