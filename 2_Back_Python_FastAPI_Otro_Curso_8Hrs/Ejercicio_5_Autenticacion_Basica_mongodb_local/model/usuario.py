#importamos pydantic para definir la entidad
from pydantic import BaseModel

class Usuario(BaseModel):
    cedula : int
    nombres : str
    apellidos : str
    direccion : str