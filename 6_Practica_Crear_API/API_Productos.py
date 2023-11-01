#importar fastapi
from fastapi import FastAPI
from models.producto  import Productos
#importamos uuid para los id automaticos
from uuid import uuid4 as uuid

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
    for p in lista_productos:
        if p.id_producto == producto_id:
            return p
    return {'Mensaje': f'Producto con el id {producto_id} no encontrado'}

@app.post('/crearproducto')
def crear_producto(producto: Productos):
    producto.id_producto = str(uuid())
    lista_productos.append(producto)
    return {'Mensaje': f'Producto {producto.nombre_producto}  creado y agregado correctamente!'}