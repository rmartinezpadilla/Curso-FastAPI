#importamos lo necesrio de fastappi
from typing import Union
from fastapi import FastAPI

#importamos BaseModel desde pydantic para poder crear el modelo de consulta
from pydantic import BaseModel


app = FastAPI()

class Producto(BaseModel):
    nombre : str
    precio: float
    esta_en_oferta: Union[bool, None] = None