from typing import Union
from fastapi import FastAPI
from producto import Producto

# Creación de una aplicación FastAPI:
app= FastAPI()

@app.put('/items/{producto_id}')
def update_item(producto_id: int, prod:Producto):
    
    if prod.esta_en_oferta:
        mensaje='El producto está en oferta'
    else:
        mensaje='El producto no está en oferta'
    
    return {'Id de item': producto_id, 'Nombre de item': prod.nombre, 'Precio': prod.precio, 'Oferta': mensaje}