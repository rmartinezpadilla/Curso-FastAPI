from typing import Union
from fastapi import FastAPI
from producto import Producto

app: FastAPI()

@app.put('/items/{item_id}')
def update_item(item_id: int, item:Producto):
    
    if item.esta_en_oferta:
        mensaje='El producto está en oferta'
    else:
        mensaje='El producto no está en oferta'
    
    return {'Id de item': item_id, 'Nombre de item': item.nombre, 'Precio': item.precio, 'Oferta': mensaje}