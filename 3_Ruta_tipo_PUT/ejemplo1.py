#importamos lo necesrio de fastappi
from typing import Union
from fastapi import FastAPI

#importamos BaseModel desde pydantic para poder crear el modelo de consulta
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    nombre : str
    precio: float
    esta_en_oferta: Union[bool, None] = None

@app.put('/items/{item_id}')
def update_item(item_id: int, item:Item):
    
    if item.esta_en_oferta:
        mensaje='El producto está en oferta'
    else:
        mensaje='El producto no está en oferta'
    
    return {'Id de item': item_id, 'Nombre de item': item.nombre, 'Precio': item.precio, 'Oferta': mensaje}
