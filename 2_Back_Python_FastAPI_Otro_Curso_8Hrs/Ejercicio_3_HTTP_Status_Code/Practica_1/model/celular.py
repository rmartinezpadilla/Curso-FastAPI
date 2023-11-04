from pydantic import BaseModel

class Celular(BaseModel):
    id : int
    peso : float
    color : str
    marca : str
    operador : str
    dimesion_x : float
    dimesion_y : float
    
    