from pydantic import BaseModel

class Usuario(BaseModel):
    #ponemos el ID como opcional
    id: str = None
    cedula : int
    nombres : str
    apellidos : str
    direccion : str