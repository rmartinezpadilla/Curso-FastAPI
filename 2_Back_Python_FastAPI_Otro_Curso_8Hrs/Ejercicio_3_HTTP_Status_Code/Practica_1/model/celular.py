from pydantic import BaseModel

class Celular(BaseModel):
    id : int
    peso : int
    color : str
    marca : str
    operador : str
    dimesion_x : int
    dimesion_y : int
    
    