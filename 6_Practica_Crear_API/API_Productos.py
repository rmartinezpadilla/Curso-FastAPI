#importar fastapi HTTP exception
from fastapi import FastAPI, HTTPException
from models.producto  import Productos
#importamos uuid para los id automaticos
from uuid import uuid4 as uuid
#importamos las excepciones HTTP


app= FastAPI()

lista_productos = []

@app.get('/')
def index():
    return {'Bienvenidos a la API de productos'}

@app.get('/productos')
def obtener_todos_los_productos():
    return lista_productos

@app.get('/productos/{producto_id}')
def obtener_producto_por_id(producto_id: str):
    #forma tradicional
    
    # for p in lista_productos:
    #     if p.id_producto == producto_id:
    #         return p
    
    """usando lamba y mejorando el código"""
    resultado = list(filter(lambda p : p.id_producto == producto_id, lista_productos))
    if len(resultado) > 0:
        return resultado[0]
    
    raise HTTPException(status_code=400, detail=f'Producto {producto_id} No encontrado!')
    #return {'Mensaje': f'Producto con el id {producto_id} no encontrado'}

@app.post('/crearproducto')
def crear_producto(producto: Productos):
    producto.id_producto = str(uuid())
    lista_productos.append(producto)
    return {'Mensaje': f'Producto {producto.nombre_producto}  creado y agregado correctamente!'}