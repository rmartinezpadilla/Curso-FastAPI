#importamos lo necesrio de fastappi
from typing import Union

#importamos BaseModel desde pydantic para poder crear el modelo de consulta
from pydantic import BaseModel

class Producto(BaseModel):
    nombre : str
    precio: float
    esta_en_oferta: Union[bool, None] = None