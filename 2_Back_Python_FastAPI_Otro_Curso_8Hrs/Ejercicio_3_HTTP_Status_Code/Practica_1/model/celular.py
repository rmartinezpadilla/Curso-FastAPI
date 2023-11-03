from pydantic import BaseModel

class Celular(BaseModel):
    peso : int
    color : str
    operador : str
    dimesion_x : int
    dimesion_y : int
    
    