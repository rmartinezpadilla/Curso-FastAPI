from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    #ponemos el ID como opcional
    id: Optional[str]
    cedula : int
    nombres : str
    apellidos : str
    direccion : str